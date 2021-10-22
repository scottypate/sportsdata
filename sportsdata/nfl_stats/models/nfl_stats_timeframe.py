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

class NflStatsTimeframe(object):
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
        'season_type': 'int',
        'season': 'int',
        'week': 'int',
        'name': 'str',
        'short_name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'first_game_start': 'str',
        'first_game_end': 'str',
        'last_game_end': 'str',
        'has_games': 'bool',
        'has_started': 'bool',
        'has_ended': 'bool',
        'has_first_game_started': 'bool',
        'has_first_game_ended': 'bool',
        'has_last_game_ended': 'bool',
        'api_season': 'str',
        'api_week': 'str'
    }

    attribute_map = {
        'season_type': 'SeasonType',
        'season': 'Season',
        'week': 'Week',
        'name': 'Name',
        'short_name': 'ShortName',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'first_game_start': 'FirstGameStart',
        'first_game_end': 'FirstGameEnd',
        'last_game_end': 'LastGameEnd',
        'has_games': 'HasGames',
        'has_started': 'HasStarted',
        'has_ended': 'HasEnded',
        'has_first_game_started': 'HasFirstGameStarted',
        'has_first_game_ended': 'HasFirstGameEnded',
        'has_last_game_ended': 'HasLastGameEnded',
        'api_season': 'ApiSeason',
        'api_week': 'ApiWeek'
    }

    def __init__(self, season_type=None, season=None, week=None, name=None, short_name=None, start_date=None, end_date=None, first_game_start=None, first_game_end=None, last_game_end=None, has_games=None, has_started=None, has_ended=None, has_first_game_started=None, has_first_game_ended=None, has_last_game_ended=None, api_season=None, api_week=None):  # noqa: E501
        """NflStatsTimeframe - a model defined in Swagger"""  # noqa: E501
        self._season_type = None
        self._season = None
        self._week = None
        self._name = None
        self._short_name = None
        self._start_date = None
        self._end_date = None
        self._first_game_start = None
        self._first_game_end = None
        self._last_game_end = None
        self._has_games = None
        self._has_started = None
        self._has_ended = None
        self._has_first_game_started = None
        self._has_first_game_ended = None
        self._has_last_game_ended = None
        self._api_season = None
        self._api_week = None
        self.discriminator = None
        if season_type is not None:
            self.season_type = season_type
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if first_game_start is not None:
            self.first_game_start = first_game_start
        if first_game_end is not None:
            self.first_game_end = first_game_end
        if last_game_end is not None:
            self.last_game_end = last_game_end
        if has_games is not None:
            self.has_games = has_games
        if has_started is not None:
            self.has_started = has_started
        if has_ended is not None:
            self.has_ended = has_ended
        if has_first_game_started is not None:
            self.has_first_game_started = has_first_game_started
        if has_first_game_ended is not None:
            self.has_first_game_ended = has_first_game_ended
        if has_last_game_ended is not None:
            self.has_last_game_ended = has_last_game_ended
        if api_season is not None:
            self.api_season = api_season
        if api_week is not None:
            self.api_week = api_week

    @property
    def season_type(self):
        """Gets the season_type of this NflStatsTimeframe.  # noqa: E501


        :return: The season_type of this NflStatsTimeframe.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this NflStatsTimeframe.


        :param season_type: The season_type of this NflStatsTimeframe.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def season(self):
        """Gets the season of this NflStatsTimeframe.  # noqa: E501


        :return: The season of this NflStatsTimeframe.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NflStatsTimeframe.


        :param season: The season of this NflStatsTimeframe.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this NflStatsTimeframe.  # noqa: E501


        :return: The week of this NflStatsTimeframe.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this NflStatsTimeframe.


        :param week: The week of this NflStatsTimeframe.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def name(self):
        """Gets the name of this NflStatsTimeframe.  # noqa: E501


        :return: The name of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NflStatsTimeframe.


        :param name: The name of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this NflStatsTimeframe.  # noqa: E501


        :return: The short_name of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this NflStatsTimeframe.


        :param short_name: The short_name of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def start_date(self):
        """Gets the start_date of this NflStatsTimeframe.  # noqa: E501


        :return: The start_date of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NflStatsTimeframe.


        :param start_date: The start_date of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this NflStatsTimeframe.  # noqa: E501


        :return: The end_date of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this NflStatsTimeframe.


        :param end_date: The end_date of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def first_game_start(self):
        """Gets the first_game_start of this NflStatsTimeframe.  # noqa: E501


        :return: The first_game_start of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._first_game_start

    @first_game_start.setter
    def first_game_start(self, first_game_start):
        """Sets the first_game_start of this NflStatsTimeframe.


        :param first_game_start: The first_game_start of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._first_game_start = first_game_start

    @property
    def first_game_end(self):
        """Gets the first_game_end of this NflStatsTimeframe.  # noqa: E501


        :return: The first_game_end of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._first_game_end

    @first_game_end.setter
    def first_game_end(self, first_game_end):
        """Sets the first_game_end of this NflStatsTimeframe.


        :param first_game_end: The first_game_end of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._first_game_end = first_game_end

    @property
    def last_game_end(self):
        """Gets the last_game_end of this NflStatsTimeframe.  # noqa: E501


        :return: The last_game_end of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._last_game_end

    @last_game_end.setter
    def last_game_end(self, last_game_end):
        """Sets the last_game_end of this NflStatsTimeframe.


        :param last_game_end: The last_game_end of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._last_game_end = last_game_end

    @property
    def has_games(self):
        """Gets the has_games of this NflStatsTimeframe.  # noqa: E501


        :return: The has_games of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_games

    @has_games.setter
    def has_games(self, has_games):
        """Sets the has_games of this NflStatsTimeframe.


        :param has_games: The has_games of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_games = has_games

    @property
    def has_started(self):
        """Gets the has_started of this NflStatsTimeframe.  # noqa: E501


        :return: The has_started of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_started

    @has_started.setter
    def has_started(self, has_started):
        """Sets the has_started of this NflStatsTimeframe.


        :param has_started: The has_started of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_started = has_started

    @property
    def has_ended(self):
        """Gets the has_ended of this NflStatsTimeframe.  # noqa: E501


        :return: The has_ended of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_ended

    @has_ended.setter
    def has_ended(self, has_ended):
        """Sets the has_ended of this NflStatsTimeframe.


        :param has_ended: The has_ended of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_ended = has_ended

    @property
    def has_first_game_started(self):
        """Gets the has_first_game_started of this NflStatsTimeframe.  # noqa: E501


        :return: The has_first_game_started of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_first_game_started

    @has_first_game_started.setter
    def has_first_game_started(self, has_first_game_started):
        """Sets the has_first_game_started of this NflStatsTimeframe.


        :param has_first_game_started: The has_first_game_started of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_first_game_started = has_first_game_started

    @property
    def has_first_game_ended(self):
        """Gets the has_first_game_ended of this NflStatsTimeframe.  # noqa: E501


        :return: The has_first_game_ended of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_first_game_ended

    @has_first_game_ended.setter
    def has_first_game_ended(self, has_first_game_ended):
        """Sets the has_first_game_ended of this NflStatsTimeframe.


        :param has_first_game_ended: The has_first_game_ended of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_first_game_ended = has_first_game_ended

    @property
    def has_last_game_ended(self):
        """Gets the has_last_game_ended of this NflStatsTimeframe.  # noqa: E501


        :return: The has_last_game_ended of this NflStatsTimeframe.  # noqa: E501
        :rtype: bool
        """
        return self._has_last_game_ended

    @has_last_game_ended.setter
    def has_last_game_ended(self, has_last_game_ended):
        """Sets the has_last_game_ended of this NflStatsTimeframe.


        :param has_last_game_ended: The has_last_game_ended of this NflStatsTimeframe.  # noqa: E501
        :type: bool
        """

        self._has_last_game_ended = has_last_game_ended

    @property
    def api_season(self):
        """Gets the api_season of this NflStatsTimeframe.  # noqa: E501


        :return: The api_season of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._api_season

    @api_season.setter
    def api_season(self, api_season):
        """Sets the api_season of this NflStatsTimeframe.


        :param api_season: The api_season of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._api_season = api_season

    @property
    def api_week(self):
        """Gets the api_week of this NflStatsTimeframe.  # noqa: E501


        :return: The api_week of this NflStatsTimeframe.  # noqa: E501
        :rtype: str
        """
        return self._api_week

    @api_week.setter
    def api_week(self, api_week):
        """Sets the api_week of this NflStatsTimeframe.


        :param api_week: The api_week of this NflStatsTimeframe.  # noqa: E501
        :type: str
        """

        self._api_week = api_week

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
        if issubclass(NflStatsTimeframe, dict):
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
        if not isinstance(other, NflStatsTimeframe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
