# coding: utf-8

"""
    Soccer v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoccerStatsStanding(object):
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
        'standing_id': 'int',
        'round_id': 'int',
        'team_id': 'int',
        'name': 'str',
        'short_name': 'str',
        'scope': 'str',
        'order': 'int',
        'games': 'int',
        'wins': 'int',
        'losses': 'int',
        'draws': 'int',
        'goals_scored': 'int',
        'goals_against': 'int',
        'goals_differential': 'int',
        'points': 'int',
        'group': 'str',
        'global_team_id': 'int'
    }

    attribute_map = {
        'standing_id': 'StandingId',
        'round_id': 'RoundId',
        'team_id': 'TeamId',
        'name': 'Name',
        'short_name': 'ShortName',
        'scope': 'Scope',
        'order': 'Order',
        'games': 'Games',
        'wins': 'Wins',
        'losses': 'Losses',
        'draws': 'Draws',
        'goals_scored': 'GoalsScored',
        'goals_against': 'GoalsAgainst',
        'goals_differential': 'GoalsDifferential',
        'points': 'Points',
        'group': 'Group',
        'global_team_id': 'GlobalTeamID'
    }

    def __init__(self, standing_id=None, round_id=None, team_id=None, name=None, short_name=None, scope=None, order=None, games=None, wins=None, losses=None, draws=None, goals_scored=None, goals_against=None, goals_differential=None, points=None, group=None, global_team_id=None):  # noqa: E501
        """SoccerStatsStanding - a model defined in Swagger"""  # noqa: E501
        self._standing_id = None
        self._round_id = None
        self._team_id = None
        self._name = None
        self._short_name = None
        self._scope = None
        self._order = None
        self._games = None
        self._wins = None
        self._losses = None
        self._draws = None
        self._goals_scored = None
        self._goals_against = None
        self._goals_differential = None
        self._points = None
        self._group = None
        self._global_team_id = None
        self.discriminator = None
        if standing_id is not None:
            self.standing_id = standing_id
        if round_id is not None:
            self.round_id = round_id
        if team_id is not None:
            self.team_id = team_id
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if scope is not None:
            self.scope = scope
        if order is not None:
            self.order = order
        if games is not None:
            self.games = games
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if draws is not None:
            self.draws = draws
        if goals_scored is not None:
            self.goals_scored = goals_scored
        if goals_against is not None:
            self.goals_against = goals_against
        if goals_differential is not None:
            self.goals_differential = goals_differential
        if points is not None:
            self.points = points
        if group is not None:
            self.group = group
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def standing_id(self):
        """Gets the standing_id of this SoccerStatsStanding.  # noqa: E501


        :return: The standing_id of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._standing_id

    @standing_id.setter
    def standing_id(self, standing_id):
        """Sets the standing_id of this SoccerStatsStanding.


        :param standing_id: The standing_id of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._standing_id = standing_id

    @property
    def round_id(self):
        """Gets the round_id of this SoccerStatsStanding.  # noqa: E501


        :return: The round_id of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this SoccerStatsStanding.


        :param round_id: The round_id of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._round_id = round_id

    @property
    def team_id(self):
        """Gets the team_id of this SoccerStatsStanding.  # noqa: E501


        :return: The team_id of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this SoccerStatsStanding.


        :param team_id: The team_id of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def name(self):
        """Gets the name of this SoccerStatsStanding.  # noqa: E501


        :return: The name of this SoccerStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoccerStatsStanding.


        :param name: The name of this SoccerStatsStanding.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this SoccerStatsStanding.  # noqa: E501


        :return: The short_name of this SoccerStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this SoccerStatsStanding.


        :param short_name: The short_name of this SoccerStatsStanding.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def scope(self):
        """Gets the scope of this SoccerStatsStanding.  # noqa: E501


        :return: The scope of this SoccerStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SoccerStatsStanding.


        :param scope: The scope of this SoccerStatsStanding.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def order(self):
        """Gets the order of this SoccerStatsStanding.  # noqa: E501


        :return: The order of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this SoccerStatsStanding.


        :param order: The order of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def games(self):
        """Gets the games of this SoccerStatsStanding.  # noqa: E501


        :return: The games of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this SoccerStatsStanding.


        :param games: The games of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._games = games

    @property
    def wins(self):
        """Gets the wins of this SoccerStatsStanding.  # noqa: E501


        :return: The wins of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this SoccerStatsStanding.


        :param wins: The wins of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this SoccerStatsStanding.  # noqa: E501


        :return: The losses of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this SoccerStatsStanding.


        :param losses: The losses of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def draws(self):
        """Gets the draws of this SoccerStatsStanding.  # noqa: E501


        :return: The draws of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._draws

    @draws.setter
    def draws(self, draws):
        """Sets the draws of this SoccerStatsStanding.


        :param draws: The draws of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._draws = draws

    @property
    def goals_scored(self):
        """Gets the goals_scored of this SoccerStatsStanding.  # noqa: E501


        :return: The goals_scored of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._goals_scored

    @goals_scored.setter
    def goals_scored(self, goals_scored):
        """Sets the goals_scored of this SoccerStatsStanding.


        :param goals_scored: The goals_scored of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._goals_scored = goals_scored

    @property
    def goals_against(self):
        """Gets the goals_against of this SoccerStatsStanding.  # noqa: E501


        :return: The goals_against of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._goals_against

    @goals_against.setter
    def goals_against(self, goals_against):
        """Sets the goals_against of this SoccerStatsStanding.


        :param goals_against: The goals_against of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._goals_against = goals_against

    @property
    def goals_differential(self):
        """Gets the goals_differential of this SoccerStatsStanding.  # noqa: E501


        :return: The goals_differential of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._goals_differential

    @goals_differential.setter
    def goals_differential(self, goals_differential):
        """Sets the goals_differential of this SoccerStatsStanding.


        :param goals_differential: The goals_differential of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._goals_differential = goals_differential

    @property
    def points(self):
        """Gets the points of this SoccerStatsStanding.  # noqa: E501


        :return: The points of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this SoccerStatsStanding.


        :param points: The points of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def group(self):
        """Gets the group of this SoccerStatsStanding.  # noqa: E501


        :return: The group of this SoccerStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SoccerStatsStanding.


        :param group: The group of this SoccerStatsStanding.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def global_team_id(self):
        """Gets the global_team_id of this SoccerStatsStanding.  # noqa: E501


        :return: The global_team_id of this SoccerStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this SoccerStatsStanding.


        :param global_team_id: The global_team_id of this SoccerStatsStanding.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

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
        if issubclass(SoccerStatsStanding, dict):
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
        if not isinstance(other, SoccerStatsStanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other