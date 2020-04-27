# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_nfvo.models.base_model_ import Model
from ni_nfvo import util


class SFCRSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, source_client: str=None, destination_client: str=None, src_ip_prefix: str=None, dst_ip_prefix: str=None, src_port_min: int=None, src_port_max: int=None, dst_port_min: int=None, dst_port_max: int=None, proto: str=None, bw: int=None, delay: int=None, duration: int=None, nf_chain: List[str]=None):  # noqa: E501
        """SFCRSpec - a model defined in Swagger

        :param name: The name of this SFCRSpec.  # noqa: E501
        :type name: str
        :param source_client: The source_client of this SFCRSpec.  # noqa: E501
        :type source_client: str
        :param destination_client: The destination_client of this SFCRSpec.  # noqa: E501
        :type destination_client: str
        :param src_ip_prefix: The src_ip_prefix of this SFCRSpec.  # noqa: E501
        :type src_ip_prefix: str
        :param dst_ip_prefix: The dst_ip_prefix of this SFCRSpec.  # noqa: E501
        :type dst_ip_prefix: str
        :param src_port_min: The src_port_min of this SFCRSpec.  # noqa: E501
        :type src_port_min: int
        :param src_port_max: The src_port_max of this SFCRSpec.  # noqa: E501
        :type src_port_max: int
        :param dst_port_min: The dst_port_min of this SFCRSpec.  # noqa: E501
        :type dst_port_min: int
        :param dst_port_max: The dst_port_max of this SFCRSpec.  # noqa: E501
        :type dst_port_max: int
        :param proto: The proto of this SFCRSpec.  # noqa: E501
        :type proto: str
        :param bw: The bw of this SFCRSpec.  # noqa: E501
        :type bw: int
        :param delay: The delay of this SFCRSpec.  # noqa: E501
        :type delay: int
        :param duration: The duration of this SFCRSpec.  # noqa: E501
        :type duration: int
        :param nf_chain: The nf_chain of this SFCRSpec.  # noqa: E501
        :type nf_chain: List[str]
        """
        self.swagger_types = {
            'name': str,
            'source_client': str,
            'destination_client': str,
            'src_ip_prefix': str,
            'dst_ip_prefix': str,
            'src_port_min': int,
            'src_port_max': int,
            'dst_port_min': int,
            'dst_port_max': int,
            'proto': str,
            'bw': int,
            'delay': int,
            'duration': int,
            'nf_chain': List[str]
        }

        self.attribute_map = {
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

        self._name = name
        self._source_client = source_client
        self._destination_client = destination_client
        self._src_ip_prefix = src_ip_prefix
        self._dst_ip_prefix = dst_ip_prefix
        self._src_port_min = src_port_min
        self._src_port_max = src_port_max
        self._dst_port_min = dst_port_min
        self._dst_port_max = dst_port_max
        self._proto = proto
        self._bw = bw
        self._delay = delay
        self._duration = duration
        self._nf_chain = nf_chain

    @classmethod
    def from_dict(cls, dikt) -> 'SFCRSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SFCRSpec of this SFCRSpec.  # noqa: E501
        :rtype: SFCRSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this SFCRSpec.


        :return: The name of this SFCRSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SFCRSpec.


        :param name: The name of this SFCRSpec.
        :type name: str
        """

        self._name = name

    @property
    def source_client(self) -> str:
        """Gets the source_client of this SFCRSpec.

        the id of the source VM (not VNF)  # noqa: E501

        :return: The source_client of this SFCRSpec.
        :rtype: str
        """
        return self._source_client

    @source_client.setter
    def source_client(self, source_client: str):
        """Sets the source_client of this SFCRSpec.

        the id of the source VM (not VNF)  # noqa: E501

        :param source_client: The source_client of this SFCRSpec.
        :type source_client: str
        """
        if source_client is None:
            raise ValueError("Invalid value for `source_client`, must not be `None`")  # noqa: E501

        self._source_client = source_client

    @property
    def destination_client(self) -> str:
        """Gets the destination_client of this SFCRSpec.

        the id of the destination VM (not VNF)  # noqa: E501

        :return: The destination_client of this SFCRSpec.
        :rtype: str
        """
        return self._destination_client

    @destination_client.setter
    def destination_client(self, destination_client: str):
        """Sets the destination_client of this SFCRSpec.

        the id of the destination VM (not VNF)  # noqa: E501

        :param destination_client: The destination_client of this SFCRSpec.
        :type destination_client: str
        """

        self._destination_client = destination_client

    @property
    def src_ip_prefix(self) -> str:
        """Gets the src_ip_prefix of this SFCRSpec.


        :return: The src_ip_prefix of this SFCRSpec.
        :rtype: str
        """
        return self._src_ip_prefix

    @src_ip_prefix.setter
    def src_ip_prefix(self, src_ip_prefix: str):
        """Sets the src_ip_prefix of this SFCRSpec.


        :param src_ip_prefix: The src_ip_prefix of this SFCRSpec.
        :type src_ip_prefix: str
        """

        self._src_ip_prefix = src_ip_prefix

    @property
    def dst_ip_prefix(self) -> str:
        """Gets the dst_ip_prefix of this SFCRSpec.


        :return: The dst_ip_prefix of this SFCRSpec.
        :rtype: str
        """
        return self._dst_ip_prefix

    @dst_ip_prefix.setter
    def dst_ip_prefix(self, dst_ip_prefix: str):
        """Sets the dst_ip_prefix of this SFCRSpec.


        :param dst_ip_prefix: The dst_ip_prefix of this SFCRSpec.
        :type dst_ip_prefix: str
        """

        self._dst_ip_prefix = dst_ip_prefix

    @property
    def src_port_min(self) -> int:
        """Gets the src_port_min of this SFCRSpec.


        :return: The src_port_min of this SFCRSpec.
        :rtype: int
        """
        return self._src_port_min

    @src_port_min.setter
    def src_port_min(self, src_port_min: int):
        """Sets the src_port_min of this SFCRSpec.


        :param src_port_min: The src_port_min of this SFCRSpec.
        :type src_port_min: int
        """

        self._src_port_min = src_port_min

    @property
    def src_port_max(self) -> int:
        """Gets the src_port_max of this SFCRSpec.


        :return: The src_port_max of this SFCRSpec.
        :rtype: int
        """
        return self._src_port_max

    @src_port_max.setter
    def src_port_max(self, src_port_max: int):
        """Sets the src_port_max of this SFCRSpec.


        :param src_port_max: The src_port_max of this SFCRSpec.
        :type src_port_max: int
        """

        self._src_port_max = src_port_max

    @property
    def dst_port_min(self) -> int:
        """Gets the dst_port_min of this SFCRSpec.


        :return: The dst_port_min of this SFCRSpec.
        :rtype: int
        """
        return self._dst_port_min

    @dst_port_min.setter
    def dst_port_min(self, dst_port_min: int):
        """Sets the dst_port_min of this SFCRSpec.


        :param dst_port_min: The dst_port_min of this SFCRSpec.
        :type dst_port_min: int
        """

        self._dst_port_min = dst_port_min

    @property
    def dst_port_max(self) -> int:
        """Gets the dst_port_max of this SFCRSpec.


        :return: The dst_port_max of this SFCRSpec.
        :rtype: int
        """
        return self._dst_port_max

    @dst_port_max.setter
    def dst_port_max(self, dst_port_max: int):
        """Sets the dst_port_max of this SFCRSpec.


        :param dst_port_max: The dst_port_max of this SFCRSpec.
        :type dst_port_max: int
        """

        self._dst_port_max = dst_port_max

    @property
    def proto(self) -> str:
        """Gets the proto of this SFCRSpec.


        :return: The proto of this SFCRSpec.
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto: str):
        """Sets the proto of this SFCRSpec.


        :param proto: The proto of this SFCRSpec.
        :type proto: str
        """

        self._proto = proto

    @property
    def bw(self) -> int:
        """Gets the bw of this SFCRSpec.

        bandwidth requirement of the sfcr  # noqa: E501

        :return: The bw of this SFCRSpec.
        :rtype: int
        """
        return self._bw

    @bw.setter
    def bw(self, bw: int):
        """Sets the bw of this SFCRSpec.

        bandwidth requirement of the sfcr  # noqa: E501

        :param bw: The bw of this SFCRSpec.
        :type bw: int
        """

        self._bw = bw

    @property
    def delay(self) -> int:
        """Gets the delay of this SFCRSpec.

        delay requirement of the sfcr  # noqa: E501

        :return: The delay of this SFCRSpec.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay: int):
        """Sets the delay of this SFCRSpec.

        delay requirement of the sfcr  # noqa: E501

        :param delay: The delay of this SFCRSpec.
        :type delay: int
        """

        self._delay = delay

    @property
    def duration(self) -> int:
        """Gets the duration of this SFCRSpec.

        sfcr running duration  # noqa: E501

        :return: The duration of this SFCRSpec.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this SFCRSpec.

        sfcr running duration  # noqa: E501

        :param duration: The duration of this SFCRSpec.
        :type duration: int
        """

        self._duration = duration

    @property
    def nf_chain(self) -> List[str]:
        """Gets the nf_chain of this SFCRSpec.

        the type of VNFs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :return: The nf_chain of this SFCRSpec.
        :rtype: List[str]
        """
        return self._nf_chain

    @nf_chain.setter
    def nf_chain(self, nf_chain: List[str]):
        """Sets the nf_chain of this SFCRSpec.

        the type of VNFs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :param nf_chain: The nf_chain of this SFCRSpec.
        :type nf_chain: List[str]
        """

        self._nf_chain = nf_chain
