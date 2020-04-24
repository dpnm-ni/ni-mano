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


class Body(object):
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
        'flavor_id': 'str',
        'node_name': 'str',
        'vnf_name': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_name': 'node_name',
        'vnf_name': 'vnf_name',
        'user_data': 'user_data'
    }

    def __init__(self, flavor_id=None, node_name=None, vnf_name=None, user_data=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._flavor_id = None
        self._node_name = None
        self._vnf_name = None
        self._user_data = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if node_name is not None:
            self.node_name = node_name
        if vnf_name is not None:
            self.vnf_name = vnf_name
        if user_data is not None:
            self.user_data = user_data

    @property
    def flavor_id(self):
        """Gets the flavor_id of this Body.  # noqa: E501


        :return: The flavor_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this Body.


        :param flavor_id: The flavor_id of this Body.  # noqa: E501
        :type: str
        """

        self._flavor_id = flavor_id

    @property
    def node_name(self):
        """Gets the node_name of this Body.  # noqa: E501


        :return: The node_name of this Body.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this Body.


        :param node_name: The node_name of this Body.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def vnf_name(self):
        """Gets the vnf_name of this Body.  # noqa: E501


        :return: The vnf_name of this Body.  # noqa: E501
        :rtype: str
        """
        return self._vnf_name

    @vnf_name.setter
    def vnf_name(self, vnf_name):
        """Sets the vnf_name of this Body.


        :param vnf_name: The vnf_name of this Body.  # noqa: E501
        :type: str
        """

        self._vnf_name = vnf_name

    @property
    def user_data(self):
        """Gets the user_data of this Body.  # noqa: E501


        :return: The user_data of this Body.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this Body.


        :param user_data: The user_data of this Body.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
