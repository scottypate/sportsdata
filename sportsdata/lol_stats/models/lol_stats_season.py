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

class LolStatsSeason(object):
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
        'season_id': 'int',
        'competition_id': 'int',
        'season': 'int',
        'name': 'str',
        'competition_name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'current_season': 'bool',
        'rounds': 'list[LolStatsRound]'
    }

    attribute_map = {
        'season_id': 'SeasonId',
        'competition_id': 'CompetitionId',
        'season': 'Season',
        'name': 'Name',
        'competition_name': 'CompetitionName',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'current_season': 'CurrentSeason',
        'rounds': 'Rounds'
    }

    def __init__(self, season_id=None, competition_id=None, season=None, name=None, competition_name=None, start_date=None, end_date=None, current_season=None, rounds=None):  # noqa: E501
        """LolStatsSeason - a model defined in Swagger"""  # noqa: E501
        self._season_id = None
        self._competition_id = None
        self._season = None
        self._name = None
        self._competition_name = None
        self._start_date = None
        self._end_date = None
        self._current_season = None
        self._rounds = None
        self.discriminator = None
        if season_id is not None:
            self.season_id = season_id
        if competition_id is not None:
            self.competition_id = competition_id
        if season is not None:
            self.season = season
        if name is not None:
            self.name = name
        if competition_name is not None:
            self.competition_name = competition_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if current_season is not None:
            self.current_season = current_season
        if rounds is not None:
            self.rounds = rounds

    @property
    def season_id(self):
        """Gets the season_id of this LolStatsSeason.  # noqa: E501


        :return: The season_id of this LolStatsSeason.  # noqa: E501
        :rtype: int
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id):
        """Sets the season_id of this LolStatsSeason.


        :param season_id: The season_id of this LolStatsSeason.  # noqa: E501
        :type: int
        """

        self._season_id = season_id

    @property
    def competition_id(self):
        """Gets the competition_id of this LolStatsSeason.  # noqa: E501


        :return: The competition_id of this LolStatsSeason.  # noqa: E501
        :rtype: int
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this LolStatsSeason.


        :param competition_id: The competition_id of this LolStatsSeason.  # noqa: E501
        :type: int
        """

        self._competition_id = competition_id

    @property
    def season(self):
        """Gets the season of this LolStatsSeason.  # noqa: E501


        :return: The season of this LolStatsSeason.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this LolStatsSeason.


        :param season: The season of this LolStatsSeason.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def name(self):
        """Gets the name of this LolStatsSeason.  # noqa: E501


        :return: The name of this LolStatsSeason.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LolStatsSeason.


        :param name: The name of this LolStatsSeason.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def competition_name(self):
        """Gets the competition_name of this LolStatsSeason.  # noqa: E501


        :return: The competition_name of this LolStatsSeason.  # noqa: E501
        :rtype: str
        """
        return self._competition_name

    @competition_name.setter
    def competition_name(self, competition_name):
        """Sets the competition_name of this LolStatsSeason.


        :param competition_name: The competition_name of this LolStatsSeason.  # noqa: E501
        :type: str
        """

        self._competition_name = competition_name

    @property
    def start_date(self):
        """Gets the start_date of this LolStatsSeason.  # noqa: E501


        :return: The start_date of this LolStatsSeason.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LolStatsSeason.


        :param start_date: The start_date of this LolStatsSeason.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this LolStatsSeason.  # noqa: E501


        :return: The end_date of this LolStatsSeason.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this LolStatsSeason.


        :param end_date: The end_date of this LolStatsSeason.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def current_season(self):
        """Gets the current_season of this LolStatsSeason.  # noqa: E501


        :return: The current_season of this LolStatsSeason.  # noqa: E501
        :rtype: bool
        """
        return self._current_season

    @current_season.setter
    def current_season(self, current_season):
        """Sets the current_season of this LolStatsSeason.


        :param current_season: The current_season of this LolStatsSeason.  # noqa: E501
        :type: bool
        """

        self._current_season = current_season

    @property
    def rounds(self):
        """Gets the rounds of this LolStatsSeason.  # noqa: E501


        :return: The rounds of this LolStatsSeason.  # noqa: E501
        :rtype: list[LolStatsRound]
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        """Sets the rounds of this LolStatsSeason.


        :param rounds: The rounds of this LolStatsSeason.  # noqa: E501
        :type: list[LolStatsRound]
        """

        self._rounds = rounds

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
        if issubclass(LolStatsSeason, dict):
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
        if not isinstance(other, LolStatsSeason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
