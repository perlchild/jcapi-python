# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApplicationConfigConstantAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'label': 'str',
        'read_only': 'bool',
        'tooltip': 'ApplicationConfigIdpEntityIdTooltip',
        'type': 'str',
        'value': 'list[ApplicationConfigConstantAttributesValue]',
        'visible': 'bool',
        'mutable': 'bool',
        'required': 'bool',
        'position': 'int'
    }

    attribute_map = {
        'label': 'label',
        'read_only': 'readOnly',
        'tooltip': 'tooltip',
        'type': 'type',
        'value': 'value',
        'visible': 'visible',
        'mutable': 'mutable',
        'required': 'required',
        'position': 'position'
    }

    def __init__(self, label=None, read_only=None, tooltip=None, type=None, value=None, visible=None, mutable=None, required=None, position=None):
        """
        ApplicationConfigConstantAttributes - a model defined in Swagger
        """

        self._label = None
        self._read_only = None
        self._tooltip = None
        self._type = None
        self._value = None
        self._visible = None
        self._mutable = None
        self._required = None
        self._position = None

        if label is not None:
          self.label = label
        if read_only is not None:
          self.read_only = read_only
        if tooltip is not None:
          self.tooltip = tooltip
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value
        if visible is not None:
          self.visible = visible
        if mutable is not None:
          self.mutable = mutable
        if required is not None:
          self.required = required
        if position is not None:
          self.position = position

    @property
    def label(self):
        """
        Gets the label of this ApplicationConfigConstantAttributes.

        :return: The label of this ApplicationConfigConstantAttributes.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ApplicationConfigConstantAttributes.

        :param label: The label of this ApplicationConfigConstantAttributes.
        :type: str
        """

        self._label = label

    @property
    def read_only(self):
        """
        Gets the read_only of this ApplicationConfigConstantAttributes.

        :return: The read_only of this ApplicationConfigConstantAttributes.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this ApplicationConfigConstantAttributes.

        :param read_only: The read_only of this ApplicationConfigConstantAttributes.
        :type: bool
        """

        self._read_only = read_only

    @property
    def tooltip(self):
        """
        Gets the tooltip of this ApplicationConfigConstantAttributes.

        :return: The tooltip of this ApplicationConfigConstantAttributes.
        :rtype: ApplicationConfigIdpEntityIdTooltip
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """
        Sets the tooltip of this ApplicationConfigConstantAttributes.

        :param tooltip: The tooltip of this ApplicationConfigConstantAttributes.
        :type: ApplicationConfigIdpEntityIdTooltip
        """

        self._tooltip = tooltip

    @property
    def type(self):
        """
        Gets the type of this ApplicationConfigConstantAttributes.

        :return: The type of this ApplicationConfigConstantAttributes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApplicationConfigConstantAttributes.

        :param type: The type of this ApplicationConfigConstantAttributes.
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this ApplicationConfigConstantAttributes.

        :return: The value of this ApplicationConfigConstantAttributes.
        :rtype: list[ApplicationConfigConstantAttributesValue]
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ApplicationConfigConstantAttributes.

        :param value: The value of this ApplicationConfigConstantAttributes.
        :type: list[ApplicationConfigConstantAttributesValue]
        """

        self._value = value

    @property
    def visible(self):
        """
        Gets the visible of this ApplicationConfigConstantAttributes.

        :return: The visible of this ApplicationConfigConstantAttributes.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this ApplicationConfigConstantAttributes.

        :param visible: The visible of this ApplicationConfigConstantAttributes.
        :type: bool
        """

        self._visible = visible

    @property
    def mutable(self):
        """
        Gets the mutable of this ApplicationConfigConstantAttributes.

        :return: The mutable of this ApplicationConfigConstantAttributes.
        :rtype: bool
        """
        return self._mutable

    @mutable.setter
    def mutable(self, mutable):
        """
        Sets the mutable of this ApplicationConfigConstantAttributes.

        :param mutable: The mutable of this ApplicationConfigConstantAttributes.
        :type: bool
        """

        self._mutable = mutable

    @property
    def required(self):
        """
        Gets the required of this ApplicationConfigConstantAttributes.

        :return: The required of this ApplicationConfigConstantAttributes.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ApplicationConfigConstantAttributes.

        :param required: The required of this ApplicationConfigConstantAttributes.
        :type: bool
        """

        self._required = required

    @property
    def position(self):
        """
        Gets the position of this ApplicationConfigConstantAttributes.

        :return: The position of this ApplicationConfigConstantAttributes.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ApplicationConfigConstantAttributes.

        :param position: The position of this ApplicationConfigConstantAttributes.
        :type: int
        """

        self._position = position

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApplicationConfigConstantAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
