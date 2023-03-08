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


class CreateTaskDefinitionRequest(object):
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
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'fields': 'list[FieldSchema]',
        'states': 'list[State]',
        'transitions': 'list[Transition]',
        'triggers': 'list[Trigger]',
        'initial_state': 'InitialState',
        'outputs': 'list[Output]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'fields': 'fields',
        'states': 'states',
        'transitions': 'transitions',
        'triggers': 'triggers',
        'initial_state': 'initialState',
        'outputs': 'outputs'
    }

    required_map = {
        'id': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'fields': 'optional',
        'states': 'optional',
        'transitions': 'optional',
        'triggers': 'optional',
        'initial_state': 'optional',
        'outputs': 'optional'
    }

    def __init__(self, id=None, display_name=None, description=None, fields=None, states=None, transitions=None, triggers=None, initial_state=None, outputs=None, local_vars_configuration=None):  # noqa: E501
        """CreateTaskDefinitionRequest - a model defined in OpenAPI"
        
        :param id: 
        :type id: lusid_workflow.ResourceId
        :param display_name:  Human readable name
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param fields:  Defines the fields associated with this Task
        :type fields: list[lusid_workflow.FieldSchema]
        :param states:  The states this Task Definition operates over
        :type states: list[lusid_workflow.State]
        :param transitions:  Transitions
        :type transitions: list[lusid_workflow.Transition]
        :param triggers:  Triggers
        :type triggers: list[lusid_workflow.Trigger]
        :param initial_state: 
        :type initial_state: lusid_workflow.InitialState
        :param outputs:  The Outputs of this Task
        :type outputs: list[lusid_workflow.Output]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._fields = None
        self._states = None
        self._transitions = None
        self._triggers = None
        self._initial_state = None
        self._outputs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.display_name = display_name
        self.description = description
        self.fields = fields
        self.states = states
        self.transitions = transitions
        self.triggers = triggers
        if initial_state is not None:
            self.initial_state = initial_state
        self.outputs = outputs

    @property
    def id(self):
        """Gets the id of this CreateTaskDefinitionRequest.  # noqa: E501


        :return: The id of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateTaskDefinitionRequest.


        :param id: The id of this CreateTaskDefinitionRequest.  # noqa: E501
        :type id: lusid_workflow.ResourceId
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this CreateTaskDefinitionRequest.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateTaskDefinitionRequest.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this CreateTaskDefinitionRequest.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreateTaskDefinitionRequest.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTaskDefinitionRequest.

        Human readable description  # noqa: E501

        :param description: The description of this CreateTaskDefinitionRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def fields(self):
        """Gets the fields of this CreateTaskDefinitionRequest.  # noqa: E501

        Defines the fields associated with this Task  # noqa: E501

        :return: The fields of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.FieldSchema]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CreateTaskDefinitionRequest.

        Defines the fields associated with this Task  # noqa: E501

        :param fields: The fields of this CreateTaskDefinitionRequest.  # noqa: E501
        :type fields: list[lusid_workflow.FieldSchema]
        """

        self._fields = fields

    @property
    def states(self):
        """Gets the states of this CreateTaskDefinitionRequest.  # noqa: E501

        The states this Task Definition operates over  # noqa: E501

        :return: The states of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this CreateTaskDefinitionRequest.

        The states this Task Definition operates over  # noqa: E501

        :param states: The states of this CreateTaskDefinitionRequest.  # noqa: E501
        :type states: list[lusid_workflow.State]
        """

        self._states = states

    @property
    def transitions(self):
        """Gets the transitions of this CreateTaskDefinitionRequest.  # noqa: E501

        Transitions  # noqa: E501

        :return: The transitions of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.Transition]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """Sets the transitions of this CreateTaskDefinitionRequest.

        Transitions  # noqa: E501

        :param transitions: The transitions of this CreateTaskDefinitionRequest.  # noqa: E501
        :type transitions: list[lusid_workflow.Transition]
        """

        self._transitions = transitions

    @property
    def triggers(self):
        """Gets the triggers of this CreateTaskDefinitionRequest.  # noqa: E501

        Triggers  # noqa: E501

        :return: The triggers of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this CreateTaskDefinitionRequest.

        Triggers  # noqa: E501

        :param triggers: The triggers of this CreateTaskDefinitionRequest.  # noqa: E501
        :type triggers: list[lusid_workflow.Trigger]
        """

        self._triggers = triggers

    @property
    def initial_state(self):
        """Gets the initial_state of this CreateTaskDefinitionRequest.  # noqa: E501


        :return: The initial_state of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: lusid_workflow.InitialState
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state):
        """Sets the initial_state of this CreateTaskDefinitionRequest.


        :param initial_state: The initial_state of this CreateTaskDefinitionRequest.  # noqa: E501
        :type initial_state: lusid_workflow.InitialState
        """

        self._initial_state = initial_state

    @property
    def outputs(self):
        """Gets the outputs of this CreateTaskDefinitionRequest.  # noqa: E501

        The Outputs of this Task  # noqa: E501

        :return: The outputs of this CreateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.Output]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this CreateTaskDefinitionRequest.

        The Outputs of this Task  # noqa: E501

        :param outputs: The outputs of this CreateTaskDefinitionRequest.  # noqa: E501
        :type outputs: list[lusid_workflow.Output]
        """

        self._outputs = outputs

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
        if not isinstance(other, CreateTaskDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTaskDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
