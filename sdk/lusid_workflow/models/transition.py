# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.158
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class Transition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        '_from': 'str',
        'to': 'str',
        'trigger': 'str',
        'guard': 'str',
        'output': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'trigger': 'trigger',
        'guard': 'guard',
        'output': 'output'
    }

    required_map = {
        '_from': 'optional',
        'to': 'optional',
        'trigger': 'optional',
        'guard': 'optional',
        'output': 'optional'
    }

    def __init__(self, _from=None, to=None, trigger=None, guard=None, output=None, local_vars_configuration=None):  # noqa: E501
        """Transition - a model defined in OpenAPI"
        
        :param _from:  The State this Transition if coming From
        :type _from: str
        :param to:  The State this Transition is going To
        :type to: str
        :param trigger:  The Trigger for this Transition
        :type trigger: str
        :param guard:  The Guard for this Transition, if any
        :type guard: str
        :param output:  The Output action to invoke on successful Transition
        :type output: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self._trigger = None
        self._guard = None
        self._output = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.trigger = trigger
        self.guard = guard
        self.output = output

    @property
    def _from(self):
        """Gets the _from of this Transition.  # noqa: E501

        The State this Transition if coming From  # noqa: E501

        :return: The _from of this Transition.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Transition.

        The State this Transition if coming From  # noqa: E501

        :param _from: The _from of this Transition.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Transition.  # noqa: E501

        The State this Transition is going To  # noqa: E501

        :return: The to of this Transition.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Transition.

        The State this Transition is going To  # noqa: E501

        :param to: The to of this Transition.  # noqa: E501
        :type to: str
        """

        self._to = to

    @property
    def trigger(self):
        """Gets the trigger of this Transition.  # noqa: E501

        The Trigger for this Transition  # noqa: E501

        :return: The trigger of this Transition.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Transition.

        The Trigger for this Transition  # noqa: E501

        :param trigger: The trigger of this Transition.  # noqa: E501
        :type trigger: str
        """

        self._trigger = trigger

    @property
    def guard(self):
        """Gets the guard of this Transition.  # noqa: E501

        The Guard for this Transition, if any  # noqa: E501

        :return: The guard of this Transition.  # noqa: E501
        :rtype: str
        """
        return self._guard

    @guard.setter
    def guard(self, guard):
        """Sets the guard of this Transition.

        The Guard for this Transition, if any  # noqa: E501

        :param guard: The guard of this Transition.  # noqa: E501
        :type guard: str
        """

        self._guard = guard

    @property
    def output(self):
        """Gets the output of this Transition.  # noqa: E501

        The Output action to invoke on successful Transition  # noqa: E501

        :return: The output of this Transition.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Transition.

        The Output action to invoke on successful Transition  # noqa: E501

        :param output: The output of this Transition.  # noqa: E501
        :type output: str
        """

        self._output = output

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Transition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transition):
            return True

        return self.to_dict() != other.to_dict()
