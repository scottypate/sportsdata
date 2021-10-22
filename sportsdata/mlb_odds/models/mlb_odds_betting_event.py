# coding: utf-8

"""
    MLB v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbOddsBettingEvent(object):
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
        'betting_event_id': 'int',
        'name': 'str',
        'season': 'int',
        'betting_event_type_id': 'int',
        'betting_event_type': 'str',
        'start_date': 'str',
        'created': 'str',
        'updated': 'str',
        'game_id': 'int',
        'global_game_id': 'int',
        'game_status': 'str',
        'quarter': 'str',
        'away_team': 'str',
        'home_team': 'str',
        'away_team_id': 'int',
        'home_team_id': 'int',
        'global_away_team_id': 'int',
        'global_home_team_id': 'int',
        'away_team_score': 'int',
        'home_team_score': 'int',
        'total_score': 'int',
        'away_rotation_number': 'int',
        'home_rotation_number': 'int',
        'betting_markets': 'list[MlbOddsBettingMarket]'
    }

    attribute_map = {
        'betting_event_id': 'BettingEventID',
        'name': 'Name',
        'season': 'Season',
        'betting_event_type_id': 'BettingEventTypeID',
        'betting_event_type': 'BettingEventType',
        'start_date': 'StartDate',
        'created': 'Created',
        'updated': 'Updated',
        'game_id': 'GameID',
        'global_game_id': 'GlobalGameID',
        'game_status': 'GameStatus',
        'quarter': 'Quarter',
        'away_team': 'AwayTeam',
        'home_team': 'HomeTeam',
        'away_team_id': 'AwayTeamID',
        'home_team_id': 'HomeTeamID',
        'global_away_team_id': 'GlobalAwayTeamID',
        'global_home_team_id': 'GlobalHomeTeamID',
        'away_team_score': 'AwayTeamScore',
        'home_team_score': 'HomeTeamScore',
        'total_score': 'TotalScore',
        'away_rotation_number': 'AwayRotationNumber',
        'home_rotation_number': 'HomeRotationNumber',
        'betting_markets': 'BettingMarkets'
    }

    def __init__(self, betting_event_id=None, name=None, season=None, betting_event_type_id=None, betting_event_type=None, start_date=None, created=None, updated=None, game_id=None, global_game_id=None, game_status=None, quarter=None, away_team=None, home_team=None, away_team_id=None, home_team_id=None, global_away_team_id=None, global_home_team_id=None, away_team_score=None, home_team_score=None, total_score=None, away_rotation_number=None, home_rotation_number=None, betting_markets=None):  # noqa: E501
        """MlbOddsBettingEvent - a model defined in Swagger"""  # noqa: E501
        self._betting_event_id = None
        self._name = None
        self._season = None
        self._betting_event_type_id = None
        self._betting_event_type = None
        self._start_date = None
        self._created = None
        self._updated = None
        self._game_id = None
        self._global_game_id = None
        self._game_status = None
        self._quarter = None
        self._away_team = None
        self._home_team = None
        self._away_team_id = None
        self._home_team_id = None
        self._global_away_team_id = None
        self._global_home_team_id = None
        self._away_team_score = None
        self._home_team_score = None
        self._total_score = None
        self._away_rotation_number = None
        self._home_rotation_number = None
        self._betting_markets = None
        self.discriminator = None
        if betting_event_id is not None:
            self.betting_event_id = betting_event_id
        if name is not None:
            self.name = name
        if season is not None:
            self.season = season
        if betting_event_type_id is not None:
            self.betting_event_type_id = betting_event_type_id
        if betting_event_type is not None:
            self.betting_event_type = betting_event_type
        if start_date is not None:
            self.start_date = start_date
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if game_id is not None:
            self.game_id = game_id
        if global_game_id is not None:
            self.global_game_id = global_game_id
        if game_status is not None:
            self.game_status = game_status
        if quarter is not None:
            self.quarter = quarter
        if away_team is not None:
            self.away_team = away_team
        if home_team is not None:
            self.home_team = home_team
        if away_team_id is not None:
            self.away_team_id = away_team_id
        if home_team_id is not None:
            self.home_team_id = home_team_id
        if global_away_team_id is not None:
            self.global_away_team_id = global_away_team_id
        if global_home_team_id is not None:
            self.global_home_team_id = global_home_team_id
        if away_team_score is not None:
            self.away_team_score = away_team_score
        if home_team_score is not None:
            self.home_team_score = home_team_score
        if total_score is not None:
            self.total_score = total_score
        if away_rotation_number is not None:
            self.away_rotation_number = away_rotation_number
        if home_rotation_number is not None:
            self.home_rotation_number = home_rotation_number
        if betting_markets is not None:
            self.betting_markets = betting_markets

    @property
    def betting_event_id(self):
        """Gets the betting_event_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The betting_event_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._betting_event_id

    @betting_event_id.setter
    def betting_event_id(self, betting_event_id):
        """Sets the betting_event_id of this MlbOddsBettingEvent.


        :param betting_event_id: The betting_event_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._betting_event_id = betting_event_id

    @property
    def name(self):
        """Gets the name of this MlbOddsBettingEvent.  # noqa: E501


        :return: The name of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MlbOddsBettingEvent.


        :param name: The name of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def season(self):
        """Gets the season of this MlbOddsBettingEvent.  # noqa: E501


        :return: The season of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this MlbOddsBettingEvent.


        :param season: The season of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def betting_event_type_id(self):
        """Gets the betting_event_type_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The betting_event_type_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._betting_event_type_id

    @betting_event_type_id.setter
    def betting_event_type_id(self, betting_event_type_id):
        """Sets the betting_event_type_id of this MlbOddsBettingEvent.


        :param betting_event_type_id: The betting_event_type_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._betting_event_type_id = betting_event_type_id

    @property
    def betting_event_type(self):
        """Gets the betting_event_type of this MlbOddsBettingEvent.  # noqa: E501


        :return: The betting_event_type of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._betting_event_type

    @betting_event_type.setter
    def betting_event_type(self, betting_event_type):
        """Sets the betting_event_type of this MlbOddsBettingEvent.


        :param betting_event_type: The betting_event_type of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._betting_event_type = betting_event_type

    @property
    def start_date(self):
        """Gets the start_date of this MlbOddsBettingEvent.  # noqa: E501


        :return: The start_date of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this MlbOddsBettingEvent.


        :param start_date: The start_date of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def created(self):
        """Gets the created of this MlbOddsBettingEvent.  # noqa: E501


        :return: The created of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MlbOddsBettingEvent.


        :param created: The created of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this MlbOddsBettingEvent.  # noqa: E501


        :return: The updated of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this MlbOddsBettingEvent.


        :param updated: The updated of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def game_id(self):
        """Gets the game_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The game_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this MlbOddsBettingEvent.


        :param game_id: The game_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def global_game_id(self):
        """Gets the global_game_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The global_game_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._global_game_id

    @global_game_id.setter
    def global_game_id(self, global_game_id):
        """Sets the global_game_id of this MlbOddsBettingEvent.


        :param global_game_id: The global_game_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._global_game_id = global_game_id

    @property
    def game_status(self):
        """Gets the game_status of this MlbOddsBettingEvent.  # noqa: E501


        :return: The game_status of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._game_status

    @game_status.setter
    def game_status(self, game_status):
        """Sets the game_status of this MlbOddsBettingEvent.


        :param game_status: The game_status of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._game_status = game_status

    @property
    def quarter(self):
        """Gets the quarter of this MlbOddsBettingEvent.  # noqa: E501


        :return: The quarter of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._quarter

    @quarter.setter
    def quarter(self, quarter):
        """Sets the quarter of this MlbOddsBettingEvent.


        :param quarter: The quarter of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._quarter = quarter

    @property
    def away_team(self):
        """Gets the away_team of this MlbOddsBettingEvent.  # noqa: E501


        :return: The away_team of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this MlbOddsBettingEvent.


        :param away_team: The away_team of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def home_team(self):
        """Gets the home_team of this MlbOddsBettingEvent.  # noqa: E501


        :return: The home_team of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this MlbOddsBettingEvent.


        :param home_team: The home_team of this MlbOddsBettingEvent.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The away_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this MlbOddsBettingEvent.


        :param away_team_id: The away_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._away_team_id = away_team_id

    @property
    def home_team_id(self):
        """Gets the home_team_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The home_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this MlbOddsBettingEvent.


        :param home_team_id: The home_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._home_team_id = home_team_id

    @property
    def global_away_team_id(self):
        """Gets the global_away_team_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The global_away_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._global_away_team_id

    @global_away_team_id.setter
    def global_away_team_id(self, global_away_team_id):
        """Sets the global_away_team_id of this MlbOddsBettingEvent.


        :param global_away_team_id: The global_away_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._global_away_team_id = global_away_team_id

    @property
    def global_home_team_id(self):
        """Gets the global_home_team_id of this MlbOddsBettingEvent.  # noqa: E501


        :return: The global_home_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._global_home_team_id

    @global_home_team_id.setter
    def global_home_team_id(self, global_home_team_id):
        """Sets the global_home_team_id of this MlbOddsBettingEvent.


        :param global_home_team_id: The global_home_team_id of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._global_home_team_id = global_home_team_id

    @property
    def away_team_score(self):
        """Gets the away_team_score of this MlbOddsBettingEvent.  # noqa: E501


        :return: The away_team_score of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this MlbOddsBettingEvent.


        :param away_team_score: The away_team_score of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._away_team_score = away_team_score

    @property
    def home_team_score(self):
        """Gets the home_team_score of this MlbOddsBettingEvent.  # noqa: E501


        :return: The home_team_score of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this MlbOddsBettingEvent.


        :param home_team_score: The home_team_score of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._home_team_score = home_team_score

    @property
    def total_score(self):
        """Gets the total_score of this MlbOddsBettingEvent.  # noqa: E501


        :return: The total_score of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """Sets the total_score of this MlbOddsBettingEvent.


        :param total_score: The total_score of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._total_score = total_score

    @property
    def away_rotation_number(self):
        """Gets the away_rotation_number of this MlbOddsBettingEvent.  # noqa: E501


        :return: The away_rotation_number of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._away_rotation_number

    @away_rotation_number.setter
    def away_rotation_number(self, away_rotation_number):
        """Sets the away_rotation_number of this MlbOddsBettingEvent.


        :param away_rotation_number: The away_rotation_number of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._away_rotation_number = away_rotation_number

    @property
    def home_rotation_number(self):
        """Gets the home_rotation_number of this MlbOddsBettingEvent.  # noqa: E501


        :return: The home_rotation_number of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: int
        """
        return self._home_rotation_number

    @home_rotation_number.setter
    def home_rotation_number(self, home_rotation_number):
        """Sets the home_rotation_number of this MlbOddsBettingEvent.


        :param home_rotation_number: The home_rotation_number of this MlbOddsBettingEvent.  # noqa: E501
        :type: int
        """

        self._home_rotation_number = home_rotation_number

    @property
    def betting_markets(self):
        """Gets the betting_markets of this MlbOddsBettingEvent.  # noqa: E501


        :return: The betting_markets of this MlbOddsBettingEvent.  # noqa: E501
        :rtype: list[MlbOddsBettingMarket]
        """
        return self._betting_markets

    @betting_markets.setter
    def betting_markets(self, betting_markets):
        """Sets the betting_markets of this MlbOddsBettingEvent.


        :param betting_markets: The betting_markets of this MlbOddsBettingEvent.  # noqa: E501
        :type: list[MlbOddsBettingMarket]
        """

        self._betting_markets = betting_markets

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
        if issubclass(MlbOddsBettingEvent, dict):
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
        if not isinstance(other, MlbOddsBettingEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other