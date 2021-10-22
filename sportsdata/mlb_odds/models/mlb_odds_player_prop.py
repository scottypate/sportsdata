# coding: utf-8

"""
    MLB v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbOddsPlayerProp(object):
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
        'player_id': 'int',
        'game_id': 'int',
        'name': 'str',
        'opponent': 'str',
        'team': 'str',
        'date_time': 'str',
        'description': 'str',
        'over_under': 'float',
        'over_payout': 'int',
        'under_payout': 'int',
        'bet_result': 'str',
        'stat_result': 'float'
    }

    attribute_map = {
        'player_id': 'PlayerID',
        'game_id': 'GameID',
        'name': 'Name',
        'opponent': 'Opponent',
        'team': 'Team',
        'date_time': 'DateTime',
        'description': 'Description',
        'over_under': 'OverUnder',
        'over_payout': 'OverPayout',
        'under_payout': 'UnderPayout',
        'bet_result': 'BetResult',
        'stat_result': 'StatResult'
    }

    def __init__(self, player_id=None, game_id=None, name=None, opponent=None, team=None, date_time=None, description=None, over_under=None, over_payout=None, under_payout=None, bet_result=None, stat_result=None):  # noqa: E501
        """MlbOddsPlayerProp - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._game_id = None
        self._name = None
        self._opponent = None
        self._team = None
        self._date_time = None
        self._description = None
        self._over_under = None
        self._over_payout = None
        self._under_payout = None
        self._bet_result = None
        self._stat_result = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if game_id is not None:
            self.game_id = game_id
        if name is not None:
            self.name = name
        if opponent is not None:
            self.opponent = opponent
        if team is not None:
            self.team = team
        if date_time is not None:
            self.date_time = date_time
        if description is not None:
            self.description = description
        if over_under is not None:
            self.over_under = over_under
        if over_payout is not None:
            self.over_payout = over_payout
        if under_payout is not None:
            self.under_payout = under_payout
        if bet_result is not None:
            self.bet_result = bet_result
        if stat_result is not None:
            self.stat_result = stat_result

    @property
    def player_id(self):
        """Gets the player_id of this MlbOddsPlayerProp.  # noqa: E501


        :return: The player_id of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this MlbOddsPlayerProp.


        :param player_id: The player_id of this MlbOddsPlayerProp.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def game_id(self):
        """Gets the game_id of this MlbOddsPlayerProp.  # noqa: E501


        :return: The game_id of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this MlbOddsPlayerProp.


        :param game_id: The game_id of this MlbOddsPlayerProp.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def name(self):
        """Gets the name of this MlbOddsPlayerProp.  # noqa: E501


        :return: The name of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MlbOddsPlayerProp.


        :param name: The name of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def opponent(self):
        """Gets the opponent of this MlbOddsPlayerProp.  # noqa: E501


        :return: The opponent of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this MlbOddsPlayerProp.


        :param opponent: The opponent of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def team(self):
        """Gets the team of this MlbOddsPlayerProp.  # noqa: E501


        :return: The team of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this MlbOddsPlayerProp.


        :param team: The team of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def date_time(self):
        """Gets the date_time of this MlbOddsPlayerProp.  # noqa: E501


        :return: The date_time of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this MlbOddsPlayerProp.


        :param date_time: The date_time of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def description(self):
        """Gets the description of this MlbOddsPlayerProp.  # noqa: E501


        :return: The description of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MlbOddsPlayerProp.


        :param description: The description of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def over_under(self):
        """Gets the over_under of this MlbOddsPlayerProp.  # noqa: E501


        :return: The over_under of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: float
        """
        return self._over_under

    @over_under.setter
    def over_under(self, over_under):
        """Sets the over_under of this MlbOddsPlayerProp.


        :param over_under: The over_under of this MlbOddsPlayerProp.  # noqa: E501
        :type: float
        """

        self._over_under = over_under

    @property
    def over_payout(self):
        """Gets the over_payout of this MlbOddsPlayerProp.  # noqa: E501


        :return: The over_payout of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: int
        """
        return self._over_payout

    @over_payout.setter
    def over_payout(self, over_payout):
        """Sets the over_payout of this MlbOddsPlayerProp.


        :param over_payout: The over_payout of this MlbOddsPlayerProp.  # noqa: E501
        :type: int
        """

        self._over_payout = over_payout

    @property
    def under_payout(self):
        """Gets the under_payout of this MlbOddsPlayerProp.  # noqa: E501


        :return: The under_payout of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: int
        """
        return self._under_payout

    @under_payout.setter
    def under_payout(self, under_payout):
        """Sets the under_payout of this MlbOddsPlayerProp.


        :param under_payout: The under_payout of this MlbOddsPlayerProp.  # noqa: E501
        :type: int
        """

        self._under_payout = under_payout

    @property
    def bet_result(self):
        """Gets the bet_result of this MlbOddsPlayerProp.  # noqa: E501


        :return: The bet_result of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: str
        """
        return self._bet_result

    @bet_result.setter
    def bet_result(self, bet_result):
        """Sets the bet_result of this MlbOddsPlayerProp.


        :param bet_result: The bet_result of this MlbOddsPlayerProp.  # noqa: E501
        :type: str
        """

        self._bet_result = bet_result

    @property
    def stat_result(self):
        """Gets the stat_result of this MlbOddsPlayerProp.  # noqa: E501


        :return: The stat_result of this MlbOddsPlayerProp.  # noqa: E501
        :rtype: float
        """
        return self._stat_result

    @stat_result.setter
    def stat_result(self, stat_result):
        """Sets the stat_result of this MlbOddsPlayerProp.


        :param stat_result: The stat_result of this MlbOddsPlayerProp.  # noqa: E501
        :type: float
        """

        self._stat_result = stat_result

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
        if issubclass(MlbOddsPlayerProp, dict):
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
        if not isinstance(other, MlbOddsPlayerProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
