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

class SoccerStatsCompetitionDetail(object):
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
        'current_season': 'SoccerStatsSeason',
        'teams': 'list[SoccerStatsTeamDetail]',
        'games': 'list[SoccerStatsGame]',
        'competition_id': 'int',
        'area_id': 'int',
        'area_name': 'str',
        'name': 'str',
        'gender': 'str',
        'type': 'str',
        'format': 'str',
        'seasons': 'list[SoccerStatsSeason]',
        'key': 'str'
    }

    attribute_map = {
        'current_season': 'CurrentSeason',
        'teams': 'Teams',
        'games': 'Games',
        'competition_id': 'CompetitionId',
        'area_id': 'AreaId',
        'area_name': 'AreaName',
        'name': 'Name',
        'gender': 'Gender',
        'type': 'Type',
        'format': 'Format',
        'seasons': 'Seasons',
        'key': 'Key'
    }

    def __init__(self, current_season=None, teams=None, games=None, competition_id=None, area_id=None, area_name=None, name=None, gender=None, type=None, format=None, seasons=None, key=None):  # noqa: E501
        """SoccerStatsCompetitionDetail - a model defined in Swagger"""  # noqa: E501
        self._current_season = None
        self._teams = None
        self._games = None
        self._competition_id = None
        self._area_id = None
        self._area_name = None
        self._name = None
        self._gender = None
        self._type = None
        self._format = None
        self._seasons = None
        self._key = None
        self.discriminator = None
        if current_season is not None:
            self.current_season = current_season
        if teams is not None:
            self.teams = teams
        if games is not None:
            self.games = games
        if competition_id is not None:
            self.competition_id = competition_id
        if area_id is not None:
            self.area_id = area_id
        if area_name is not None:
            self.area_name = area_name
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender
        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if seasons is not None:
            self.seasons = seasons
        if key is not None:
            self.key = key

    @property
    def current_season(self):
        """Gets the current_season of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The current_season of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: SoccerStatsSeason
        """
        return self._current_season

    @current_season.setter
    def current_season(self, current_season):
        """Sets the current_season of this SoccerStatsCompetitionDetail.


        :param current_season: The current_season of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: SoccerStatsSeason
        """

        self._current_season = current_season

    @property
    def teams(self):
        """Gets the teams of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The teams of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: list[SoccerStatsTeamDetail]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this SoccerStatsCompetitionDetail.


        :param teams: The teams of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: list[SoccerStatsTeamDetail]
        """

        self._teams = teams

    @property
    def games(self):
        """Gets the games of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The games of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: list[SoccerStatsGame]
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this SoccerStatsCompetitionDetail.


        :param games: The games of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: list[SoccerStatsGame]
        """

        self._games = games

    @property
    def competition_id(self):
        """Gets the competition_id of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The competition_id of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: int
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this SoccerStatsCompetitionDetail.


        :param competition_id: The competition_id of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: int
        """

        self._competition_id = competition_id

    @property
    def area_id(self):
        """Gets the area_id of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The area_id of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this SoccerStatsCompetitionDetail.


        :param area_id: The area_id of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: int
        """

        self._area_id = area_id

    @property
    def area_name(self):
        """Gets the area_name of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The area_name of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this SoccerStatsCompetitionDetail.


        :param area_name: The area_name of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._area_name = area_name

    @property
    def name(self):
        """Gets the name of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The name of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoccerStatsCompetitionDetail.


        :param name: The name of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def gender(self):
        """Gets the gender of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The gender of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SoccerStatsCompetitionDetail.


        :param gender: The gender of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def type(self):
        """Gets the type of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The type of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoccerStatsCompetitionDetail.


        :param type: The type of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """Gets the format of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The format of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SoccerStatsCompetitionDetail.


        :param format: The format of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def seasons(self):
        """Gets the seasons of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The seasons of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: list[SoccerStatsSeason]
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this SoccerStatsCompetitionDetail.


        :param seasons: The seasons of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: list[SoccerStatsSeason]
        """

        self._seasons = seasons

    @property
    def key(self):
        """Gets the key of this SoccerStatsCompetitionDetail.  # noqa: E501


        :return: The key of this SoccerStatsCompetitionDetail.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SoccerStatsCompetitionDetail.


        :param key: The key of this SoccerStatsCompetitionDetail.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(SoccerStatsCompetitionDetail, dict):
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
        if not isinstance(other, SoccerStatsCompetitionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
