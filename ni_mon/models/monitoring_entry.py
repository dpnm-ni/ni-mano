# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_mon.models.base_model_ import Model
from ni_mon import util


class MonitoringEntry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, timestamp: datetime=None, component_type: str=None, component_id: str=None, measurement_type: str=None, measurement_value: float=None):  # noqa: E501
        """MonitoringEntry - a model defined in Swagger

        :param timestamp: The timestamp of this MonitoringEntry.  # noqa: E501
        :type timestamp: datetime
        :param component_type: The component_type of this MonitoringEntry.  # noqa: E501
        :type component_type: str
        :param component_id: The component_id of this MonitoringEntry.  # noqa: E501
        :type component_id: str
        :param measurement_type: The measurement_type of this MonitoringEntry.  # noqa: E501
        :type measurement_type: str
        :param measurement_value: The measurement_value of this MonitoringEntry.  # noqa: E501
        :type measurement_value: float
        """
        self.swagger_types = {
            'timestamp': datetime,
            'component_type': str,
            'component_id': str,
            'measurement_type': str,
            'measurement_value': float
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'component_type': 'component_type',
            'component_id': 'component_id',
            'measurement_type': 'measurement_type',
            'measurement_value': 'measurement_value'
        }

        self._timestamp = timestamp
        self._component_type = component_type
        self._component_id = component_id
        self._measurement_type = measurement_type
        self._measurement_value = measurement_value

    @classmethod
    def from_dict(cls, dikt) -> 'MonitoringEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MonitoringEntry of this MonitoringEntry.  # noqa: E501
        :rtype: MonitoringEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this MonitoringEntry.


        :return: The timestamp of this MonitoringEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this MonitoringEntry.


        :param timestamp: The timestamp of this MonitoringEntry.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def component_type(self) -> str:
        """Gets the component_type of this MonitoringEntry.

        unused for now  # noqa: E501

        :return: The component_type of this MonitoringEntry.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type: str):
        """Sets the component_type of this MonitoringEntry.

        unused for now  # noqa: E501

        :param component_type: The component_type of this MonitoringEntry.
        :type component_type: str
        """

        self._component_type = component_type

    @property
    def component_id(self) -> str:
        """Gets the component_id of this MonitoringEntry.

        the id of the VNF instance or compute node  # noqa: E501

        :return: The component_id of this MonitoringEntry.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id: str):
        """Sets the component_id of this MonitoringEntry.

        the id of the VNF instance or compute node  # noqa: E501

        :param component_id: The component_id of this MonitoringEntry.
        :type component_id: str
        """

        self._component_id = component_id

    @property
    def measurement_type(self) -> str:
        """Gets the measurement_type of this MonitoringEntry.


        :return: The measurement_type of this MonitoringEntry.
        :rtype: str
        """
        return self._measurement_type

    @measurement_type.setter
    def measurement_type(self, measurement_type: str):
        """Sets the measurement_type of this MonitoringEntry.


        :param measurement_type: The measurement_type of this MonitoringEntry.
        :type measurement_type: str
        """

        self._measurement_type = measurement_type

    @property
    def measurement_value(self) -> float:
        """Gets the measurement_value of this MonitoringEntry.


        :return: The measurement_value of this MonitoringEntry.
        :rtype: float
        """
        return self._measurement_value

    @measurement_value.setter
    def measurement_value(self, measurement_value: float):
        """Sets the measurement_value of this MonitoringEntry.


        :param measurement_value: The measurement_value of this MonitoringEntry.
        :type measurement_value: float
        """

        self._measurement_value = measurement_value
