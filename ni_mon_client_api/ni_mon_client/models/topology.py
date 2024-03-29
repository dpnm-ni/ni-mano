# coding: utf-8

"""
    NI-Mon

    Monitoring module for NI project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: vantu.bkhn@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ni_mon_client.configuration import Configuration


class Topology(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'nodes': 'list[str]',
        'links': 'list[str]'
    }

    attribute_map = {
        'nodes': 'nodes',
        'links': 'links'
    }

    def __init__(self, nodes=None, links=None, _configuration=None):  # noqa: E501
        """Topology - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nodes = None
        self._links = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if links is not None:
            self.links = links

    @property
    def nodes(self):
        """Gets the nodes of this Topology.  # noqa: E501

        List of node ids  # noqa: E501

        :return: The nodes of this Topology.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Topology.

        List of node ids  # noqa: E501

        :param nodes: The nodes of this Topology.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def links(self):
        """Gets the links of this Topology.  # noqa: E501

        List of link ids  # noqa: E501

        :return: The links of this Topology.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Topology.

        List of link ids  # noqa: E501

        :param links: The links of this Topology.  # noqa: E501
        :type: list[str]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Topology, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Topology):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Topology):
            return True

        return self.to_dict() != other.to_dict()
