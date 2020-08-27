/**
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

/* global Hogan */
/* Namespace for core functionality related to Network Topology. */

horizon.ni_topology = {
  fa_globe_glyph: '\uf0ac',
  fa_globe_glyph_width: 15,
  svg:'#topology_canvas',
  nodes: [],
  links: [],
  data: [],
  zoom: d3.behavior.zoom(),
  data_loaded: false,
  svg_container:'#niTopologyCanvasContainer',
  balloonTmpl : null,
  balloon_deviceTmpl : null,
  balloon_computeTmpl : null,
  balloon_instanceTmpl : null,
  network_index: {},
  balloonID:null,
  network_height : 0,

  init:function() {
    var self = this;

    self.$loading_template = horizon.loader.inline(gettext('Loading')).hide().prependTo($(self.svg_container));

    console.log(topo_data);

    self.data = {};
    self.data.routers = {};
    self.data.vnfs = {};
    self.data.computes = {};

    // Setup balloon popups
    self.balloonTmpl = Hogan.compile(angular.element('#balloon_container').html());
    self.balloon_deviceTmpl = Hogan.compile(angular.element('#balloon_device').html());
    self.balloon_instanceTmpl = Hogan.compile(angular.element('#balloon_instance').html());
    self.balloon_computeTmpl = Hogan.compile(angular.element('#balloon_compute').html());

    angular.element(document)
      .on('click', 'a.closeTopologyBalloon', function(e) {
        e.preventDefault();
        self.delete_balloon();
      })
      .on('click', '.topologyBalloon', function(e) {
        e.stopPropagation();
      })
      .on('click', 'a.vnc_window', function(e) {
        e.preventDefault();
        var vncWindow = window.open(angular.element(this).attr('href'), vncWindow, 'width=760,height=560');
        self.delete_balloon();
      });

    angular.element('#toggle_labels').change(function() {
      horizon.cookies.put('show_labels', this.checked);
      self.refresh_labels();
    });

    angular.element('#center_topology').click(function() {
     this.blur(); // remove btn focus after click
     self.delete_balloon();
      // move visualization to the center and reset scale
      self.vis.transition()
        .duration(1500)
        .attr('transform', 'translate(0,0)scale(1)');

      // reset internal zoom translate and scale parameters so on next
      // move the objects do not jump to the old position
      self.zoom.translate([0,0]);
      self.zoom.scale(1);
      self.translate = null;
    });

    // set up loader first thing
    self.$loading_template.show();
    self.create_vis();
    self.force_direction(0.05,70,-700);

    d3.select(window).on('resize', function() {
      var width = angular.element('#niTopologyCanvasContainer').width();
      var height = angular.element('#niTopologyCanvasContainer').height();
      self.force.size([width, height]).resume();
    });

    self.load_topology(topo_data);
  },


  Router: function(data) {
    for (var key in data) {
      if ({}.hasOwnProperty.call(data, key)) {
        this[key] = data[key];
      }
    }
    this.iconType = 'path';
    this.svg = 'router';
    this.type = 'router';
  },

  Vnf :function(data) {
    for (var key in data) {
      if ({}.hasOwnProperty.call(data, key)) {
        this[key] = data[key];
      }
    }
    this.iconType = 'text';
    this.icon = '\uf108'; // self.Vnf
    this.type = 'instance';
  },

  Compute: function(data) {
    for (var key in data) {
      if ({}.hasOwnProperty.call(data, key)) {
        this[key] = data[key];
      }
    }
    this.iconType = 'text';
    this.icon = '\uf233'; // Compute
    this.type = 'compute';
    this.ip_addresses = [];
  },

  listContains: function(obj, list) {
    // Function to help checking if an object is present on a list
    for (var i = 0; i < list.length; i++) {
      if (angular.equals(list[i], obj)) {
        return true;
      }
    }
    return false;
  },

  // Shows/Hides graph labels
  refresh_labels: function() {
    var show_labels = horizon.cookies.get('show_labels') == 'true';
    angular.element('.nodeLabel').toggle(show_labels);
  },

  // Load config from cookie
  load_config: function() {
    var self = this;

    var labels = horizon.cookies.get('show_labels') == 'true';

    if(labels) {
      angular.element('#toggle_labels_label').addClass('active');
      angular.element('#toggle_labels').prop('checked', labels);
      self.refresh_labels();
    }
  },

  getScreenCoords: function(x, y) {
    var self = this;
    if (self.translate) {
      var xn = self.translate[0] + x * self.zoom.scale();
      var yn = self.translate[1] + y * self.zoom.scale();
      return { x: xn, y: yn };
    } else {
      return { x: x, y: y };
    }
  },

  // Setup the main visualisation
  create_vis: function() {
    var self = this;
    angular.element('#niTopologyCanvasContainer').find('svg').remove();

    // Main svg
    self.outer_group = d3.select('#niTopologyCanvasContainer').append('svg')
      .attr('width', '100%')
      .attr('height', angular.element(document).height() - 200 + "px")
      .attr('pointer-events', 'all')
      .append('g')
      .call(self.zoom
        .scaleExtent([0.1,1.5])
        .on('zoom', function() {
            self.delete_balloon();
            self.vis.attr('transform', 'translate(' + d3.event.translate + ')scale(' +
              self.zoom.scale() + ')');
            self.translate = d3.event.translate;
          })
        )
      .on('dblclick.zoom', null);

    // Background for capturing mouse events
    self.outer_group.append('rect')
      .attr('width', '100%')
      .attr('height', '100%')
      .attr('fill', 'white')
      .on('click', function() {
        self.delete_balloon();
      });

    // svg wrapper for nodes to sit on
    self.vis = self.outer_group.append('g');
  },

  // Setup the force direction
  force_direction: function(grav, dist, ch) {
    var self = this;

    angular.element('[data-toggle="tooltip"]').tooltip({container: 'body'});
    self.curve = d3.svg.line()
      .interpolate('cardinal-closed')
      .tension(0.85);
    self.fill = d3.scale.category10();

    self.force = d3.layout.force()
      .gravity(grav)
      .linkDistance(function(d) {
          return dist;
      })
      .charge(ch)
      .size([angular.element('#niTopologyCanvasContainer').width(),
             angular.element('#niTopologyCanvasContainer').height()])
      .nodes(self.nodes)
      .links(self.links)
      .on('tick', function() {
        self.vis.selectAll('g.node')
          .attr('transform', function(d) {
            return 'translate(' + d.x + ',' + d.y + ')';
          });

        self.vis.selectAll('line.link')
          .attr('x1', function(d) { return d.source.x; })
          .attr('y1', function(d) { return d.source.y; })
          .attr('x2', function(d) { return d.target.x; })
          .attr('y2', function(d) { return d.target.y; });
      });
  },

  // Create a new node
  new_node: function(data, x, y) {
    var self = this;
    data = {data: data};
    if (x && y) {
      data.x = x;
      data.y = y;
    }
    self.nodes.push(data);

    var node = self.vis.selectAll('g.node').data(self.nodes);
    var nodeEnter = node.enter().append('g')
      .attr('class', 'node')
      .style('fill', 'white')
      .call(self.force.drag);

    nodeEnter.append('circle')
      .attr('class', 'frame')
      .attr('r', function(d) {
        switch (Object.getPrototypeOf(d.data)) {
          case self.Router.prototype:
            return 20;
          case self.Vnf.prototype:
            return 15;
          case self.Compute.prototype:
            return 20;
        }
      })
      .style('fill', 'white')
      .style('stroke', 'black')
      .style('stroke-width', 2);

    switch (data.data.iconType) {
      case 'text':
        nodeEnter.append('text')
          .style('fill', 'black')
          .style('font', '20px FontAwesome')
          .attr('text-anchor', 'middle')
          .attr('dominant-baseline', 'central')
          .text(function(d) { return d.data.icon; })
          .attr('transform', function(d) {
            switch (Object.getPrototypeOf(d.data)) {
              case self.Vnf.prototype:
                return 'scale(0.75)';
              case self.Compute.prototype:
                return 'scale(1.2)';
            }
          });
        break;
      case 'path':
        nodeEnter.append('path')
          .attr('class', 'svgpath')
          .style('fill', 'black')
          .attr('d', function(d) { return self.svgs(d.data.svg); })
          .attr('transform', function() {
            return 'scale(0.8)translate(-16,-15)';
          });
        break;
    }

    nodeEnter.append('text')
      .attr('class', 'nodeLabel')
      .style('display',function() {
        return 'inline';
      })
      .style('fill','black')
      .text(function(d) {
        return d.data.name;
      })
      .attr('transform', function(d) {
        switch (Object.getPrototypeOf(d.data)) {
          case self.Router.prototype:
            return 'translate(25,3)';
          case self.Vnf.prototype:
            return 'translate(20,3)';
          case self.Compute.prototype:
            return 'translate(25,3)';
        }
      });

    nodeEnter.on('click', function(d) {
      self.show_balloon(d.data, d, angular.element(this));
    });

    // Highlight the links for currently selected node
    nodeEnter.on('mouseover', function(d) {
      self.vis.selectAll('line.link').filter(function(z) {
        if (z.source === d || z.target === d) {
          return true;
        } else {
          return false;
        }
      }).style('stroke-width', '3px');
    });

    // Remove the highlight on the links
    nodeEnter.on('mouseout', function() {
      self.vis.selectAll('line.link').style('stroke-width','1px');
    });
  },

  new_link: function(source, target) {
    var self = this;
    self.links.push({source: source, target: target});
    var line = self.vis.selectAll('line.link').data(self.links);
    line.enter().insert('line', 'g.node')
      .attr('class', 'link')
      .attr('x1', function(d) { return d.source.x; })
      .attr('y1', function(d) { return d.source.y; })
      .attr('x2', function(d) { return d.target.x; })
      .attr('y2', function(d) { return d.target.y; })
      .style('stroke', 'black')
      .style('stroke-width', 1);
  },

  find_by_id: function(id) {
    var self = this;
    var obj, _i, _len, _ref;
    _ref = self.vis.selectAll('g.node').data();
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      obj = _ref[_i];
      if (obj.data.id == id) {
        return obj;
      }
    }
    return undefined;
  },

  already_in_graph: function(data, node) {
    // All other node types have UUIDs
    for (var n in data) {
      if (n == node.id) {
        return true;
      }
    }
    return false;
  },

  load_topology: function(data) {
    var self = this;
    var net, _i, _netlen, _netref, rou, _j, _roulen, _rouref, port, _l, _portlen, _portref,
        vnf, _k, _vnflen, _vnfref, obj, vmCount;
    var change = false;
    var filterNode = function(obj) {
      return function(d) {
        return obj == d.data;
      };
    };

    // self.Routers
    _rouref = data.routers;
    for (_j = 0, _roulen = _rouref.length; _j < _roulen; _j++) {
      rou = _rouref[_j];
      var router = new self.Router(rou);
      if (!self.already_in_graph(self.data.routers, router)) {
        self.new_node(router);
        change = true;
      } else {
        obj = self.find_by_id(router.id);
        if (obj) {
          obj.data = router;
        }
      }
      self.data.routers[router.id] = router;
    }

    // self.Compute
    _computeref = data.computes;
    for (_k = 0, _computelen = _computeref.length; _k < _computelen; _k++) {
      compute = _computeref[_k];
      var compute = new self.Compute(compute);
      if (!self.already_in_graph(self.data.computes, compute)) {
        self.new_node(compute);
        change = true;
      } else {
        obj = self.find_by_id(compute.id);
        if (obj) {
          obj.data = compute;
        }
      }
      self.data.computes[compute.id] = compute;
    }

    // self.Vnfs
    _vnfref = data.vnfs;
    for (_k = 0, _vnflen = _vnfref.length; _k < _vnflen; _k++) {
      vnf = _vnfref[_k];
      var vnf = new self.Vnf(vnf);
      if (!self.already_in_graph(self.data.vnfs, vnf)) {
        self.new_node(vnf);
        self.new_link(self.find_by_id(vnf.id), self.find_by_id(vnf.node_id));
        change = true;
      } else {
        obj = self.find_by_id(vnf.id);
        if (obj) {
          obj.data = vnf;
        }
      }
      self.data.vnfs[vnf.id] = vnf;
    }

    // links
    _linkref = data.links;
    for (_k = 0, _linklen = _linkref.length; _k < _linklen; _k++) {
      link = _linkref[_k];
      self.new_link(self.find_by_id(link.node1_id), self.find_by_id(link.node2_id));
    }

    if (change) {
        self.force.start();
    }
    self.load_config();
    self.$loading_template.hide();
  },



  removeLink: function(link) {
    var i, index, l, _i, _len, _ref;
    index = -1;
    _ref = this.links;
    for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
      l = _ref[i];
      if (l === link) {
        index = i;
        break;
      }
    }
    if (index !== -1) {
      this.links.splice(index, 1);
    }
    return this.vis.selectAll('line.link').data(this.links).exit().remove();
  },


  show_balloon: function(d,d2,element) {
    var self = this;
    var balloonTmpl = self.balloonTmpl;
    var deviceTmpl = self.balloon_deviceTmpl;
    var computeTmpl = self.balloon_computeTmpl;
    var instanceTmpl = self.balloon_instanceTmpl;
    var balloonID = 'bl_' + d.id;
    var subnets = [];
    if (self.balloonID) {
      if (self.balloonID == balloonID) {
        self.delete_balloon();
        return;
      }
      self.delete_balloon();
    }
    self.force.stop();

    var htmlData = {
      balloon_id:balloonID,
      id:d.id,
      url:d.url,
      name:d.name,
      type:d.type,
      status:d.status,
      status_class: (d.status === 'enabled') ? 'active' : 'down',
      status_label: gettext('STATUS'),
      id_label: gettext('ID'),
      view_details_label: gettext('View Details'),
      ips_label: gettext('IP Addresses')
    };

    var html;
    if (d instanceof self.Vnf) {
      htmlData.view_details_label = gettext('View Instance Details');
      htmlData.ports = d.ports;
      htmlData.url = `/dashboard/admin/instances/${d.id}/detail`;
      html = balloonTmpl.render(htmlData,{
        table1:deviceTmpl,
        table2:instanceTmpl
      });
    } else if (d instanceof self.Compute) {
      htmlData.compute_info = d;
      html = balloonTmpl.render(htmlData,{
        table1:deviceTmpl,
        table2:computeTmpl
      });
    } else {
      return;
    }
    angular.element(self.svg_container).append(html);
    var devicePosition = self.getScreenCoords(d2.x, d2.y);
    var x = devicePosition.x;
    var y = devicePosition.y;
    var xoffset = 100;
    var yoffset = 95;
    angular.element('#' + balloonID).css({
      'left': x + xoffset + 'px',
      'top': y + yoffset + 'px'
    }).show();
    var _balloon = angular.element('#' + balloonID);
    if (element.x + _balloon.outerWidth() > angular.element(window).outerWidth()) {
      _balloon
        .css({
          'left': 0 + 'px'
        })
        .css({
          'left': (x - _balloon.outerWidth() + 'px')
        })
        .addClass('leftPosition');
    }
    _balloon.find('.delete-device').click(function() {
      var _this = angular.element(this);
      var delete_modal = horizon.datatables.confirm(_this);
      delete_modal.find('.btn.btn-danger').click(function () {
        _this.prop('disabled', true);
        d3.select('#id_' + _this.data('device-id')).classed('loading',true);
      });
    });
    self.balloonID = balloonID;
  },

  delete_balloon:function() {
    var self = this;
    if (self.balloonID) {
      angular.element('#' + self.balloonID).remove();
      self.balloonID = null;
      self.force.start();
    }
  },

  svgs: function(name) {
    switch (name) {
      case 'router':
        return 'm 26.628571,16.08 -8.548572,0 0,8.548571 2.08,-2.079998 6.308572,6.30857 4.38857,-4.388572 -6.308571,-6.30857 z m -21.2571429,-4.159999 8.5485709,0 0,-8.5485723 -2.08,2.08 L 5.5314281,-0.85714307 1.1428571,3.5314287 7.4514281,9.84 z m -3.108571,7.268571 0,8.548571 8.5485709,0 L 8.7314281,25.657144 15.039999,19.325715 10.674285,14.96 4.3428571,21.268573 z M 29.737142,8.8114288 l 0,-8.54857147 -8.548572,0 2.08,2.07999987 -6.308571,6.3085716 4.388572,4.3885722 6.308571,-6.3085723 z';
      default:
        return '';
    }
  }
};

