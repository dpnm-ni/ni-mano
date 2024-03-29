# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ni_nfvo.models.base_model_ import Model
from ni_nfvo import util


class VnfSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, flavor_id: str=None, node_name: str=None, vnf_name: str=None, user_data: str=None, image_id: str=None, command: List[str]=None):  # noqa: E501
        """VnfSpec - a model defined in Swagger

        :param flavor_id: The flavor_id of this VnfSpec.  # noqa: E501
        :type flavor_id: str
        :param node_name: The node_name of this VnfSpec.  # noqa: E501
        :type node_name: str
        :param vnf_name: The vnf_name of this VnfSpec.  # noqa: E501
        :type vnf_name: str
        :param user_data: The user_data of this VnfSpec.  # noqa: E501
        :type user_data: str
        :param image_id: The image_id of this VnfSpec.  # noqa: E501
        :type image_id: str
        :param command: The command of this VnfSpec.  # noqa: E501
        :type command: List[str]
        """
        self.swagger_types = {
            'flavor_id': str,
            'node_name': str,
            'vnf_name': str,
            'user_data': str,
            'image_id': str,
            'command': List[str]
        }

        self.attribute_map = {
            'flavor_id': 'flavor_id',
            'node_name': 'node_name',
            'vnf_name': 'vnf_name',
            'user_data': 'user_data',
            'image_id': 'image_id',
            'command': 'command'
        }

        self._flavor_id = flavor_id
        self._node_name = node_name
        self._vnf_name = vnf_name
        self._user_data = user_data
        self._image_id = image_id
        self._command = command

    @classmethod
    def from_dict(cls, dikt) -> 'VnfSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VnfSpec of this VnfSpec.  # noqa: E501
        :rtype: VnfSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flavor_id(self) -> str:
        """Gets the flavor_id of this VnfSpec.

        flavor used to deploy vnf  # noqa: E501

        :return: The flavor_id of this VnfSpec.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id: str):
        """Sets the flavor_id of this VnfSpec.

        flavor used to deploy vnf  # noqa: E501

        :param flavor_id: The flavor_id of this VnfSpec.
        :type flavor_id: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def node_name(self) -> str:
        """Gets the node_name of this VnfSpec.

        name of the compute node where Vnf will be deployed  # noqa: E501

        :return: The node_name of this VnfSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name: str):
        """Sets the node_name of this VnfSpec.

        name of the compute node where Vnf will be deployed  # noqa: E501

        :param node_name: The node_name of this VnfSpec.
        :type node_name: str
        """

        self._node_name = node_name

    @property
    def vnf_name(self) -> str:
        """Gets the vnf_name of this VnfSpec.


        :return: The vnf_name of this VnfSpec.
        :rtype: str
        """
        return self._vnf_name

    @vnf_name.setter
    def vnf_name(self, vnf_name: str):
        """Sets the vnf_name of this VnfSpec.


        :param vnf_name: The vnf_name of this VnfSpec.
        :type vnf_name: str
        """

        self._vnf_name = vnf_name

    @property
    def user_data(self) -> str:
        """Gets the user_data of this VnfSpec.

        [VM only] configuration to pass to the Vnf at boot (e.g., cloud-init)  # noqa: E501

        :return: The user_data of this VnfSpec.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data: str):
        """Sets the user_data of this VnfSpec.

        [VM only] configuration to pass to the Vnf at boot (e.g., cloud-init)  # noqa: E501

        :param user_data: The user_data of this VnfSpec.
        :type user_data: str
        """

        self._user_data = user_data

    @property
    def image_id(self) -> str:
        """Gets the image_id of this VnfSpec.

        if container: put the dockerhub container (e.g., ubuntu:18.04). If VM, put the OS image id. default to ubuntu image id in the config file  # noqa: E501

        :return: The image_id of this VnfSpec.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id: str):
        """Sets the image_id of this VnfSpec.

        if container: put the dockerhub container (e.g., ubuntu:18.04). If VM, put the OS image id. default to ubuntu image id in the config file  # noqa: E501

        :param image_id: The image_id of this VnfSpec.
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def command(self) -> List[str]:
        """Gets the command of this VnfSpec.

        [Container only] Command to run when start the container,e.g., ./script.sh  # noqa: E501

        :return: The command of this VnfSpec.
        :rtype: List[str]
        """
        return self._command

    @command.setter
    def command(self, command: List[str]):
        """Sets the command of this VnfSpec.

        [Container only] Command to run when start the container,e.g., ./script.sh  # noqa: E501

        :param command: The command of this VnfSpec.
        :type command: List[str]
        """

        self._command = command
