import pprint
import re  # noqa: F401

import six


class CorrelationIdsSearchRequest(object):
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
        'correlation_ids': 'list[str]',
        'workflow_names': 'list[str]'
    }

    attribute_map = {
        'correlation_ids': 'correlationIds',
        'workflow_names': 'workflowNames'
    }

    def __init__(self, correlation_ids=None, workflow_names=None):  # noqa: E501
        """CorrelationIdsSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._correlation_ids = None
        self._workflow_names = None
        self.discriminator = None
        self.correlation_ids = correlation_ids
        self.workflow_names = workflow_names

    @property
    def correlation_ids(self):
        """Gets the correlation_ids of this CorrelationIdsSearchRequest.  # noqa: E501


        :return: The correlation_ids of this CorrelationIdsSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._correlation_ids

    @correlation_ids.setter
    def correlation_ids(self, correlation_ids):
        """Sets the correlation_ids of this CorrelationIdsSearchRequest.


        :param correlation_ids: The correlation_ids of this CorrelationIdsSearchRequest.  # noqa: E501
        :type: list[str]
        """
        self._correlation_ids = correlation_ids

    @property
    def workflow_names(self):
        """Gets the workflow_names of this CorrelationIdsSearchRequest.  # noqa: E501


        :return: The workflow_names of this CorrelationIdsSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._workflow_names

    @workflow_names.setter
    def workflow_names(self, workflow_names):
        """Sets the workflow_names of this CorrelationIdsSearchRequest.


        :param workflow_names: The workflow_names of this CorrelationIdsSearchRequest.  # noqa: E501
        :type: list[str]
        """
        self._workflow_names = workflow_names

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
        if issubclass(CorrelationIdsSearchRequest, dict):
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
        if not isinstance(other, CorrelationIdsSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
