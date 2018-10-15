# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Radiusserverpost(object):
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
        'network_source_ip': 'str',
        'name': 'str',
        'tag_names': 'list[str]',
        'shared_secret': 'str'
    }

    attribute_map = {
        'network_source_ip': 'networkSourceIp',
        'name': 'name',
        'tag_names': 'tagNames',
        'shared_secret': 'sharedSecret'
    }

    def __init__(self, network_source_ip=None, name=None, tag_names=None, shared_secret=None):  # noqa: E501
        """Radiusserverpost - a model defined in Swagger"""  # noqa: E501

        self._network_source_ip = None
        self._name = None
        self._tag_names = None
        self._shared_secret = None
        self.discriminator = None

        self.network_source_ip = network_source_ip
        self.name = name
        if tag_names is not None:
            self.tag_names = tag_names
        self.shared_secret = shared_secret

    @property
    def network_source_ip(self):
        """Gets the network_source_ip of this Radiusserverpost.  # noqa: E501


        :return: The network_source_ip of this Radiusserverpost.  # noqa: E501
        :rtype: str
        """
        return self._network_source_ip

    @network_source_ip.setter
    def network_source_ip(self, network_source_ip):
        """Sets the network_source_ip of this Radiusserverpost.


        :param network_source_ip: The network_source_ip of this Radiusserverpost.  # noqa: E501
        :type: str
        """
        if network_source_ip is None:
            raise ValueError("Invalid value for `network_source_ip`, must not be `None`")  # noqa: E501

        self._network_source_ip = network_source_ip

    @property
    def name(self):
        """Gets the name of this Radiusserverpost.  # noqa: E501


        :return: The name of this Radiusserverpost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Radiusserverpost.


        :param name: The name of this Radiusserverpost.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tag_names(self):
        """Gets the tag_names of this Radiusserverpost.  # noqa: E501


        :return: The tag_names of this Radiusserverpost.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this Radiusserverpost.


        :param tag_names: The tag_names of this Radiusserverpost.  # noqa: E501
        :type: list[str]
        """

        self._tag_names = tag_names

    @property
    def shared_secret(self):
        """Gets the shared_secret of this Radiusserverpost.  # noqa: E501

        RADIUS shared secret between the server and client.  # noqa: E501

        :return: The shared_secret of this Radiusserverpost.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this Radiusserverpost.

        RADIUS shared secret between the server and client.  # noqa: E501

        :param shared_secret: The shared_secret of this Radiusserverpost.  # noqa: E501
        :type: str
        """
        if shared_secret is None:
            raise ValueError("Invalid value for `shared_secret`, must not be `None`")  # noqa: E501

        self._shared_secret = shared_secret

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Radiusserverpost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other