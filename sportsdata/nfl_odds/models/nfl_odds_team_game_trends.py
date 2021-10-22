# coding: utf-8

"""
    NFL v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflOddsTeamGameTrends(object):
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
        'scope': 'str',
        'team_id': 'int',
        'team': 'str',
        'opponent_id': 'int',
        'opponent': 'str',
        'wins': 'int',
        'losses': 'int',
        'ties': 'int',
        'wins_against_the_spread': 'int',
        'losses_against_the_spread': 'int',
        'pushes_against_the_spread': 'int',
        'overs': 'int',
        'unders': 'int',
        'over_under_pushes': 'int',
        'average_score': 'float',
        'average_opponent_score': 'float'
    }

    attribute_map = {
        'scope': 'Scope',
        'team_id': 'TeamID',
        'team': 'Team',
        'opponent_id': 'OpponentID',
        'opponent': 'Opponent',
        'wins': 'Wins',
        'losses': 'Losses',
        'ties': 'Ties',
        'wins_against_the_spread': 'WinsAgainstTheSpread',
        'losses_against_the_spread': 'LossesAgainstTheSpread',
        'pushes_against_the_spread': 'PushesAgainstTheSpread',
        'overs': 'Overs',
        'unders': 'Unders',
        'over_under_pushes': 'OverUnderPushes',
        'average_score': 'AverageScore',
        'average_opponent_score': 'AverageOpponentScore'
    }

    def __init__(self, scope=None, team_id=None, team=None, opponent_id=None, opponent=None, wins=None, losses=None, ties=None, wins_against_the_spread=None, losses_against_the_spread=None, pushes_against_the_spread=None, overs=None, unders=None, over_under_pushes=None, average_score=None, average_opponent_score=None):  # noqa: E501
        """NflOddsTeamGameTrends - a model defined in Swagger"""  # noqa: E501
        self._scope = None
        self._team_id = None
        self._team = None
        self._opponent_id = None
        self._opponent = None
        self._wins = None
        self._losses = None
        self._ties = None
        self._wins_against_the_spread = None
        self._losses_against_the_spread = None
        self._pushes_against_the_spread = None
        self._overs = None
        self._unders = None
        self._over_under_pushes = None
        self._average_score = None
        self._average_opponent_score = None
        self.discriminator = None
        if scope is not None:
            self.scope = scope
        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if opponent_id is not None:
            self.opponent_id = opponent_id
        if opponent is not None:
            self.opponent = opponent
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ties is not None:
            self.ties = ties
        if wins_against_the_spread is not None:
            self.wins_against_the_spread = wins_against_the_spread
        if losses_against_the_spread is not None:
            self.losses_against_the_spread = losses_against_the_spread
        if pushes_against_the_spread is not None:
            self.pushes_against_the_spread = pushes_against_the_spread
        if overs is not None:
            self.overs = overs
        if unders is not None:
            self.unders = unders
        if over_under_pushes is not None:
            self.over_under_pushes = over_under_pushes
        if average_score is not None:
            self.average_score = average_score
        if average_opponent_score is not None:
            self.average_opponent_score = average_opponent_score

    @property
    def scope(self):
        """Gets the scope of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The scope of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this NflOddsTeamGameTrends.


        :param scope: The scope of this NflOddsTeamGameTrends.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def team_id(self):
        """Gets the team_id of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The team_id of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NflOddsTeamGameTrends.


        :param team_id: The team_id of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The team of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this NflOddsTeamGameTrends.


        :param team: The team of this NflOddsTeamGameTrends.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opponent_id(self):
        """Gets the opponent_id of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The opponent_id of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._opponent_id

    @opponent_id.setter
    def opponent_id(self, opponent_id):
        """Sets the opponent_id of this NflOddsTeamGameTrends.


        :param opponent_id: The opponent_id of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._opponent_id = opponent_id

    @property
    def opponent(self):
        """Gets the opponent of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The opponent of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this NflOddsTeamGameTrends.


        :param opponent: The opponent of this NflOddsTeamGameTrends.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def wins(self):
        """Gets the wins of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The wins of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this NflOddsTeamGameTrends.


        :param wins: The wins of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The losses of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this NflOddsTeamGameTrends.


        :param losses: The losses of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def ties(self):
        """Gets the ties of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The ties of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """Sets the ties of this NflOddsTeamGameTrends.


        :param ties: The ties of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._ties = ties

    @property
    def wins_against_the_spread(self):
        """Gets the wins_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The wins_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._wins_against_the_spread

    @wins_against_the_spread.setter
    def wins_against_the_spread(self, wins_against_the_spread):
        """Sets the wins_against_the_spread of this NflOddsTeamGameTrends.


        :param wins_against_the_spread: The wins_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._wins_against_the_spread = wins_against_the_spread

    @property
    def losses_against_the_spread(self):
        """Gets the losses_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The losses_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._losses_against_the_spread

    @losses_against_the_spread.setter
    def losses_against_the_spread(self, losses_against_the_spread):
        """Sets the losses_against_the_spread of this NflOddsTeamGameTrends.


        :param losses_against_the_spread: The losses_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._losses_against_the_spread = losses_against_the_spread

    @property
    def pushes_against_the_spread(self):
        """Gets the pushes_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The pushes_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._pushes_against_the_spread

    @pushes_against_the_spread.setter
    def pushes_against_the_spread(self, pushes_against_the_spread):
        """Sets the pushes_against_the_spread of this NflOddsTeamGameTrends.


        :param pushes_against_the_spread: The pushes_against_the_spread of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._pushes_against_the_spread = pushes_against_the_spread

    @property
    def overs(self):
        """Gets the overs of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The overs of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._overs

    @overs.setter
    def overs(self, overs):
        """Sets the overs of this NflOddsTeamGameTrends.


        :param overs: The overs of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._overs = overs

    @property
    def unders(self):
        """Gets the unders of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The unders of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._unders

    @unders.setter
    def unders(self, unders):
        """Sets the unders of this NflOddsTeamGameTrends.


        :param unders: The unders of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._unders = unders

    @property
    def over_under_pushes(self):
        """Gets the over_under_pushes of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The over_under_pushes of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: int
        """
        return self._over_under_pushes

    @over_under_pushes.setter
    def over_under_pushes(self, over_under_pushes):
        """Sets the over_under_pushes of this NflOddsTeamGameTrends.


        :param over_under_pushes: The over_under_pushes of this NflOddsTeamGameTrends.  # noqa: E501
        :type: int
        """

        self._over_under_pushes = over_under_pushes

    @property
    def average_score(self):
        """Gets the average_score of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The average_score of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: float
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score):
        """Sets the average_score of this NflOddsTeamGameTrends.


        :param average_score: The average_score of this NflOddsTeamGameTrends.  # noqa: E501
        :type: float
        """

        self._average_score = average_score

    @property
    def average_opponent_score(self):
        """Gets the average_opponent_score of this NflOddsTeamGameTrends.  # noqa: E501


        :return: The average_opponent_score of this NflOddsTeamGameTrends.  # noqa: E501
        :rtype: float
        """
        return self._average_opponent_score

    @average_opponent_score.setter
    def average_opponent_score(self, average_opponent_score):
        """Sets the average_opponent_score of this NflOddsTeamGameTrends.


        :param average_opponent_score: The average_opponent_score of this NflOddsTeamGameTrends.  # noqa: E501
        :type: float
        """

        self._average_opponent_score = average_opponent_score

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
        if issubclass(NflOddsTeamGameTrends, dict):
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
        if not isinstance(other, NflOddsTeamGameTrends):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
