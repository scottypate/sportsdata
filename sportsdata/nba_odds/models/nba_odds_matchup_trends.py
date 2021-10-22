# coding: utf-8

"""
    NBA v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NbaOddsMatchupTrends(object):
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
        'upcoming_game': 'NbaOddsGame',
        'team_trends': 'list[NbaOddsTeamTrends]',
        'team_matchup_trends': 'list[NbaOddsTeamGameTrends]',
        'opponent_matchup_trends': 'list[NbaOddsTeamGameTrends]',
        'previous_games': 'list[NbaOddsGame]'
    }

    attribute_map = {
        'upcoming_game': 'UpcomingGame',
        'team_trends': 'TeamTrends',
        'team_matchup_trends': 'TeamMatchupTrends',
        'opponent_matchup_trends': 'OpponentMatchupTrends',
        'previous_games': 'PreviousGames'
    }

    def __init__(self, upcoming_game=None, team_trends=None, team_matchup_trends=None, opponent_matchup_trends=None, previous_games=None):  # noqa: E501
        """NbaOddsMatchupTrends - a model defined in Swagger"""  # noqa: E501
        self._upcoming_game = None
        self._team_trends = None
        self._team_matchup_trends = None
        self._opponent_matchup_trends = None
        self._previous_games = None
        self.discriminator = None
        if upcoming_game is not None:
            self.upcoming_game = upcoming_game
        if team_trends is not None:
            self.team_trends = team_trends
        if team_matchup_trends is not None:
            self.team_matchup_trends = team_matchup_trends
        if opponent_matchup_trends is not None:
            self.opponent_matchup_trends = opponent_matchup_trends
        if previous_games is not None:
            self.previous_games = previous_games

    @property
    def upcoming_game(self):
        """Gets the upcoming_game of this NbaOddsMatchupTrends.  # noqa: E501


        :return: The upcoming_game of this NbaOddsMatchupTrends.  # noqa: E501
        :rtype: NbaOddsGame
        """
        return self._upcoming_game

    @upcoming_game.setter
    def upcoming_game(self, upcoming_game):
        """Sets the upcoming_game of this NbaOddsMatchupTrends.


        :param upcoming_game: The upcoming_game of this NbaOddsMatchupTrends.  # noqa: E501
        :type: NbaOddsGame
        """

        self._upcoming_game = upcoming_game

    @property
    def team_trends(self):
        """Gets the team_trends of this NbaOddsMatchupTrends.  # noqa: E501


        :return: The team_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :rtype: list[NbaOddsTeamTrends]
        """
        return self._team_trends

    @team_trends.setter
    def team_trends(self, team_trends):
        """Sets the team_trends of this NbaOddsMatchupTrends.


        :param team_trends: The team_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :type: list[NbaOddsTeamTrends]
        """

        self._team_trends = team_trends

    @property
    def team_matchup_trends(self):
        """Gets the team_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501


        :return: The team_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :rtype: list[NbaOddsTeamGameTrends]
        """
        return self._team_matchup_trends

    @team_matchup_trends.setter
    def team_matchup_trends(self, team_matchup_trends):
        """Sets the team_matchup_trends of this NbaOddsMatchupTrends.


        :param team_matchup_trends: The team_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :type: list[NbaOddsTeamGameTrends]
        """

        self._team_matchup_trends = team_matchup_trends

    @property
    def opponent_matchup_trends(self):
        """Gets the opponent_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501


        :return: The opponent_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :rtype: list[NbaOddsTeamGameTrends]
        """
        return self._opponent_matchup_trends

    @opponent_matchup_trends.setter
    def opponent_matchup_trends(self, opponent_matchup_trends):
        """Sets the opponent_matchup_trends of this NbaOddsMatchupTrends.


        :param opponent_matchup_trends: The opponent_matchup_trends of this NbaOddsMatchupTrends.  # noqa: E501
        :type: list[NbaOddsTeamGameTrends]
        """

        self._opponent_matchup_trends = opponent_matchup_trends

    @property
    def previous_games(self):
        """Gets the previous_games of this NbaOddsMatchupTrends.  # noqa: E501


        :return: The previous_games of this NbaOddsMatchupTrends.  # noqa: E501
        :rtype: list[NbaOddsGame]
        """
        return self._previous_games

    @previous_games.setter
    def previous_games(self, previous_games):
        """Sets the previous_games of this NbaOddsMatchupTrends.


        :param previous_games: The previous_games of this NbaOddsMatchupTrends.  # noqa: E501
        :type: list[NbaOddsGame]
        """

        self._previous_games = previous_games

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
        if issubclass(NbaOddsMatchupTrends, dict):
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
        if not isinstance(other, NbaOddsMatchupTrends):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
