# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_nfvo.models.base_model_ import Model
from ni_nfvo import util


class SFCR(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, arrivaltime: datetime=None, name: str=None, source_client: str=None, destination_client: str=None, src_ip_prefix: str=None, dst_ip_prefix: str=None, src_port_min: int=None, src_port_max: int=None, dst_port_min: int=None, dst_port_max: int=None, proto: str=None, bw: int=None, delay: int=None, duration: int=None, nf_chain: List[str]=None):  # noqa: E501
        """SFCR - a model defined in Swagger

        :param id: The id of this SFCR.  # noqa: E501
        :type id: str
        :param arrivaltime: The arrivaltime of this SFCR.  # noqa: E501
        :type arrivaltime: datetime
        :param name: The name of this SFCR.  # noqa: E501
        :type name: str
        :param source_client: The source_client of this SFCR.  # noqa: E501
        :type source_client: str
        :param destination_client: The destination_client of this SFCR.  # noqa: E501
        :type destination_client: str
        :param src_ip_prefix: The src_ip_prefix of this SFCR.  # noqa: E501
        :type src_ip_prefix: str
        :param dst_ip_prefix: The dst_ip_prefix of this SFCR.  # noqa: E501
        :type dst_ip_prefix: str
        :param src_port_min: The src_port_min of this SFCR.  # noqa: E501
        :type src_port_min: int
        :param src_port_max: The src_port_max of this SFCR.  # noqa: E501
        :type src_port_max: int
        :param dst_port_min: The dst_port_min of this SFCR.  # noqa: E501
        :type dst_port_min: int
        :param dst_port_max: The dst_port_max of this SFCR.  # noqa: E501
        :type dst_port_max: int
        :param proto: The proto of this SFCR.  # noqa: E501
        :type proto: str
        :param bw: The bw of this SFCR.  # noqa: E501
        :type bw: int
        :param delay: The delay of this SFCR.  # noqa: E501
        :type delay: int
        :param duration: The duration of this SFCR.  # noqa: E501
        :type duration: int
        :param nf_chain: The nf_chain of this SFCR.  # noqa: E501
        :type nf_chain: List[str]
        """
        self.swagger_types = {
            'id': str,
            'arrivaltime': datetime,
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
            'id': 'id',
            'arrivaltime': 'arrivaltime',
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

        self._id = id
        self._arrivaltime = arrivaltime
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
    def from_dict(cls, dikt) -> 'SFCR':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SFCR of this SFCR.  # noqa: E501
        :rtype: SFCR
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SFCR.


        :return: The id of this SFCR.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SFCR.


        :param id: The id of this SFCR.
        :type id: str
        """

        self._id = id

    @property
    def arrivaltime(self) -> datetime:
        """Gets the arrivaltime of this SFCR.


        :return: The arrivaltime of this SFCR.
        :rtype: datetime
        """
        return self._arrivaltime

    @arrivaltime.setter
    def arrivaltime(self, arrivaltime: datetime):
        """Sets the arrivaltime of this SFCR.


        :param arrivaltime: The arrivaltime of this SFCR.
        :type arrivaltime: datetime
        """

        self._arrivaltime = arrivaltime

    @property
    def name(self) -> str:
        """Gets the name of this SFCR.


        :return: The name of this SFCR.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SFCR.


        :param name: The name of this SFCR.
        :type name: str
        """

        self._name = name

    @property
    def source_client(self) -> str:
        """Gets the source_client of this SFCR.

        the id of the source VM (not VNF)  # noqa: E501

        :return: The source_client of this SFCR.
        :rtype: str
        """
        return self._source_client

    @source_client.setter
    def source_client(self, source_client: str):
        """Sets the source_client of this SFCR.

        the id of the source VM (not VNF)  # noqa: E501

        :param source_client: The source_client of this SFCR.
        :type source_client: str
        """

        self._source_client = source_client

    @property
    def destination_client(self) -> str:
        """Gets the destination_client of this SFCR.

        the id of the destination VM (not VNF)  # noqa: E501

        :return: The destination_client of this SFCR.
        :rtype: str
        """
        return self._destination_client

    @destination_client.setter
    def destination_client(self, destination_client: str):
        """Sets the destination_client of this SFCR.

        the id of the destination VM (not VNF)  # noqa: E501

        :param destination_client: The destination_client of this SFCR.
        :type destination_client: str
        """

        self._destination_client = destination_client

    @property
    def src_ip_prefix(self) -> str:
        """Gets the src_ip_prefix of this SFCR.


        :return: The src_ip_prefix of this SFCR.
        :rtype: str
        """
        return self._src_ip_prefix

    @src_ip_prefix.setter
    def src_ip_prefix(self, src_ip_prefix: str):
        """Sets the src_ip_prefix of this SFCR.


        :param src_ip_prefix: The src_ip_prefix of this SFCR.
        :type src_ip_prefix: str
        """

        self._src_ip_prefix = src_ip_prefix

    @property
    def dst_ip_prefix(self) -> str:
        """Gets the dst_ip_prefix of this SFCR.


        :return: The dst_ip_prefix of this SFCR.
        :rtype: str
        """
        return self._dst_ip_prefix

    @dst_ip_prefix.setter
    def dst_ip_prefix(self, dst_ip_prefix: str):
        """Sets the dst_ip_prefix of this SFCR.


        :param dst_ip_prefix: The dst_ip_prefix of this SFCR.
        :type dst_ip_prefix: str
        """

        self._dst_ip_prefix = dst_ip_prefix

    @property
    def src_port_min(self) -> int:
        """Gets the src_port_min of this SFCR.


        :return: The src_port_min of this SFCR.
        :rtype: int
        """
        return self._src_port_min

    @src_port_min.setter
    def src_port_min(self, src_port_min: int):
        """Sets the src_port_min of this SFCR.


        :param src_port_min: The src_port_min of this SFCR.
        :type src_port_min: int
        """

        self._src_port_min = src_port_min

    @property
    def src_port_max(self) -> int:
        """Gets the src_port_max of this SFCR.


        :return: The src_port_max of this SFCR.
        :rtype: int
        """
        return self._src_port_max

    @src_port_max.setter
    def src_port_max(self, src_port_max: int):
        """Sets the src_port_max of this SFCR.


        :param src_port_max: The src_port_max of this SFCR.
        :type src_port_max: int
        """

        self._src_port_max = src_port_max

    @property
    def dst_port_min(self) -> int:
        """Gets the dst_port_min of this SFCR.


        :return: The dst_port_min of this SFCR.
        :rtype: int
        """
        return self._dst_port_min

    @dst_port_min.setter
    def dst_port_min(self, dst_port_min: int):
        """Sets the dst_port_min of this SFCR.


        :param dst_port_min: The dst_port_min of this SFCR.
        :type dst_port_min: int
        """

        self._dst_port_min = dst_port_min

    @property
    def dst_port_max(self) -> int:
        """Gets the dst_port_max of this SFCR.


        :return: The dst_port_max of this SFCR.
        :rtype: int
        """
        return self._dst_port_max

    @dst_port_max.setter
    def dst_port_max(self, dst_port_max: int):
        """Sets the dst_port_max of this SFCR.


        :param dst_port_max: The dst_port_max of this SFCR.
        :type dst_port_max: int
        """

        self._dst_port_max = dst_port_max

    @property
    def proto(self) -> str:
        """Gets the proto of this SFCR.


        :return: The proto of this SFCR.
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto: str):
        """Sets the proto of this SFCR.


        :param proto: The proto of this SFCR.
        :type proto: str
        """

        self._proto = proto

    @property
    def bw(self) -> int:
        """Gets the bw of this SFCR.

        bandwidth requirement of the sfcr  # noqa: E501

        :return: The bw of this SFCR.
        :rtype: int
        """
        return self._bw

    @bw.setter
    def bw(self, bw: int):
        """Sets the bw of this SFCR.

        bandwidth requirement of the sfcr  # noqa: E501

        :param bw: The bw of this SFCR.
        :type bw: int
        """

        self._bw = bw

    @property
    def delay(self) -> int:
        """Gets the delay of this SFCR.

        delay requirement of the sfcr  # noqa: E501

        :return: The delay of this SFCR.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay: int):
        """Sets the delay of this SFCR.

        delay requirement of the sfcr  # noqa: E501

        :param delay: The delay of this SFCR.
        :type delay: int
        """

        self._delay = delay

    @property
    def duration(self) -> int:
        """Gets the duration of this SFCR.

        sfcr running duration  # noqa: E501

        :return: The duration of this SFCR.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this SFCR.

        sfcr running duration  # noqa: E501

        :param duration: The duration of this SFCR.
        :type duration: int
        """

        self._duration = duration

    @property
    def nf_chain(self) -> List[str]:
        """Gets the nf_chain of this SFCR.

        the type of VNFs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :return: The nf_chain of this SFCR.
        :rtype: List[str]
        """
        return self._nf_chain

    @nf_chain.setter
    def nf_chain(self, nf_chain: List[str]):
        """Sets the nf_chain of this SFCR.

        the type of VNFs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :param nf_chain: The nf_chain of this SFCR.
        :type nf_chain: List[str]
        """

        self._nf_chain = nf_chain
