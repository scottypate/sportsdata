# coding: utf-8

"""
    NFL v3 Projections

    NFL projected stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflProjectionsDfsSlate(object):
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
        'slate_id': 'int',
        'operator': 'str',
        'operator_slate_id': 'int',
        'operator_name': 'str',
        'operator_day': 'str',
        'operator_start_time': 'str',
        'number_of_games': 'int',
        'is_multi_day_slate': 'bool',
        'removed_by_operator': 'bool',
        'operator_game_type': 'str',
        'dfs_slate_games': 'list[NflProjectionsDfsSlateGame]',
        'dfs_slate_players': 'list[NflProjectionsDfsSlatePlayer]',
        'slate_roster_slots': 'list[str]',
        'salary_cap': 'int'
    }

    attribute_map = {
        'slate_id': 'SlateID',
        'operator': 'Operator',
        'operator_slate_id': 'OperatorSlateID',
        'operator_name': 'OperatorName',
        'operator_day': 'OperatorDay',
        'operator_start_time': 'OperatorStartTime',
        'number_of_games': 'NumberOfGames',
        'is_multi_day_slate': 'IsMultiDaySlate',
        'removed_by_operator': 'RemovedByOperator',
        'operator_game_type': 'OperatorGameType',
        'dfs_slate_games': 'DfsSlateGames',
        'dfs_slate_players': 'DfsSlatePlayers',
        'slate_roster_slots': 'SlateRosterSlots',
        'salary_cap': 'SalaryCap'
    }

    def __init__(self, slate_id=None, operator=None, operator_slate_id=None, operator_name=None, operator_day=None, operator_start_time=None, number_of_games=None, is_multi_day_slate=None, removed_by_operator=None, operator_game_type=None, dfs_slate_games=None, dfs_slate_players=None, slate_roster_slots=None, salary_cap=None):  # noqa: E501
        """NflProjectionsDfsSlate - a model defined in Swagger"""  # noqa: E501
        self._slate_id = None
        self._operator = None
        self._operator_slate_id = None
        self._operator_name = None
        self._operator_day = None
        self._operator_start_time = None
        self._number_of_games = None
        self._is_multi_day_slate = None
        self._removed_by_operator = None
        self._operator_game_type = None
        self._dfs_slate_games = None
        self._dfs_slate_players = None
        self._slate_roster_slots = None
        self._salary_cap = None
        self.discriminator = None
        if slate_id is not None:
            self.slate_id = slate_id
        if operator is not None:
            self.operator = operator
        if operator_slate_id is not None:
            self.operator_slate_id = operator_slate_id
        if operator_name is not None:
            self.operator_name = operator_name
        if operator_day is not None:
            self.operator_day = operator_day
        if operator_start_time is not None:
            self.operator_start_time = operator_start_time
        if number_of_games is not None:
            self.number_of_games = number_of_games
        if is_multi_day_slate is not None:
            self.is_multi_day_slate = is_multi_day_slate
        if removed_by_operator is not None:
            self.removed_by_operator = removed_by_operator
        if operator_game_type is not None:
            self.operator_game_type = operator_game_type
        if dfs_slate_games is not None:
            self.dfs_slate_games = dfs_slate_games
        if dfs_slate_players is not None:
            self.dfs_slate_players = dfs_slate_players
        if slate_roster_slots is not None:
            self.slate_roster_slots = slate_roster_slots
        if salary_cap is not None:
            self.salary_cap = salary_cap

    @property
    def slate_id(self):
        """Gets the slate_id of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The slate_id of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: int
        """
        return self._slate_id

    @slate_id.setter
    def slate_id(self, slate_id):
        """Sets the slate_id of this NflProjectionsDfsSlate.


        :param slate_id: The slate_id of this NflProjectionsDfsSlate.  # noqa: E501
        :type: int
        """

        self._slate_id = slate_id

    @property
    def operator(self):
        """Gets the operator of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this NflProjectionsDfsSlate.


        :param operator: The operator of this NflProjectionsDfsSlate.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def operator_slate_id(self):
        """Gets the operator_slate_id of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator_slate_id of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: int
        """
        return self._operator_slate_id

    @operator_slate_id.setter
    def operator_slate_id(self, operator_slate_id):
        """Sets the operator_slate_id of this NflProjectionsDfsSlate.


        :param operator_slate_id: The operator_slate_id of this NflProjectionsDfsSlate.  # noqa: E501
        :type: int
        """

        self._operator_slate_id = operator_slate_id

    @property
    def operator_name(self):
        """Gets the operator_name of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator_name of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: str
        """
        return self._operator_name

    @operator_name.setter
    def operator_name(self, operator_name):
        """Sets the operator_name of this NflProjectionsDfsSlate.


        :param operator_name: The operator_name of this NflProjectionsDfsSlate.  # noqa: E501
        :type: str
        """

        self._operator_name = operator_name

    @property
    def operator_day(self):
        """Gets the operator_day of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator_day of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: str
        """
        return self._operator_day

    @operator_day.setter
    def operator_day(self, operator_day):
        """Sets the operator_day of this NflProjectionsDfsSlate.


        :param operator_day: The operator_day of this NflProjectionsDfsSlate.  # noqa: E501
        :type: str
        """

        self._operator_day = operator_day

    @property
    def operator_start_time(self):
        """Gets the operator_start_time of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator_start_time of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: str
        """
        return self._operator_start_time

    @operator_start_time.setter
    def operator_start_time(self, operator_start_time):
        """Sets the operator_start_time of this NflProjectionsDfsSlate.


        :param operator_start_time: The operator_start_time of this NflProjectionsDfsSlate.  # noqa: E501
        :type: str
        """

        self._operator_start_time = operator_start_time

    @property
    def number_of_games(self):
        """Gets the number_of_games of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The number_of_games of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_games

    @number_of_games.setter
    def number_of_games(self, number_of_games):
        """Sets the number_of_games of this NflProjectionsDfsSlate.


        :param number_of_games: The number_of_games of this NflProjectionsDfsSlate.  # noqa: E501
        :type: int
        """

        self._number_of_games = number_of_games

    @property
    def is_multi_day_slate(self):
        """Gets the is_multi_day_slate of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The is_multi_day_slate of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_day_slate

    @is_multi_day_slate.setter
    def is_multi_day_slate(self, is_multi_day_slate):
        """Sets the is_multi_day_slate of this NflProjectionsDfsSlate.


        :param is_multi_day_slate: The is_multi_day_slate of this NflProjectionsDfsSlate.  # noqa: E501
        :type: bool
        """

        self._is_multi_day_slate = is_multi_day_slate

    @property
    def removed_by_operator(self):
        """Gets the removed_by_operator of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The removed_by_operator of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: bool
        """
        return self._removed_by_operator

    @removed_by_operator.setter
    def removed_by_operator(self, removed_by_operator):
        """Sets the removed_by_operator of this NflProjectionsDfsSlate.


        :param removed_by_operator: The removed_by_operator of this NflProjectionsDfsSlate.  # noqa: E501
        :type: bool
        """

        self._removed_by_operator = removed_by_operator

    @property
    def operator_game_type(self):
        """Gets the operator_game_type of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The operator_game_type of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: str
        """
        return self._operator_game_type

    @operator_game_type.setter
    def operator_game_type(self, operator_game_type):
        """Sets the operator_game_type of this NflProjectionsDfsSlate.


        :param operator_game_type: The operator_game_type of this NflProjectionsDfsSlate.  # noqa: E501
        :type: str
        """

        self._operator_game_type = operator_game_type

    @property
    def dfs_slate_games(self):
        """Gets the dfs_slate_games of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The dfs_slate_games of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: list[NflProjectionsDfsSlateGame]
        """
        return self._dfs_slate_games

    @dfs_slate_games.setter
    def dfs_slate_games(self, dfs_slate_games):
        """Sets the dfs_slate_games of this NflProjectionsDfsSlate.


        :param dfs_slate_games: The dfs_slate_games of this NflProjectionsDfsSlate.  # noqa: E501
        :type: list[NflProjectionsDfsSlateGame]
        """

        self._dfs_slate_games = dfs_slate_games

    @property
    def dfs_slate_players(self):
        """Gets the dfs_slate_players of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The dfs_slate_players of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: list[NflProjectionsDfsSlatePlayer]
        """
        return self._dfs_slate_players

    @dfs_slate_players.setter
    def dfs_slate_players(self, dfs_slate_players):
        """Sets the dfs_slate_players of this NflProjectionsDfsSlate.


        :param dfs_slate_players: The dfs_slate_players of this NflProjectionsDfsSlate.  # noqa: E501
        :type: list[NflProjectionsDfsSlatePlayer]
        """

        self._dfs_slate_players = dfs_slate_players

    @property
    def slate_roster_slots(self):
        """Gets the slate_roster_slots of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The slate_roster_slots of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: list[str]
        """
        return self._slate_roster_slots

    @slate_roster_slots.setter
    def slate_roster_slots(self, slate_roster_slots):
        """Sets the slate_roster_slots of this NflProjectionsDfsSlate.


        :param slate_roster_slots: The slate_roster_slots of this NflProjectionsDfsSlate.  # noqa: E501
        :type: list[str]
        """

        self._slate_roster_slots = slate_roster_slots

    @property
    def salary_cap(self):
        """Gets the salary_cap of this NflProjectionsDfsSlate.  # noqa: E501


        :return: The salary_cap of this NflProjectionsDfsSlate.  # noqa: E501
        :rtype: int
        """
        return self._salary_cap

    @salary_cap.setter
    def salary_cap(self, salary_cap):
        """Sets the salary_cap of this NflProjectionsDfsSlate.


        :param salary_cap: The salary_cap of this NflProjectionsDfsSlate.  # noqa: E501
        :type: int
        """

        self._salary_cap = salary_cap

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
        if issubclass(NflProjectionsDfsSlate, dict):
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
        if not isinstance(other, NflProjectionsDfsSlate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
