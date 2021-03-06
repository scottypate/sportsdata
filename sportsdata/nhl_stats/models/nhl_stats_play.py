# coding: utf-8

"""
    NHL v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NhlStatsPlay(object):
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
        'play_id': 'int',
        'period_id': 'int',
        'period_name': 'str',
        'sequence': 'int',
        'clock_minutes': 'int',
        'clock_seconds': 'int',
        'away_team_score': 'int',
        'home_team_score': 'int',
        'team_id': 'int',
        'team': 'str',
        'opponent_id': 'int',
        'opponent': 'str',
        'category': 'str',
        'type': 'str',
        'description': 'str',
        'player_id': 'int',
        'updated': 'str',
        'created': 'str',
        'first_assisted_by_player_id': 'int',
        'second_assisted_by_player_id': 'int',
        'power_play_team_id': 'int',
        'power_play_team': 'str',
        'opposing_player_id': 'int'
    }

    attribute_map = {
        'play_id': 'PlayID',
        'period_id': 'PeriodID',
        'period_name': 'PeriodName',
        'sequence': 'Sequence',
        'clock_minutes': 'ClockMinutes',
        'clock_seconds': 'ClockSeconds',
        'away_team_score': 'AwayTeamScore',
        'home_team_score': 'HomeTeamScore',
        'team_id': 'TeamID',
        'team': 'Team',
        'opponent_id': 'OpponentID',
        'opponent': 'Opponent',
        'category': 'Category',
        'type': 'Type',
        'description': 'Description',
        'player_id': 'PlayerID',
        'updated': 'Updated',
        'created': 'Created',
        'first_assisted_by_player_id': 'FirstAssistedByPlayerID',
        'second_assisted_by_player_id': 'SecondAssistedByPlayerID',
        'power_play_team_id': 'PowerPlayTeamID',
        'power_play_team': 'PowerPlayTeam',
        'opposing_player_id': 'OpposingPlayerID'
    }

    def __init__(self, play_id=None, period_id=None, period_name=None, sequence=None, clock_minutes=None, clock_seconds=None, away_team_score=None, home_team_score=None, team_id=None, team=None, opponent_id=None, opponent=None, category=None, type=None, description=None, player_id=None, updated=None, created=None, first_assisted_by_player_id=None, second_assisted_by_player_id=None, power_play_team_id=None, power_play_team=None, opposing_player_id=None):  # noqa: E501
        """NhlStatsPlay - a model defined in Swagger"""  # noqa: E501
        self._play_id = None
        self._period_id = None
        self._period_name = None
        self._sequence = None
        self._clock_minutes = None
        self._clock_seconds = None
        self._away_team_score = None
        self._home_team_score = None
        self._team_id = None
        self._team = None
        self._opponent_id = None
        self._opponent = None
        self._category = None
        self._type = None
        self._description = None
        self._player_id = None
        self._updated = None
        self._created = None
        self._first_assisted_by_player_id = None
        self._second_assisted_by_player_id = None
        self._power_play_team_id = None
        self._power_play_team = None
        self._opposing_player_id = None
        self.discriminator = None
        if play_id is not None:
            self.play_id = play_id
        if period_id is not None:
            self.period_id = period_id
        if period_name is not None:
            self.period_name = period_name
        if sequence is not None:
            self.sequence = sequence
        if clock_minutes is not None:
            self.clock_minutes = clock_minutes
        if clock_seconds is not None:
            self.clock_seconds = clock_seconds
        if away_team_score is not None:
            self.away_team_score = away_team_score
        if home_team_score is not None:
            self.home_team_score = home_team_score
        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if opponent_id is not None:
            self.opponent_id = opponent_id
        if opponent is not None:
            self.opponent = opponent
        if category is not None:
            self.category = category
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if player_id is not None:
            self.player_id = player_id
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if first_assisted_by_player_id is not None:
            self.first_assisted_by_player_id = first_assisted_by_player_id
        if second_assisted_by_player_id is not None:
            self.second_assisted_by_player_id = second_assisted_by_player_id
        if power_play_team_id is not None:
            self.power_play_team_id = power_play_team_id
        if power_play_team is not None:
            self.power_play_team = power_play_team
        if opposing_player_id is not None:
            self.opposing_player_id = opposing_player_id

    @property
    def play_id(self):
        """Gets the play_id of this NhlStatsPlay.  # noqa: E501


        :return: The play_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._play_id

    @play_id.setter
    def play_id(self, play_id):
        """Sets the play_id of this NhlStatsPlay.


        :param play_id: The play_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._play_id = play_id

    @property
    def period_id(self):
        """Gets the period_id of this NhlStatsPlay.  # noqa: E501


        :return: The period_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this NhlStatsPlay.


        :param period_id: The period_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._period_id = period_id

    @property
    def period_name(self):
        """Gets the period_name of this NhlStatsPlay.  # noqa: E501


        :return: The period_name of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._period_name

    @period_name.setter
    def period_name(self, period_name):
        """Sets the period_name of this NhlStatsPlay.


        :param period_name: The period_name of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._period_name = period_name

    @property
    def sequence(self):
        """Gets the sequence of this NhlStatsPlay.  # noqa: E501


        :return: The sequence of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this NhlStatsPlay.


        :param sequence: The sequence of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def clock_minutes(self):
        """Gets the clock_minutes of this NhlStatsPlay.  # noqa: E501


        :return: The clock_minutes of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._clock_minutes

    @clock_minutes.setter
    def clock_minutes(self, clock_minutes):
        """Sets the clock_minutes of this NhlStatsPlay.


        :param clock_minutes: The clock_minutes of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._clock_minutes = clock_minutes

    @property
    def clock_seconds(self):
        """Gets the clock_seconds of this NhlStatsPlay.  # noqa: E501


        :return: The clock_seconds of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._clock_seconds

    @clock_seconds.setter
    def clock_seconds(self, clock_seconds):
        """Sets the clock_seconds of this NhlStatsPlay.


        :param clock_seconds: The clock_seconds of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._clock_seconds = clock_seconds

    @property
    def away_team_score(self):
        """Gets the away_team_score of this NhlStatsPlay.  # noqa: E501


        :return: The away_team_score of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this NhlStatsPlay.


        :param away_team_score: The away_team_score of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._away_team_score = away_team_score

    @property
    def home_team_score(self):
        """Gets the home_team_score of this NhlStatsPlay.  # noqa: E501


        :return: The home_team_score of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this NhlStatsPlay.


        :param home_team_score: The home_team_score of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._home_team_score = home_team_score

    @property
    def team_id(self):
        """Gets the team_id of this NhlStatsPlay.  # noqa: E501


        :return: The team_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NhlStatsPlay.


        :param team_id: The team_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this NhlStatsPlay.  # noqa: E501


        :return: The team of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this NhlStatsPlay.


        :param team: The team of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opponent_id(self):
        """Gets the opponent_id of this NhlStatsPlay.  # noqa: E501


        :return: The opponent_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._opponent_id

    @opponent_id.setter
    def opponent_id(self, opponent_id):
        """Sets the opponent_id of this NhlStatsPlay.


        :param opponent_id: The opponent_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._opponent_id = opponent_id

    @property
    def opponent(self):
        """Gets the opponent of this NhlStatsPlay.  # noqa: E501


        :return: The opponent of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this NhlStatsPlay.


        :param opponent: The opponent of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def category(self):
        """Gets the category of this NhlStatsPlay.  # noqa: E501


        :return: The category of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NhlStatsPlay.


        :param category: The category of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def type(self):
        """Gets the type of this NhlStatsPlay.  # noqa: E501


        :return: The type of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NhlStatsPlay.


        :param type: The type of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this NhlStatsPlay.  # noqa: E501


        :return: The description of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NhlStatsPlay.


        :param description: The description of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def player_id(self):
        """Gets the player_id of this NhlStatsPlay.  # noqa: E501


        :return: The player_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this NhlStatsPlay.


        :param player_id: The player_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def updated(self):
        """Gets the updated of this NhlStatsPlay.  # noqa: E501


        :return: The updated of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NhlStatsPlay.


        :param updated: The updated of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this NhlStatsPlay.  # noqa: E501


        :return: The created of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NhlStatsPlay.


        :param created: The created of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def first_assisted_by_player_id(self):
        """Gets the first_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501


        :return: The first_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._first_assisted_by_player_id

    @first_assisted_by_player_id.setter
    def first_assisted_by_player_id(self, first_assisted_by_player_id):
        """Sets the first_assisted_by_player_id of this NhlStatsPlay.


        :param first_assisted_by_player_id: The first_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._first_assisted_by_player_id = first_assisted_by_player_id

    @property
    def second_assisted_by_player_id(self):
        """Gets the second_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501


        :return: The second_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._second_assisted_by_player_id

    @second_assisted_by_player_id.setter
    def second_assisted_by_player_id(self, second_assisted_by_player_id):
        """Sets the second_assisted_by_player_id of this NhlStatsPlay.


        :param second_assisted_by_player_id: The second_assisted_by_player_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._second_assisted_by_player_id = second_assisted_by_player_id

    @property
    def power_play_team_id(self):
        """Gets the power_play_team_id of this NhlStatsPlay.  # noqa: E501


        :return: The power_play_team_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._power_play_team_id

    @power_play_team_id.setter
    def power_play_team_id(self, power_play_team_id):
        """Sets the power_play_team_id of this NhlStatsPlay.


        :param power_play_team_id: The power_play_team_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._power_play_team_id = power_play_team_id

    @property
    def power_play_team(self):
        """Gets the power_play_team of this NhlStatsPlay.  # noqa: E501


        :return: The power_play_team of this NhlStatsPlay.  # noqa: E501
        :rtype: str
        """
        return self._power_play_team

    @power_play_team.setter
    def power_play_team(self, power_play_team):
        """Sets the power_play_team of this NhlStatsPlay.


        :param power_play_team: The power_play_team of this NhlStatsPlay.  # noqa: E501
        :type: str
        """

        self._power_play_team = power_play_team

    @property
    def opposing_player_id(self):
        """Gets the opposing_player_id of this NhlStatsPlay.  # noqa: E501


        :return: The opposing_player_id of this NhlStatsPlay.  # noqa: E501
        :rtype: int
        """
        return self._opposing_player_id

    @opposing_player_id.setter
    def opposing_player_id(self, opposing_player_id):
        """Sets the opposing_player_id of this NhlStatsPlay.


        :param opposing_player_id: The opposing_player_id of this NhlStatsPlay.  # noqa: E501
        :type: int
        """

        self._opposing_player_id = opposing_player_id

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
        if issubclass(NhlStatsPlay, dict):
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
        if not isinstance(other, NhlStatsPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
