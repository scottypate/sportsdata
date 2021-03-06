# coding: utf-8

"""
    LoL v3 Stats

    LoL v3 Stats  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LolStatsBoxScore(object):
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
        'game': 'LolStatsGame',
        'matches': 'list[LolStatsMatch]',
        'player_games': 'list[LolStatsPlayerGame]',
        'team_games': 'list[LolStatsTeamGame]'
    }

    attribute_map = {
        'game': 'Game',
        'matches': 'Matches',
        'player_games': 'PlayerGames',
        'team_games': 'TeamGames'
    }

    def __init__(self, game=None, matches=None, player_games=None, team_games=None):  # noqa: E501
        """LolStatsBoxScore - a model defined in Swagger"""  # noqa: E501
        self._game = None
        self._matches = None
        self._player_games = None
        self._team_games = None
        self.discriminator = None
        if game is not None:
            self.game = game
        if matches is not None:
            self.matches = matches
        if player_games is not None:
            self.player_games = player_games
        if team_games is not None:
            self.team_games = team_games

    @property
    def game(self):
        """Gets the game of this LolStatsBoxScore.  # noqa: E501


        :return: The game of this LolStatsBoxScore.  # noqa: E501
        :rtype: LolStatsGame
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this LolStatsBoxScore.


        :param game: The game of this LolStatsBoxScore.  # noqa: E501
        :type: LolStatsGame
        """

        self._game = game

    @property
    def matches(self):
        """Gets the matches of this LolStatsBoxScore.  # noqa: E501


        :return: The matches of this LolStatsBoxScore.  # noqa: E501
        :rtype: list[LolStatsMatch]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this LolStatsBoxScore.


        :param matches: The matches of this LolStatsBoxScore.  # noqa: E501
        :type: list[LolStatsMatch]
        """

        self._matches = matches

    @property
    def player_games(self):
        """Gets the player_games of this LolStatsBoxScore.  # noqa: E501


        :return: The player_games of this LolStatsBoxScore.  # noqa: E501
        :rtype: list[LolStatsPlayerGame]
        """
        return self._player_games

    @player_games.setter
    def player_games(self, player_games):
        """Sets the player_games of this LolStatsBoxScore.


        :param player_games: The player_games of this LolStatsBoxScore.  # noqa: E501
        :type: list[LolStatsPlayerGame]
        """

        self._player_games = player_games

    @property
    def team_games(self):
        """Gets the team_games of this LolStatsBoxScore.  # noqa: E501


        :return: The team_games of this LolStatsBoxScore.  # noqa: E501
        :rtype: list[LolStatsTeamGame]
        """
        return self._team_games

    @team_games.setter
    def team_games(self, team_games):
        """Sets the team_games of this LolStatsBoxScore.


        :param team_games: The team_games of this LolStatsBoxScore.  # noqa: E501
        :type: list[LolStatsTeamGame]
        """

        self._team_games = team_games

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
        if issubclass(LolStatsBoxScore, dict):
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
        if not isinstance(other, LolStatsBoxScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
