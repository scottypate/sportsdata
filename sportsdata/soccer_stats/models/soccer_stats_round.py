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

class SoccerStatsRound(object):
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
        'round_id': 'int',
        'season_id': 'int',
        'season': 'int',
        'season_type': 'int',
        'name': 'str',
        'type': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'current_week': 'int',
        'current_round': 'bool'
    }

    attribute_map = {
        'round_id': 'RoundId',
        'season_id': 'SeasonId',
        'season': 'Season',
        'season_type': 'SeasonType',
        'name': 'Name',
        'type': 'Type',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'current_week': 'CurrentWeek',
        'current_round': 'CurrentRound'
    }

    def __init__(self, round_id=None, season_id=None, season=None, season_type=None, name=None, type=None, start_date=None, end_date=None, current_week=None, current_round=None):  # noqa: E501
        """SoccerStatsRound - a model defined in Swagger"""  # noqa: E501
        self._round_id = None
        self._season_id = None
        self._season = None
        self._season_type = None
        self._name = None
        self._type = None
        self._start_date = None
        self._end_date = None
        self._current_week = None
        self._current_round = None
        self.discriminator = None
        if round_id is not None:
            self.round_id = round_id
        if season_id is not None:
            self.season_id = season_id
        if season is not None:
            self.season = season
        if season_type is not None:
            self.season_type = season_type
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if current_week is not None:
            self.current_week = current_week
        if current_round is not None:
            self.current_round = current_round

    @property
    def round_id(self):
        """Gets the round_id of this SoccerStatsRound.  # noqa: E501


        :return: The round_id of this SoccerStatsRound.  # noqa: E501
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this SoccerStatsRound.


        :param round_id: The round_id of this SoccerStatsRound.  # noqa: E501
        :type: int
        """

        self._round_id = round_id

    @property
    def season_id(self):
        """Gets the season_id of this SoccerStatsRound.  # noqa: E501


        :return: The season_id of this SoccerStatsRound.  # noqa: E501
        :rtype: int
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id):
        """Sets the season_id of this SoccerStatsRound.


        :param season_id: The season_id of this SoccerStatsRound.  # noqa: E501
        :type: int
        """

        self._season_id = season_id

    @property
    def season(self):
        """Gets the season of this SoccerStatsRound.  # noqa: E501


        :return: The season of this SoccerStatsRound.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this SoccerStatsRound.


        :param season: The season of this SoccerStatsRound.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this SoccerStatsRound.  # noqa: E501


        :return: The season_type of this SoccerStatsRound.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this SoccerStatsRound.


        :param season_type: The season_type of this SoccerStatsRound.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def name(self):
        """Gets the name of this SoccerStatsRound.  # noqa: E501


        :return: The name of this SoccerStatsRound.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoccerStatsRound.


        :param name: The name of this SoccerStatsRound.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SoccerStatsRound.  # noqa: E501


        :return: The type of this SoccerStatsRound.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoccerStatsRound.


        :param type: The type of this SoccerStatsRound.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def start_date(self):
        """Gets the start_date of this SoccerStatsRound.  # noqa: E501


        :return: The start_date of this SoccerStatsRound.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SoccerStatsRound.


        :param start_date: The start_date of this SoccerStatsRound.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SoccerStatsRound.  # noqa: E501


        :return: The end_date of this SoccerStatsRound.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SoccerStatsRound.


        :param end_date: The end_date of this SoccerStatsRound.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def current_week(self):
        """Gets the current_week of this SoccerStatsRound.  # noqa: E501


        :return: The current_week of this SoccerStatsRound.  # noqa: E501
        :rtype: int
        """
        return self._current_week

    @current_week.setter
    def current_week(self, current_week):
        """Sets the current_week of this SoccerStatsRound.


        :param current_week: The current_week of this SoccerStatsRound.  # noqa: E501
        :type: int
        """

        self._current_week = current_week

    @property
    def current_round(self):
        """Gets the current_round of this SoccerStatsRound.  # noqa: E501


        :return: The current_round of this SoccerStatsRound.  # noqa: E501
        :rtype: bool
        """
        return self._current_round

    @current_round.setter
    def current_round(self, current_round):
        """Sets the current_round of this SoccerStatsRound.


        :param current_round: The current_round of this SoccerStatsRound.  # noqa: E501
        :type: bool
        """

        self._current_round = current_round

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
        if issubclass(SoccerStatsRound, dict):
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
        if not isinstance(other, SoccerStatsRound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
