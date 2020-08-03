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


class NetworkPort(object):
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
        'port_id': 'str',
        'port_name': 'str',
        'network_id': 'str',
        'ip_addresses': 'list[str]'
    }

    attribute_map = {
        'port_id': 'port_id',
        'port_name': 'port_name',
        'network_id': 'network_id',
        'ip_addresses': 'ip_addresses'
    }

    def __init__(self, port_id=None, port_name=None, network_id=None, ip_addresses=None):  # noqa: E501
        """NetworkPort - a model defined in Swagger"""  # noqa: E501

        self._port_id = None
        self._port_name = None
        self._network_id = None
        self._ip_addresses = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if port_name is not None:
            self.port_name = port_name
        if network_id is not None:
            self.network_id = network_id
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses

    @property
    def port_id(self):
        """Gets the port_id of this NetworkPort.  # noqa: E501


        :return: The port_id of this NetworkPort.  # noqa: E501
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NetworkPort.


        :param port_id: The port_id of this NetworkPort.  # noqa: E501
        :type: str
        """

        self._port_id = port_id

    @property
    def port_name(self):
        """Gets the port_name of this NetworkPort.  # noqa: E501


        :return: The port_name of this NetworkPort.  # noqa: E501
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """Sets the port_name of this NetworkPort.


        :param port_name: The port_name of this NetworkPort.  # noqa: E501
        :type: str
        """

        self._port_name = port_name

    @property
    def network_id(self):
        """Gets the network_id of this NetworkPort.  # noqa: E501


        :return: The network_id of this NetworkPort.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NetworkPort.


        :param network_id: The network_id of this NetworkPort.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this NetworkPort.  # noqa: E501


        :return: The ip_addresses of this NetworkPort.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this NetworkPort.


        :param ip_addresses: The ip_addresses of this NetworkPort.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

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
        if issubclass(NetworkPort, dict):
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
        if not isinstance(other, NetworkPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
