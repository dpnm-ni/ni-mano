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


class VNFFlavor(object):
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
        'id': 'str',
        'name': 'str',
        'capacity_mbps': 'int',
        'delay_us': 'int',
        'n_cores': 'int',
        'ram_mb': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'capacity_mbps': 'capacity_mbps',
        'delay_us': 'delay_us',
        'n_cores': 'n_cores',
        'ram_mb': 'ram_mb'
    }

    def __init__(self, id=None, name=None, capacity_mbps=None, delay_us=None, n_cores=None, ram_mb=None, _configuration=None):  # noqa: E501
        """VNFFlavor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._capacity_mbps = None
        self._delay_us = None
        self._n_cores = None
        self._ram_mb = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if capacity_mbps is not None:
            self.capacity_mbps = capacity_mbps
        if delay_us is not None:
            self.delay_us = delay_us
        if n_cores is not None:
            self.n_cores = n_cores
        if ram_mb is not None:
            self.ram_mb = ram_mb

    @property
    def id(self):
        """Gets the id of this VNFFlavor.  # noqa: E501


        :return: The id of this VNFFlavor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VNFFlavor.


        :param id: The id of this VNFFlavor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VNFFlavor.  # noqa: E501


        :return: The name of this VNFFlavor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VNFFlavor.


        :param name: The name of this VNFFlavor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def capacity_mbps(self):
        """Gets the capacity_mbps of this VNFFlavor.  # noqa: E501


        :return: The capacity_mbps of this VNFFlavor.  # noqa: E501
        :rtype: int
        """
        return self._capacity_mbps

    @capacity_mbps.setter
    def capacity_mbps(self, capacity_mbps):
        """Sets the capacity_mbps of this VNFFlavor.


        :param capacity_mbps: The capacity_mbps of this VNFFlavor.  # noqa: E501
        :type: int
        """

        self._capacity_mbps = capacity_mbps

    @property
    def delay_us(self):
        """Gets the delay_us of this VNFFlavor.  # noqa: E501


        :return: The delay_us of this VNFFlavor.  # noqa: E501
        :rtype: int
        """
        return self._delay_us

    @delay_us.setter
    def delay_us(self, delay_us):
        """Sets the delay_us of this VNFFlavor.


        :param delay_us: The delay_us of this VNFFlavor.  # noqa: E501
        :type: int
        """

        self._delay_us = delay_us

    @property
    def n_cores(self):
        """Gets the n_cores of this VNFFlavor.  # noqa: E501


        :return: The n_cores of this VNFFlavor.  # noqa: E501
        :rtype: int
        """
        return self._n_cores

    @n_cores.setter
    def n_cores(self, n_cores):
        """Sets the n_cores of this VNFFlavor.


        :param n_cores: The n_cores of this VNFFlavor.  # noqa: E501
        :type: int
        """

        self._n_cores = n_cores

    @property
    def ram_mb(self):
        """Gets the ram_mb of this VNFFlavor.  # noqa: E501


        :return: The ram_mb of this VNFFlavor.  # noqa: E501
        :rtype: int
        """
        return self._ram_mb

    @ram_mb.setter
    def ram_mb(self, ram_mb):
        """Sets the ram_mb of this VNFFlavor.


        :param ram_mb: The ram_mb of this VNFFlavor.  # noqa: E501
        :type: int
        """

        self._ram_mb = ram_mb

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
        if issubclass(VNFFlavor, dict):
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
        if not isinstance(other, VNFFlavor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VNFFlavor):
            return True

        return self.to_dict() != other.to_dict()
