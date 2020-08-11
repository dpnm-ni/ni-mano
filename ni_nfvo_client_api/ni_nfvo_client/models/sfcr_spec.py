# coding: utf-8

"""
    NI-NFVO

    NFVO module service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: vantu.bkhn@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SfcrSpec(object):
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
        'name': 'str',
        'source_client': 'str',
        'destination_client': 'str',
        'src_ip_prefix': 'str',
        'dst_ip_prefix': 'str',
        'src_port_min': 'int',
        'src_port_max': 'int',
        'dst_port_min': 'int',
        'dst_port_max': 'int',
        'proto': 'str',
        'bw': 'int',
        'delay': 'int',
        'duration': 'int',
        'nf_chain': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'source_client': 'source_client',
        'destination_client': 'destination_client',
        'src_ip_prefix': 'src_ip_prefix',
        'dst_ip_prefix': 'dst_ip_prefix',
        'src_port_min': 'src_port_min',
        'src_port_max': 'src_port_max',
        'dst_port_min': 'dst_port_min',
        'dst_port_max': 'dst_port_max',
        'proto': 'proto',
        'bw': 'bw',
        'delay': 'delay',
        'duration': 'duration',
        'nf_chain': 'nf_chain'
    }

    def __init__(self, name=None, source_client=None, destination_client=None, src_ip_prefix=None, dst_ip_prefix=None, src_port_min=None, src_port_max=None, dst_port_min=None, dst_port_max=None, proto=None, bw=None, delay=None, duration=None, nf_chain=None):  # noqa: E501
        """SfcrSpec - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._source_client = None
        self._destination_client = None
        self._src_ip_prefix = None
        self._dst_ip_prefix = None
        self._src_port_min = None
        self._src_port_max = None
        self._dst_port_min = None
        self._dst_port_max = None
        self._proto = None
        self._bw = None
        self._delay = None
        self._duration = None
        self._nf_chain = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.source_client = source_client
        if destination_client is not None:
            self.destination_client = destination_client
        if src_ip_prefix is not None:
            self.src_ip_prefix = src_ip_prefix
        if dst_ip_prefix is not None:
            self.dst_ip_prefix = dst_ip_prefix
        if src_port_min is not None:
            self.src_port_min = src_port_min
        if src_port_max is not None:
            self.src_port_max = src_port_max
        if dst_port_min is not None:
            self.dst_port_min = dst_port_min
        if dst_port_max is not None:
            self.dst_port_max = dst_port_max
        if proto is not None:
            self.proto = proto
        if bw is not None:
            self.bw = bw
        if delay is not None:
            self.delay = delay
        if duration is not None:
            self.duration = duration
        if nf_chain is not None:
            self.nf_chain = nf_chain

    @property
    def name(self):
        """Gets the name of this SfcrSpec.  # noqa: E501


        :return: The name of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SfcrSpec.


        :param name: The name of this SfcrSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_client(self):
        """Gets the source_client of this SfcrSpec.  # noqa: E501

        the id of the source VM (not Vnf)  # noqa: E501

        :return: The source_client of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._source_client

    @source_client.setter
    def source_client(self, source_client):
        """Sets the source_client of this SfcrSpec.

        the id of the source VM (not Vnf)  # noqa: E501

        :param source_client: The source_client of this SfcrSpec.  # noqa: E501
        :type: str
        """
        if source_client is None:
            raise ValueError("Invalid value for `source_client`, must not be `None`")  # noqa: E501

        self._source_client = source_client

    @property
    def destination_client(self):
        """Gets the destination_client of this SfcrSpec.  # noqa: E501

        the id of the destination VM (not Vnf)  # noqa: E501

        :return: The destination_client of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._destination_client

    @destination_client.setter
    def destination_client(self, destination_client):
        """Sets the destination_client of this SfcrSpec.

        the id of the destination VM (not Vnf)  # noqa: E501

        :param destination_client: The destination_client of this SfcrSpec.  # noqa: E501
        :type: str
        """

        self._destination_client = destination_client

    @property
    def src_ip_prefix(self):
        """Gets the src_ip_prefix of this SfcrSpec.  # noqa: E501


        :return: The src_ip_prefix of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._src_ip_prefix

    @src_ip_prefix.setter
    def src_ip_prefix(self, src_ip_prefix):
        """Sets the src_ip_prefix of this SfcrSpec.


        :param src_ip_prefix: The src_ip_prefix of this SfcrSpec.  # noqa: E501
        :type: str
        """

        self._src_ip_prefix = src_ip_prefix

    @property
    def dst_ip_prefix(self):
        """Gets the dst_ip_prefix of this SfcrSpec.  # noqa: E501


        :return: The dst_ip_prefix of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._dst_ip_prefix

    @dst_ip_prefix.setter
    def dst_ip_prefix(self, dst_ip_prefix):
        """Sets the dst_ip_prefix of this SfcrSpec.


        :param dst_ip_prefix: The dst_ip_prefix of this SfcrSpec.  # noqa: E501
        :type: str
        """

        self._dst_ip_prefix = dst_ip_prefix

    @property
    def src_port_min(self):
        """Gets the src_port_min of this SfcrSpec.  # noqa: E501


        :return: The src_port_min of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._src_port_min

    @src_port_min.setter
    def src_port_min(self, src_port_min):
        """Sets the src_port_min of this SfcrSpec.


        :param src_port_min: The src_port_min of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._src_port_min = src_port_min

    @property
    def src_port_max(self):
        """Gets the src_port_max of this SfcrSpec.  # noqa: E501


        :return: The src_port_max of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._src_port_max

    @src_port_max.setter
    def src_port_max(self, src_port_max):
        """Sets the src_port_max of this SfcrSpec.


        :param src_port_max: The src_port_max of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._src_port_max = src_port_max

    @property
    def dst_port_min(self):
        """Gets the dst_port_min of this SfcrSpec.  # noqa: E501


        :return: The dst_port_min of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._dst_port_min

    @dst_port_min.setter
    def dst_port_min(self, dst_port_min):
        """Sets the dst_port_min of this SfcrSpec.


        :param dst_port_min: The dst_port_min of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._dst_port_min = dst_port_min

    @property
    def dst_port_max(self):
        """Gets the dst_port_max of this SfcrSpec.  # noqa: E501


        :return: The dst_port_max of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._dst_port_max

    @dst_port_max.setter
    def dst_port_max(self, dst_port_max):
        """Sets the dst_port_max of this SfcrSpec.


        :param dst_port_max: The dst_port_max of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._dst_port_max = dst_port_max

    @property
    def proto(self):
        """Gets the proto of this SfcrSpec.  # noqa: E501


        :return: The proto of this SfcrSpec.  # noqa: E501
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this SfcrSpec.


        :param proto: The proto of this SfcrSpec.  # noqa: E501
        :type: str
        """

        self._proto = proto

    @property
    def bw(self):
        """Gets the bw of this SfcrSpec.  # noqa: E501

        bandwidth requirement of the sfcr  # noqa: E501

        :return: The bw of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._bw

    @bw.setter
    def bw(self, bw):
        """Sets the bw of this SfcrSpec.

        bandwidth requirement of the sfcr  # noqa: E501

        :param bw: The bw of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._bw = bw

    @property
    def delay(self):
        """Gets the delay of this SfcrSpec.  # noqa: E501

        delay requirement of the sfcr  # noqa: E501

        :return: The delay of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this SfcrSpec.

        delay requirement of the sfcr  # noqa: E501

        :param delay: The delay of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def duration(self):
        """Gets the duration of this SfcrSpec.  # noqa: E501

        sfcr running duration  # noqa: E501

        :return: The duration of this SfcrSpec.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SfcrSpec.

        sfcr running duration  # noqa: E501

        :param duration: The duration of this SfcrSpec.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def nf_chain(self):
        """Gets the nf_chain of this SfcrSpec.  # noqa: E501

        the type of Vnfs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :return: The nf_chain of this SfcrSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._nf_chain

    @nf_chain.setter
    def nf_chain(self, nf_chain):
        """Sets the nf_chain of this SfcrSpec.

        the type of Vnfs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :param nf_chain: The nf_chain of this SfcrSpec.  # noqa: E501
        :type: list[str]
        """

        self._nf_chain = nf_chain

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
        if issubclass(SfcrSpec, dict):
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
        if not isinstance(other, SfcrSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
