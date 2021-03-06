# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PolicyResult(object):
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
        'policy_id': 'str',
        'system_id': 'str',
        'id': 'str',
        'started_at': 'datetime',
        'ended_at': 'datetime',
        'success': 'bool',
        'exit_status': 'int',
        'std_err': 'str',
        'std_out': 'str',
        'state': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'policy_id': 'policyID',
        'system_id': 'systemID',
        'id': 'id',
        'started_at': 'startedAt',
        'ended_at': 'endedAt',
        'success': 'success',
        'exit_status': 'exitStatus',
        'std_err': 'stdErr',
        'std_out': 'stdOut',
        'state': 'state',
        'detail': 'detail'
    }

    def __init__(self, policy_id=None, system_id=None, id=None, started_at=None, ended_at=None, success=None, exit_status=None, std_err=None, std_out=None, state=None, detail=None):  # noqa: E501
        """PolicyResult - a model defined in Swagger"""  # noqa: E501

        self._policy_id = None
        self._system_id = None
        self._id = None
        self._started_at = None
        self._ended_at = None
        self._success = None
        self._exit_status = None
        self._std_err = None
        self._std_out = None
        self._state = None
        self._detail = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if system_id is not None:
            self.system_id = system_id
        if id is not None:
            self.id = id
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if success is not None:
            self.success = success
        if exit_status is not None:
            self.exit_status = exit_status
        if std_err is not None:
            self.std_err = std_err
        if std_out is not None:
            self.std_out = std_out
        if state is not None:
            self.state = state
        if detail is not None:
            self.detail = detail

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyResult.  # noqa: E501

        ObjectId uniquely identifying the parent Policy.  # noqa: E501

        :return: The policy_id of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyResult.

        ObjectId uniquely identifying the parent Policy.  # noqa: E501

        :param policy_id: The policy_id of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def system_id(self):
        """Gets the system_id of this PolicyResult.  # noqa: E501

        ObjectId uniquely identifying the parent System.  # noqa: E501

        :return: The system_id of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this PolicyResult.

        ObjectId uniquely identifying the parent System.  # noqa: E501

        :param system_id: The system_id of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def id(self):
        """Gets the id of this PolicyResult.  # noqa: E501

        ObjectId uniquely identifying a Policy Result.  # noqa: E501

        :return: The id of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyResult.

        ObjectId uniquely identifying a Policy Result.  # noqa: E501

        :param id: The id of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def started_at(self):
        """Gets the started_at of this PolicyResult.  # noqa: E501

        The start of the policy application.  # noqa: E501

        :return: The started_at of this PolicyResult.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this PolicyResult.

        The start of the policy application.  # noqa: E501

        :param started_at: The started_at of this PolicyResult.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def ended_at(self):
        """Gets the ended_at of this PolicyResult.  # noqa: E501

        The end of the policy application.  # noqa: E501

        :return: The ended_at of this PolicyResult.  # noqa: E501
        :rtype: datetime
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this PolicyResult.

        The end of the policy application.  # noqa: E501

        :param ended_at: The ended_at of this PolicyResult.  # noqa: E501
        :type: datetime
        """

        self._ended_at = ended_at

    @property
    def success(self):
        """Gets the success of this PolicyResult.  # noqa: E501

        True if the policy was successfully applied; false otherwise.  # noqa: E501

        :return: The success of this PolicyResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PolicyResult.

        True if the policy was successfully applied; false otherwise.  # noqa: E501

        :param success: The success of this PolicyResult.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def exit_status(self):
        """Gets the exit_status of this PolicyResult.  # noqa: E501

        The 32-bit unsigned exit status from the applying the policy.  # noqa: E501

        :return: The exit_status of this PolicyResult.  # noqa: E501
        :rtype: int
        """
        return self._exit_status

    @exit_status.setter
    def exit_status(self, exit_status):
        """Sets the exit_status of this PolicyResult.

        The 32-bit unsigned exit status from the applying the policy.  # noqa: E501

        :param exit_status: The exit_status of this PolicyResult.  # noqa: E501
        :type: int
        """

        self._exit_status = exit_status

    @property
    def std_err(self):
        """Gets the std_err of this PolicyResult.  # noqa: E501

        The STDERR output from applying the policy.  # noqa: E501

        :return: The std_err of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._std_err

    @std_err.setter
    def std_err(self, std_err):
        """Sets the std_err of this PolicyResult.

        The STDERR output from applying the policy.  # noqa: E501

        :param std_err: The std_err of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._std_err = std_err

    @property
    def std_out(self):
        """Gets the std_out of this PolicyResult.  # noqa: E501

        The STDOUT output from applying the policy.  # noqa: E501

        :return: The std_out of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._std_out

    @std_out.setter
    def std_out(self, std_out):
        """Sets the std_out of this PolicyResult.

        The STDOUT output from applying the policy.  # noqa: E501

        :param std_out: The std_out of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._std_out = std_out

    @property
    def state(self):
        """Gets the state of this PolicyResult.  # noqa: E501

        Enumeration describing the state of the policy. Success, failed, or pending.  # noqa: E501

        :return: The state of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PolicyResult.

        Enumeration describing the state of the policy. Success, failed, or pending.  # noqa: E501

        :param state: The state of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def detail(self):
        """Gets the detail of this PolicyResult.  # noqa: E501

        Details pertaining to the policy result.  # noqa: E501

        :return: The detail of this PolicyResult.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this PolicyResult.

        Details pertaining to the policy result.  # noqa: E501

        :param detail: The detail of this PolicyResult.  # noqa: E501
        :type: str
        """

        self._detail = detail

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
        if issubclass(PolicyResult, dict):
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
        if not isinstance(other, PolicyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
