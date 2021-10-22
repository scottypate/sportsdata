# coding: utf-8

"""
    NHL v3 Projections

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NhlProjectionsPenalty(object):
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
        'penalty_id': 'int',
        'period_id': 'int',
        'sequence': 'int',
        'time_remaining_minutes': 'int',
        'time_remaining_seconds': 'int',
        'description': 'str',
        'penalty_minutes': 'int',
        'penalized_team_id': 'int',
        'penalized_player_id': 'int',
        'drawn_by_team_id': 'int',
        'drawn_by_player_id': 'int',
        'is_bench_penalty': 'bool',
        'bench_penalty_served_by_player_id': 'int'
    }

    attribute_map = {
        'penalty_id': 'PenaltyID',
        'period_id': 'PeriodID',
        'sequence': 'Sequence',
        'time_remaining_minutes': 'TimeRemainingMinutes',
        'time_remaining_seconds': 'TimeRemainingSeconds',
        'description': 'Description',
        'penalty_minutes': 'PenaltyMinutes',
        'penalized_team_id': 'PenalizedTeamID',
        'penalized_player_id': 'PenalizedPlayerID',
        'drawn_by_team_id': 'DrawnByTeamID',
        'drawn_by_player_id': 'DrawnByPlayerID',
        'is_bench_penalty': 'IsBenchPenalty',
        'bench_penalty_served_by_player_id': 'BenchPenaltyServedByPlayerID'
    }

    def __init__(self, penalty_id=None, period_id=None, sequence=None, time_remaining_minutes=None, time_remaining_seconds=None, description=None, penalty_minutes=None, penalized_team_id=None, penalized_player_id=None, drawn_by_team_id=None, drawn_by_player_id=None, is_bench_penalty=None, bench_penalty_served_by_player_id=None):  # noqa: E501
        """NhlProjectionsPenalty - a model defined in Swagger"""  # noqa: E501
        self._penalty_id = None
        self._period_id = None
        self._sequence = None
        self._time_remaining_minutes = None
        self._time_remaining_seconds = None
        self._description = None
        self._penalty_minutes = None
        self._penalized_team_id = None
        self._penalized_player_id = None
        self._drawn_by_team_id = None
        self._drawn_by_player_id = None
        self._is_bench_penalty = None
        self._bench_penalty_served_by_player_id = None
        self.discriminator = None
        if penalty_id is not None:
            self.penalty_id = penalty_id
        if period_id is not None:
            self.period_id = period_id
        if sequence is not None:
            self.sequence = sequence
        if time_remaining_minutes is not None:
            self.time_remaining_minutes = time_remaining_minutes
        if time_remaining_seconds is not None:
            self.time_remaining_seconds = time_remaining_seconds
        if description is not None:
            self.description = description
        if penalty_minutes is not None:
            self.penalty_minutes = penalty_minutes
        if penalized_team_id is not None:
            self.penalized_team_id = penalized_team_id
        if penalized_player_id is not None:
            self.penalized_player_id = penalized_player_id
        if drawn_by_team_id is not None:
            self.drawn_by_team_id = drawn_by_team_id
        if drawn_by_player_id is not None:
            self.drawn_by_player_id = drawn_by_player_id
        if is_bench_penalty is not None:
            self.is_bench_penalty = is_bench_penalty
        if bench_penalty_served_by_player_id is not None:
            self.bench_penalty_served_by_player_id = bench_penalty_served_by_player_id

    @property
    def penalty_id(self):
        """Gets the penalty_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The penalty_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._penalty_id

    @penalty_id.setter
    def penalty_id(self, penalty_id):
        """Sets the penalty_id of this NhlProjectionsPenalty.


        :param penalty_id: The penalty_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._penalty_id = penalty_id

    @property
    def period_id(self):
        """Gets the period_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The period_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this NhlProjectionsPenalty.


        :param period_id: The period_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._period_id = period_id

    @property
    def sequence(self):
        """Gets the sequence of this NhlProjectionsPenalty.  # noqa: E501


        :return: The sequence of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this NhlProjectionsPenalty.


        :param sequence: The sequence of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def time_remaining_minutes(self):
        """Gets the time_remaining_minutes of this NhlProjectionsPenalty.  # noqa: E501


        :return: The time_remaining_minutes of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_minutes

    @time_remaining_minutes.setter
    def time_remaining_minutes(self, time_remaining_minutes):
        """Sets the time_remaining_minutes of this NhlProjectionsPenalty.


        :param time_remaining_minutes: The time_remaining_minutes of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._time_remaining_minutes = time_remaining_minutes

    @property
    def time_remaining_seconds(self):
        """Gets the time_remaining_seconds of this NhlProjectionsPenalty.  # noqa: E501


        :return: The time_remaining_seconds of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_seconds

    @time_remaining_seconds.setter
    def time_remaining_seconds(self, time_remaining_seconds):
        """Sets the time_remaining_seconds of this NhlProjectionsPenalty.


        :param time_remaining_seconds: The time_remaining_seconds of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._time_remaining_seconds = time_remaining_seconds

    @property
    def description(self):
        """Gets the description of this NhlProjectionsPenalty.  # noqa: E501


        :return: The description of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NhlProjectionsPenalty.


        :param description: The description of this NhlProjectionsPenalty.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def penalty_minutes(self):
        """Gets the penalty_minutes of this NhlProjectionsPenalty.  # noqa: E501


        :return: The penalty_minutes of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._penalty_minutes

    @penalty_minutes.setter
    def penalty_minutes(self, penalty_minutes):
        """Sets the penalty_minutes of this NhlProjectionsPenalty.


        :param penalty_minutes: The penalty_minutes of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._penalty_minutes = penalty_minutes

    @property
    def penalized_team_id(self):
        """Gets the penalized_team_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The penalized_team_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._penalized_team_id

    @penalized_team_id.setter
    def penalized_team_id(self, penalized_team_id):
        """Sets the penalized_team_id of this NhlProjectionsPenalty.


        :param penalized_team_id: The penalized_team_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._penalized_team_id = penalized_team_id

    @property
    def penalized_player_id(self):
        """Gets the penalized_player_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The penalized_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._penalized_player_id

    @penalized_player_id.setter
    def penalized_player_id(self, penalized_player_id):
        """Sets the penalized_player_id of this NhlProjectionsPenalty.


        :param penalized_player_id: The penalized_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._penalized_player_id = penalized_player_id

    @property
    def drawn_by_team_id(self):
        """Gets the drawn_by_team_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The drawn_by_team_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._drawn_by_team_id

    @drawn_by_team_id.setter
    def drawn_by_team_id(self, drawn_by_team_id):
        """Sets the drawn_by_team_id of this NhlProjectionsPenalty.


        :param drawn_by_team_id: The drawn_by_team_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._drawn_by_team_id = drawn_by_team_id

    @property
    def drawn_by_player_id(self):
        """Gets the drawn_by_player_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The drawn_by_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._drawn_by_player_id

    @drawn_by_player_id.setter
    def drawn_by_player_id(self, drawn_by_player_id):
        """Sets the drawn_by_player_id of this NhlProjectionsPenalty.


        :param drawn_by_player_id: The drawn_by_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._drawn_by_player_id = drawn_by_player_id

    @property
    def is_bench_penalty(self):
        """Gets the is_bench_penalty of this NhlProjectionsPenalty.  # noqa: E501


        :return: The is_bench_penalty of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: bool
        """
        return self._is_bench_penalty

    @is_bench_penalty.setter
    def is_bench_penalty(self, is_bench_penalty):
        """Sets the is_bench_penalty of this NhlProjectionsPenalty.


        :param is_bench_penalty: The is_bench_penalty of this NhlProjectionsPenalty.  # noqa: E501
        :type: bool
        """

        self._is_bench_penalty = is_bench_penalty

    @property
    def bench_penalty_served_by_player_id(self):
        """Gets the bench_penalty_served_by_player_id of this NhlProjectionsPenalty.  # noqa: E501


        :return: The bench_penalty_served_by_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :rtype: int
        """
        return self._bench_penalty_served_by_player_id

    @bench_penalty_served_by_player_id.setter
    def bench_penalty_served_by_player_id(self, bench_penalty_served_by_player_id):
        """Sets the bench_penalty_served_by_player_id of this NhlProjectionsPenalty.


        :param bench_penalty_served_by_player_id: The bench_penalty_served_by_player_id of this NhlProjectionsPenalty.  # noqa: E501
        :type: int
        """

        self._bench_penalty_served_by_player_id = bench_penalty_served_by_player_id

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
        if issubclass(NhlProjectionsPenalty, dict):
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
        if not isinstance(other, NhlProjectionsPenalty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
