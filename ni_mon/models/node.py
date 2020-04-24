# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_mon.models.base_model_ import Model
from ni_mon import util


class Node(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, type: str=None, ip: str=None, n_cores: int=None, core_freq_mhz: int=None, ram_mb: int=None, ram_freq_mhz: int=None):  # noqa: E501
        """Node - a model defined in Swagger

        :param id: The id of this Node.  # noqa: E501
        :type id: str
        :param name: The name of this Node.  # noqa: E501
        :type name: str
        :param type: The type of this Node.  # noqa: E501
        :type type: str
        :param ip: The ip of this Node.  # noqa: E501
        :type ip: str
        :param n_cores: The n_cores of this Node.  # noqa: E501
        :type n_cores: int
        :param core_freq_mhz: The core_freq_mhz of this Node.  # noqa: E501
        :type core_freq_mhz: int
        :param ram_mb: The ram_mb of this Node.  # noqa: E501
        :type ram_mb: int
        :param ram_freq_mhz: The ram_freq_mhz of this Node.  # noqa: E501
        :type ram_freq_mhz: int
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'type': str,
            'ip': str,
            'n_cores': int,
            'core_freq_mhz': int,
            'ram_mb': int,
            'ram_freq_mhz': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'ip': 'ip',
            'n_cores': 'n_cores',
            'core_freq_mhz': 'core_freq_mhz',
            'ram_mb': 'ram_mb',
            'ram_freq_mhz': 'ram_freq_mhz'
        }

        self._id = id
        self._name = name
        self._type = type
        self._ip = ip
        self._n_cores = n_cores
        self._core_freq_mhz = core_freq_mhz
        self._ram_mb = ram_mb
        self._ram_freq_mhz = ram_freq_mhz

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Node of this Node.  # noqa: E501
        :rtype: Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Node.


        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Node.


        :param id: The id of this Node.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Node.


        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Node.


        :param name: The name of this Node.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Node.


        :return: The type of this Node.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Node.


        :param type: The type of this Node.
        :type type: str
        """

        self._type = type

    @property
    def ip(self) -> str:
        """Gets the ip of this Node.


        :return: The ip of this Node.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this Node.


        :param ip: The ip of this Node.
        :type ip: str
        """

        self._ip = ip

    @property
    def n_cores(self) -> int:
        """Gets the n_cores of this Node.


        :return: The n_cores of this Node.
        :rtype: int
        """
        return self._n_cores

    @n_cores.setter
    def n_cores(self, n_cores: int):
        """Sets the n_cores of this Node.


        :param n_cores: The n_cores of this Node.
        :type n_cores: int
        """

        self._n_cores = n_cores

    @property
    def core_freq_mhz(self) -> int:
        """Gets the core_freq_mhz of this Node.


        :return: The core_freq_mhz of this Node.
        :rtype: int
        """
        return self._core_freq_mhz

    @core_freq_mhz.setter
    def core_freq_mhz(self, core_freq_mhz: int):
        """Sets the core_freq_mhz of this Node.


        :param core_freq_mhz: The core_freq_mhz of this Node.
        :type core_freq_mhz: int
        """

        self._core_freq_mhz = core_freq_mhz

    @property
    def ram_mb(self) -> int:
        """Gets the ram_mb of this Node.


        :return: The ram_mb of this Node.
        :rtype: int
        """
        return self._ram_mb

    @ram_mb.setter
    def ram_mb(self, ram_mb: int):
        """Sets the ram_mb of this Node.


        :param ram_mb: The ram_mb of this Node.
        :type ram_mb: int
        """

        self._ram_mb = ram_mb

    @property
    def ram_freq_mhz(self) -> int:
        """Gets the ram_freq_mhz of this Node.


        :return: The ram_freq_mhz of this Node.
        :rtype: int
        """
        return self._ram_freq_mhz

    @ram_freq_mhz.setter
    def ram_freq_mhz(self, ram_freq_mhz: int):
        """Sets the ram_freq_mhz of this Node.


        :param ram_freq_mhz: The ram_freq_mhz of this Node.
        :type ram_freq_mhz: int
        """

        self._ram_freq_mhz = ram_freq_mhz
