# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_nfvo.models.base_model_ import Model
from ni_nfvo import util


class Sfcr(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, arrivaltime: datetime=None, name: str=None, source_client: str=None, destination_client: str=None, src_ip_prefix: str=None, dst_ip_prefix: str=None, src_port_min: int=None, src_port_max: int=None, dst_port_min: int=None, dst_port_max: int=None, proto: str=None, bw: int=None, delay: int=None, duration: int=None, nf_chain: List[str]=None):  # noqa: E501
        """Sfcr - a model defined in Swagger

        :param id: The id of this Sfcr.  # noqa: E501
        :type id: str
        :param arrivaltime: The arrivaltime of this Sfcr.  # noqa: E501
        :type arrivaltime: datetime
        :param name: The name of this Sfcr.  # noqa: E501
        :type name: str
        :param source_client: The source_client of this Sfcr.  # noqa: E501
        :type source_client: str
        :param destination_client: The destination_client of this Sfcr.  # noqa: E501
        :type destination_client: str
        :param src_ip_prefix: The src_ip_prefix of this Sfcr.  # noqa: E501
        :type src_ip_prefix: str
        :param dst_ip_prefix: The dst_ip_prefix of this Sfcr.  # noqa: E501
        :type dst_ip_prefix: str
        :param src_port_min: The src_port_min of this Sfcr.  # noqa: E501
        :type src_port_min: int
        :param src_port_max: The src_port_max of this Sfcr.  # noqa: E501
        :type src_port_max: int
        :param dst_port_min: The dst_port_min of this Sfcr.  # noqa: E501
        :type dst_port_min: int
        :param dst_port_max: The dst_port_max of this Sfcr.  # noqa: E501
        :type dst_port_max: int
        :param proto: The proto of this Sfcr.  # noqa: E501
        :type proto: str
        :param bw: The bw of this Sfcr.  # noqa: E501
        :type bw: int
        :param delay: The delay of this Sfcr.  # noqa: E501
        :type delay: int
        :param duration: The duration of this Sfcr.  # noqa: E501
        :type duration: int
        :param nf_chain: The nf_chain of this Sfcr.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'Sfcr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Sfcr of this Sfcr.  # noqa: E501
        :rtype: Sfcr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Sfcr.


        :return: The id of this Sfcr.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Sfcr.


        :param id: The id of this Sfcr.
        :type id: str
        """

        self._id = id

    @property
    def arrivaltime(self) -> datetime:
        """Gets the arrivaltime of this Sfcr.


        :return: The arrivaltime of this Sfcr.
        :rtype: datetime
        """
        return self._arrivaltime

    @arrivaltime.setter
    def arrivaltime(self, arrivaltime: datetime):
        """Sets the arrivaltime of this Sfcr.


        :param arrivaltime: The arrivaltime of this Sfcr.
        :type arrivaltime: datetime
        """

        self._arrivaltime = arrivaltime

    @property
    def name(self) -> str:
        """Gets the name of this Sfcr.


        :return: The name of this Sfcr.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Sfcr.


        :param name: The name of this Sfcr.
        :type name: str
        """

        self._name = name

    @property
    def source_client(self) -> str:
        """Gets the source_client of this Sfcr.

        the id of the source VM/container (not Vnf)  # noqa: E501

        :return: The source_client of this Sfcr.
        :rtype: str
        """
        return self._source_client

    @source_client.setter
    def source_client(self, source_client: str):
        """Sets the source_client of this Sfcr.

        the id of the source VM/container (not Vnf)  # noqa: E501

        :param source_client: The source_client of this Sfcr.
        :type source_client: str
        """

        self._source_client = source_client

    @property
    def destination_client(self) -> str:
        """Gets the destination_client of this Sfcr.

        the id of the destination VM/container (not Vnf)  # noqa: E501

        :return: The destination_client of this Sfcr.
        :rtype: str
        """
        return self._destination_client

    @destination_client.setter
    def destination_client(self, destination_client: str):
        """Sets the destination_client of this Sfcr.

        the id of the destination VM/container (not Vnf)  # noqa: E501

        :param destination_client: The destination_client of this Sfcr.
        :type destination_client: str
        """

        self._destination_client = destination_client

    @property
    def src_ip_prefix(self) -> str:
        """Gets the src_ip_prefix of this Sfcr.


        :return: The src_ip_prefix of this Sfcr.
        :rtype: str
        """
        return self._src_ip_prefix

    @src_ip_prefix.setter
    def src_ip_prefix(self, src_ip_prefix: str):
        """Sets the src_ip_prefix of this Sfcr.


        :param src_ip_prefix: The src_ip_prefix of this Sfcr.
        :type src_ip_prefix: str
        """

        self._src_ip_prefix = src_ip_prefix

    @property
    def dst_ip_prefix(self) -> str:
        """Gets the dst_ip_prefix of this Sfcr.


        :return: The dst_ip_prefix of this Sfcr.
        :rtype: str
        """
        return self._dst_ip_prefix

    @dst_ip_prefix.setter
    def dst_ip_prefix(self, dst_ip_prefix: str):
        """Sets the dst_ip_prefix of this Sfcr.


        :param dst_ip_prefix: The dst_ip_prefix of this Sfcr.
        :type dst_ip_prefix: str
        """

        self._dst_ip_prefix = dst_ip_prefix

    @property
    def src_port_min(self) -> int:
        """Gets the src_port_min of this Sfcr.


        :return: The src_port_min of this Sfcr.
        :rtype: int
        """
        return self._src_port_min

    @src_port_min.setter
    def src_port_min(self, src_port_min: int):
        """Sets the src_port_min of this Sfcr.


        :param src_port_min: The src_port_min of this Sfcr.
        :type src_port_min: int
        """

        self._src_port_min = src_port_min

    @property
    def src_port_max(self) -> int:
        """Gets the src_port_max of this Sfcr.


        :return: The src_port_max of this Sfcr.
        :rtype: int
        """
        return self._src_port_max

    @src_port_max.setter
    def src_port_max(self, src_port_max: int):
        """Sets the src_port_max of this Sfcr.


        :param src_port_max: The src_port_max of this Sfcr.
        :type src_port_max: int
        """

        self._src_port_max = src_port_max

    @property
    def dst_port_min(self) -> int:
        """Gets the dst_port_min of this Sfcr.


        :return: The dst_port_min of this Sfcr.
        :rtype: int
        """
        return self._dst_port_min

    @dst_port_min.setter
    def dst_port_min(self, dst_port_min: int):
        """Sets the dst_port_min of this Sfcr.


        :param dst_port_min: The dst_port_min of this Sfcr.
        :type dst_port_min: int
        """

        self._dst_port_min = dst_port_min

    @property
    def dst_port_max(self) -> int:
        """Gets the dst_port_max of this Sfcr.


        :return: The dst_port_max of this Sfcr.
        :rtype: int
        """
        return self._dst_port_max

    @dst_port_max.setter
    def dst_port_max(self, dst_port_max: int):
        """Sets the dst_port_max of this Sfcr.


        :param dst_port_max: The dst_port_max of this Sfcr.
        :type dst_port_max: int
        """

        self._dst_port_max = dst_port_max

    @property
    def proto(self) -> str:
        """Gets the proto of this Sfcr.


        :return: The proto of this Sfcr.
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto: str):
        """Sets the proto of this Sfcr.


        :param proto: The proto of this Sfcr.
        :type proto: str
        """

        self._proto = proto

    @property
    def bw(self) -> int:
        """Gets the bw of this Sfcr.

        bandwidth requirement of the sfcr  # noqa: E501

        :return: The bw of this Sfcr.
        :rtype: int
        """
        return self._bw

    @bw.setter
    def bw(self, bw: int):
        """Sets the bw of this Sfcr.

        bandwidth requirement of the sfcr  # noqa: E501

        :param bw: The bw of this Sfcr.
        :type bw: int
        """

        self._bw = bw

    @property
    def delay(self) -> int:
        """Gets the delay of this Sfcr.

        delay requirement of the sfcr  # noqa: E501

        :return: The delay of this Sfcr.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay: int):
        """Sets the delay of this Sfcr.

        delay requirement of the sfcr  # noqa: E501

        :param delay: The delay of this Sfcr.
        :type delay: int
        """

        self._delay = delay

    @property
    def duration(self) -> int:
        """Gets the duration of this Sfcr.

        sfcr running duration  # noqa: E501

        :return: The duration of this Sfcr.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this Sfcr.

        sfcr running duration  # noqa: E501

        :param duration: The duration of this Sfcr.
        :type duration: int
        """

        self._duration = duration

    @property
    def nf_chain(self) -> List[str]:
        """Gets the nf_chain of this Sfcr.

        the type of Vnfs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :return: The nf_chain of this Sfcr.
        :rtype: List[str]
        """
        return self._nf_chain

    @nf_chain.setter
    def nf_chain(self, nf_chain: List[str]):
        """Sets the nf_chain of this Sfcr.

        the type of Vnfs in the path (e.g.: fw, ids, nat, etc.).  # noqa: E501

        :param nf_chain: The nf_chain of this Sfcr.
        :type nf_chain: List[str]
        """

        self._nf_chain = nf_chain
