# coding: utf-8

"""
    NFL v3 Stats

    NFL rosters, player stats, team stats, and fantasy stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflStatsDailyFantasyScoring(object):
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
        'name': 'str',
        'team': 'str',
        'position': 'str',
        'fantasy_points': 'float',
        'fantasy_points_ppr': 'float',
        'fantasy_points_fan_duel': 'float',
        'fantasy_points_draft_kings': 'float',
        'fantasy_points_yahoo': 'float',
        'has_started': 'bool',
        'is_in_progress': 'bool',
        'is_over': 'bool',
        '_date': 'str',
        'fantasy_points_fantasy_draft': 'float'
    }

    attribute_map = {
        'player_id': 'PlayerID',
        'name': 'Name',
        'team': 'Team',
        'position': 'Position',
        'fantasy_points': 'FantasyPoints',
        'fantasy_points_ppr': 'FantasyPointsPPR',
        'fantasy_points_fan_duel': 'FantasyPointsFanDuel',
        'fantasy_points_draft_kings': 'FantasyPointsDraftKings',
        'fantasy_points_yahoo': 'FantasyPointsYahoo',
        'has_started': 'HasStarted',
        'is_in_progress': 'IsInProgress',
        'is_over': 'IsOver',
        '_date': 'Date',
        'fantasy_points_fantasy_draft': 'FantasyPointsFantasyDraft'
    }

    def __init__(self, player_id=None, name=None, team=None, position=None, fantasy_points=None, fantasy_points_ppr=None, fantasy_points_fan_duel=None, fantasy_points_draft_kings=None, fantasy_points_yahoo=None, has_started=None, is_in_progress=None, is_over=None, _date=None, fantasy_points_fantasy_draft=None):  # noqa: E501
        """NflStatsDailyFantasyScoring - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._name = None
        self._team = None
        self._position = None
        self._fantasy_points = None
        self._fantasy_points_ppr = None
        self._fantasy_points_fan_duel = None
        self._fantasy_points_draft_kings = None
        self._fantasy_points_yahoo = None
        self._has_started = None
        self._is_in_progress = None
        self._is_over = None
        self.__date = None
        self._fantasy_points_fantasy_draft = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if name is not None:
            self.name = name
        if team is not None:
            self.team = team
        if position is not None:
            self.position = position
        if fantasy_points is not None:
            self.fantasy_points = fantasy_points
        if fantasy_points_ppr is not None:
            self.fantasy_points_ppr = fantasy_points_ppr
        if fantasy_points_fan_duel is not None:
            self.fantasy_points_fan_duel = fantasy_points_fan_duel
        if fantasy_points_draft_kings is not None:
            self.fantasy_points_draft_kings = fantasy_points_draft_kings
        if fantasy_points_yahoo is not None:
            self.fantasy_points_yahoo = fantasy_points_yahoo
        if has_started is not None:
            self.has_started = has_started
        if is_in_progress is not None:
            self.is_in_progress = is_in_progress
        if is_over is not None:
            self.is_over = is_over
        if _date is not None:
            self._date = _date
        if fantasy_points_fantasy_draft is not None:
            self.fantasy_points_fantasy_draft = fantasy_points_fantasy_draft

    @property
    def player_id(self):
        """Gets the player_id of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The player_id of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this NflStatsDailyFantasyScoring.


        :param player_id: The player_id of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def name(self):
        """Gets the name of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The name of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NflStatsDailyFantasyScoring.


        :param name: The name of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team(self):
        """Gets the team of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The team of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this NflStatsDailyFantasyScoring.


        :param team: The team of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def position(self):
        """Gets the position of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The position of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this NflStatsDailyFantasyScoring.


        :param position: The position of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this NflStatsDailyFantasyScoring.


        :param fantasy_points: The fantasy_points of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points = fantasy_points

    @property
    def fantasy_points_ppr(self):
        """Gets the fantasy_points_ppr of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points_ppr of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_ppr

    @fantasy_points_ppr.setter
    def fantasy_points_ppr(self, fantasy_points_ppr):
        """Sets the fantasy_points_ppr of this NflStatsDailyFantasyScoring.


        :param fantasy_points_ppr: The fantasy_points_ppr of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points_ppr = fantasy_points_ppr

    @property
    def fantasy_points_fan_duel(self):
        """Gets the fantasy_points_fan_duel of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points_fan_duel of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_fan_duel

    @fantasy_points_fan_duel.setter
    def fantasy_points_fan_duel(self, fantasy_points_fan_duel):
        """Sets the fantasy_points_fan_duel of this NflStatsDailyFantasyScoring.


        :param fantasy_points_fan_duel: The fantasy_points_fan_duel of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points_fan_duel = fantasy_points_fan_duel

    @property
    def fantasy_points_draft_kings(self):
        """Gets the fantasy_points_draft_kings of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points_draft_kings of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_draft_kings

    @fantasy_points_draft_kings.setter
    def fantasy_points_draft_kings(self, fantasy_points_draft_kings):
        """Sets the fantasy_points_draft_kings of this NflStatsDailyFantasyScoring.


        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points_draft_kings = fantasy_points_draft_kings

    @property
    def fantasy_points_yahoo(self):
        """Gets the fantasy_points_yahoo of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points_yahoo of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_yahoo

    @fantasy_points_yahoo.setter
    def fantasy_points_yahoo(self, fantasy_points_yahoo):
        """Sets the fantasy_points_yahoo of this NflStatsDailyFantasyScoring.


        :param fantasy_points_yahoo: The fantasy_points_yahoo of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points_yahoo = fantasy_points_yahoo

    @property
    def has_started(self):
        """Gets the has_started of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The has_started of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: bool
        """
        return self._has_started

    @has_started.setter
    def has_started(self, has_started):
        """Sets the has_started of this NflStatsDailyFantasyScoring.


        :param has_started: The has_started of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: bool
        """

        self._has_started = has_started

    @property
    def is_in_progress(self):
        """Gets the is_in_progress of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The is_in_progress of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_progress

    @is_in_progress.setter
    def is_in_progress(self, is_in_progress):
        """Sets the is_in_progress of this NflStatsDailyFantasyScoring.


        :param is_in_progress: The is_in_progress of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: bool
        """

        self._is_in_progress = is_in_progress

    @property
    def is_over(self):
        """Gets the is_over of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The is_over of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: bool
        """
        return self._is_over

    @is_over.setter
    def is_over(self, is_over):
        """Sets the is_over of this NflStatsDailyFantasyScoring.


        :param is_over: The is_over of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: bool
        """

        self._is_over = is_over

    @property
    def _date(self):
        """Gets the _date of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The _date of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this NflStatsDailyFantasyScoring.


        :param _date: The _date of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def fantasy_points_fantasy_draft(self):
        """Gets the fantasy_points_fantasy_draft of this NflStatsDailyFantasyScoring.  # noqa: E501


        :return: The fantasy_points_fantasy_draft of this NflStatsDailyFantasyScoring.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_fantasy_draft

    @fantasy_points_fantasy_draft.setter
    def fantasy_points_fantasy_draft(self, fantasy_points_fantasy_draft):
        """Sets the fantasy_points_fantasy_draft of this NflStatsDailyFantasyScoring.


        :param fantasy_points_fantasy_draft: The fantasy_points_fantasy_draft of this NflStatsDailyFantasyScoring.  # noqa: E501
        :type: float
        """

        self._fantasy_points_fantasy_draft = fantasy_points_fantasy_draft

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
        if issubclass(NflStatsDailyFantasyScoring, dict):
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
        if not isinstance(other, NflStatsDailyFantasyScoring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
