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

class NbaOddsGameBettingSplit(object):
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
        'game_id': 'int',
        'season_type': 'int',
        'season': 'int',
        'day': 'str',
        'away_team': 'str',
        'home_team': 'str',
        'betting_market_splits': 'list[NbaOddsBettingMarketSplit]'
    }

    attribute_map = {
        'game_id': 'GameID',
        'season_type': 'SeasonType',
        'season': 'Season',
        'day': 'Day',
        'away_team': 'AwayTeam',
        'home_team': 'HomeTeam',
        'betting_market_splits': 'BettingMarketSplits'
    }

    def __init__(self, game_id=None, season_type=None, season=None, day=None, away_team=None, home_team=None, betting_market_splits=None):  # noqa: E501
        """NbaOddsGameBettingSplit - a model defined in Swagger"""  # noqa: E501
        self._game_id = None
        self._season_type = None
        self._season = None
        self._day = None
        self._away_team = None
        self._home_team = None
        self._betting_market_splits = None
        self.discriminator = None
        if game_id is not None:
            self.game_id = game_id
        if season_type is not None:
            self.season_type = season_type
        if season is not None:
            self.season = season
        if day is not None:
            self.day = day
        if away_team is not None:
            self.away_team = away_team
        if home_team is not None:
            self.home_team = home_team
        if betting_market_splits is not None:
            self.betting_market_splits = betting_market_splits

    @property
    def game_id(self):
        """Gets the game_id of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The game_id of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this NbaOddsGameBettingSplit.


        :param game_id: The game_id of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def season_type(self):
        """Gets the season_type of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The season_type of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this NbaOddsGameBettingSplit.


        :param season_type: The season_type of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def season(self):
        """Gets the season of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The season of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NbaOddsGameBettingSplit.


        :param season: The season of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def day(self):
        """Gets the day of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The day of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this NbaOddsGameBettingSplit.


        :param day: The day of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def away_team(self):
        """Gets the away_team of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The away_team of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this NbaOddsGameBettingSplit.


        :param away_team: The away_team of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def home_team(self):
        """Gets the home_team of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The home_team of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this NbaOddsGameBettingSplit.


        :param home_team: The home_team of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def betting_market_splits(self):
        """Gets the betting_market_splits of this NbaOddsGameBettingSplit.  # noqa: E501


        :return: The betting_market_splits of this NbaOddsGameBettingSplit.  # noqa: E501
        :rtype: list[NbaOddsBettingMarketSplit]
        """
        return self._betting_market_splits

    @betting_market_splits.setter
    def betting_market_splits(self, betting_market_splits):
        """Sets the betting_market_splits of this NbaOddsGameBettingSplit.


        :param betting_market_splits: The betting_market_splits of this NbaOddsGameBettingSplit.  # noqa: E501
        :type: list[NbaOddsBettingMarketSplit]
        """

        self._betting_market_splits = betting_market_splits

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
        if issubclass(NbaOddsGameBettingSplit, dict):
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
        if not isinstance(other, NbaOddsGameBettingSplit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
