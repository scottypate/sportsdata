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

class NhlStatsBoxScore(object):
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
        'game': 'NhlStatsGame',
        'periods': 'list[NhlStatsPeriod]',
        'team_games': 'list[NhlStatsTeamGame]',
        'player_games': 'list[NhlStatsPlayerGame]',
        'shootout_plays': 'list[NhlStatsPlay]'
    }

    attribute_map = {
        'game': 'Game',
        'periods': 'Periods',
        'team_games': 'TeamGames',
        'player_games': 'PlayerGames',
        'shootout_plays': 'ShootoutPlays'
    }

    def __init__(self, game=None, periods=None, team_games=None, player_games=None, shootout_plays=None):  # noqa: E501
        """NhlStatsBoxScore - a model defined in Swagger"""  # noqa: E501
        self._game = None
        self._periods = None
        self._team_games = None
        self._player_games = None
        self._shootout_plays = None
        self.discriminator = None
        if game is not None:
            self.game = game
        if periods is not None:
            self.periods = periods
        if team_games is not None:
            self.team_games = team_games
        if player_games is not None:
            self.player_games = player_games
        if shootout_plays is not None:
            self.shootout_plays = shootout_plays

    @property
    def game(self):
        """Gets the game of this NhlStatsBoxScore.  # noqa: E501


        :return: The game of this NhlStatsBoxScore.  # noqa: E501
        :rtype: NhlStatsGame
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this NhlStatsBoxScore.


        :param game: The game of this NhlStatsBoxScore.  # noqa: E501
        :type: NhlStatsGame
        """

        self._game = game

    @property
    def periods(self):
        """Gets the periods of this NhlStatsBoxScore.  # noqa: E501


        :return: The periods of this NhlStatsBoxScore.  # noqa: E501
        :rtype: list[NhlStatsPeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this NhlStatsBoxScore.


        :param periods: The periods of this NhlStatsBoxScore.  # noqa: E501
        :type: list[NhlStatsPeriod]
        """

        self._periods = periods

    @property
    def team_games(self):
        """Gets the team_games of this NhlStatsBoxScore.  # noqa: E501


        :return: The team_games of this NhlStatsBoxScore.  # noqa: E501
        :rtype: list[NhlStatsTeamGame]
        """
        return self._team_games

    @team_games.setter
    def team_games(self, team_games):
        """Sets the team_games of this NhlStatsBoxScore.


        :param team_games: The team_games of this NhlStatsBoxScore.  # noqa: E501
        :type: list[NhlStatsTeamGame]
        """

        self._team_games = team_games

    @property
    def player_games(self):
        """Gets the player_games of this NhlStatsBoxScore.  # noqa: E501


        :return: The player_games of this NhlStatsBoxScore.  # noqa: E501
        :rtype: list[NhlStatsPlayerGame]
        """
        return self._player_games

    @player_games.setter
    def player_games(self, player_games):
        """Sets the player_games of this NhlStatsBoxScore.


        :param player_games: The player_games of this NhlStatsBoxScore.  # noqa: E501
        :type: list[NhlStatsPlayerGame]
        """

        self._player_games = player_games

    @property
    def shootout_plays(self):
        """Gets the shootout_plays of this NhlStatsBoxScore.  # noqa: E501


        :return: The shootout_plays of this NhlStatsBoxScore.  # noqa: E501
        :rtype: list[NhlStatsPlay]
        """
        return self._shootout_plays

    @shootout_plays.setter
    def shootout_plays(self, shootout_plays):
        """Sets the shootout_plays of this NhlStatsBoxScore.


        :param shootout_plays: The shootout_plays of this NhlStatsBoxScore.  # noqa: E501
        :type: list[NhlStatsPlay]
        """

        self._shootout_plays = shootout_plays

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
        if issubclass(NhlStatsBoxScore, dict):
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
        if not isinstance(other, NhlStatsBoxScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other