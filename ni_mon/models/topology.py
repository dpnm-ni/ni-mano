# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_mon.models.base_model_ import Model
from ni_mon import util


class Topology(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, nodes: List[str]=None, links: List[str]=None):  # noqa: E501
        """Topology - a model defined in Swagger

        :param nodes: The nodes of this Topology.  # noqa: E501
        :type nodes: List[str]
        :param links: The links of this Topology.  # noqa: E501
        :type links: List[str]
        """
        self.swagger_types = {
            'nodes': List[str],
            'links': List[str]
        }

        self.attribute_map = {
            'nodes': 'nodes',
            'links': 'links'
        }

        self._nodes = nodes
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'Topology':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Topology of this Topology.  # noqa: E501
        :rtype: Topology
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nodes(self) -> List[str]:
        """Gets the nodes of this Topology.

        List of node ids  # noqa: E501

        :return: The nodes of this Topology.
        :rtype: List[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: List[str]):
        """Sets the nodes of this Topology.

        List of node ids  # noqa: E501

        :param nodes: The nodes of this Topology.
        :type nodes: List[str]
        """

        self._nodes = nodes

    @property
    def links(self) -> List[str]:
        """Gets the links of this Topology.

        List of link ids  # noqa: E501

        :return: The links of this Topology.
        :rtype: List[str]
        """
        return self._links

    @links.setter
    def links(self, links: List[str]):
        """Sets the links of this Topology.

        List of link ids  # noqa: E501

        :param links: The links of this Topology.
        :type links: List[str]
        """

        self._links = links
