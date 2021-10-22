# coding: utf-8

"""
    NHL v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NhlStatsStanding(object):
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
        'season': 'int',
        'season_type': 'int',
        'team_id': 'int',
        'key': 'str',
        'city': 'str',
        'name': 'str',
        'conference': 'str',
        'division': 'str',
        'wins': 'int',
        'losses': 'int',
        'overtime_losses': 'int',
        'percentage': 'float',
        'conference_wins': 'int',
        'conference_losses': 'int',
        'division_wins': 'int',
        'division_losses': 'int',
        'shutout_wins': 'int',
        'conference_rank': 'int',
        'division_rank': 'int',
        'global_team_id': 'int'
    }

    attribute_map = {
        'season': 'Season',
        'season_type': 'SeasonType',
        'team_id': 'TeamID',
        'key': 'Key',
        'city': 'City',
        'name': 'Name',
        'conference': 'Conference',
        'division': 'Division',
        'wins': 'Wins',
        'losses': 'Losses',
        'overtime_losses': 'OvertimeLosses',
        'percentage': 'Percentage',
        'conference_wins': 'ConferenceWins',
        'conference_losses': 'ConferenceLosses',
        'division_wins': 'DivisionWins',
        'division_losses': 'DivisionLosses',
        'shutout_wins': 'ShutoutWins',
        'conference_rank': 'ConferenceRank',
        'division_rank': 'DivisionRank',
        'global_team_id': 'GlobalTeamID'
    }

    def __init__(self, season=None, season_type=None, team_id=None, key=None, city=None, name=None, conference=None, division=None, wins=None, losses=None, overtime_losses=None, percentage=None, conference_wins=None, conference_losses=None, division_wins=None, division_losses=None, shutout_wins=None, conference_rank=None, division_rank=None, global_team_id=None):  # noqa: E501
        """NhlStatsStanding - a model defined in Swagger"""  # noqa: E501
        self._season = None
        self._season_type = None
        self._team_id = None
        self._key = None
        self._city = None
        self._name = None
        self._conference = None
        self._division = None
        self._wins = None
        self._losses = None
        self._overtime_losses = None
        self._percentage = None
        self._conference_wins = None
        self._conference_losses = None
        self._division_wins = None
        self._division_losses = None
        self._shutout_wins = None
        self._conference_rank = None
        self._division_rank = None
        self._global_team_id = None
        self.discriminator = None
        if season is not None:
            self.season = season
        if season_type is not None:
            self.season_type = season_type
        if team_id is not None:
            self.team_id = team_id
        if key is not None:
            self.key = key
        if city is not None:
            self.city = city
        if name is not None:
            self.name = name
        if conference is not None:
            self.conference = conference
        if division is not None:
            self.division = division
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if overtime_losses is not None:
            self.overtime_losses = overtime_losses
        if percentage is not None:
            self.percentage = percentage
        if conference_wins is not None:
            self.conference_wins = conference_wins
        if conference_losses is not None:
            self.conference_losses = conference_losses
        if division_wins is not None:
            self.division_wins = division_wins
        if division_losses is not None:
            self.division_losses = division_losses
        if shutout_wins is not None:
            self.shutout_wins = shutout_wins
        if conference_rank is not None:
            self.conference_rank = conference_rank
        if division_rank is not None:
            self.division_rank = division_rank
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def season(self):
        """Gets the season of this NhlStatsStanding.  # noqa: E501


        :return: The season of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NhlStatsStanding.


        :param season: The season of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this NhlStatsStanding.  # noqa: E501


        :return: The season_type of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this NhlStatsStanding.


        :param season_type: The season_type of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def team_id(self):
        """Gets the team_id of this NhlStatsStanding.  # noqa: E501


        :return: The team_id of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NhlStatsStanding.


        :param team_id: The team_id of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def key(self):
        """Gets the key of this NhlStatsStanding.  # noqa: E501


        :return: The key of this NhlStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NhlStatsStanding.


        :param key: The key of this NhlStatsStanding.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def city(self):
        """Gets the city of this NhlStatsStanding.  # noqa: E501


        :return: The city of this NhlStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this NhlStatsStanding.


        :param city: The city of this NhlStatsStanding.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def name(self):
        """Gets the name of this NhlStatsStanding.  # noqa: E501


        :return: The name of this NhlStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NhlStatsStanding.


        :param name: The name of this NhlStatsStanding.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def conference(self):
        """Gets the conference of this NhlStatsStanding.  # noqa: E501


        :return: The conference of this NhlStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this NhlStatsStanding.


        :param conference: The conference of this NhlStatsStanding.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def division(self):
        """Gets the division of this NhlStatsStanding.  # noqa: E501


        :return: The division of this NhlStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this NhlStatsStanding.


        :param division: The division of this NhlStatsStanding.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def wins(self):
        """Gets the wins of this NhlStatsStanding.  # noqa: E501


        :return: The wins of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this NhlStatsStanding.


        :param wins: The wins of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this NhlStatsStanding.  # noqa: E501


        :return: The losses of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this NhlStatsStanding.


        :param losses: The losses of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def overtime_losses(self):
        """Gets the overtime_losses of this NhlStatsStanding.  # noqa: E501


        :return: The overtime_losses of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._overtime_losses

    @overtime_losses.setter
    def overtime_losses(self, overtime_losses):
        """Sets the overtime_losses of this NhlStatsStanding.


        :param overtime_losses: The overtime_losses of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._overtime_losses = overtime_losses

    @property
    def percentage(self):
        """Gets the percentage of this NhlStatsStanding.  # noqa: E501


        :return: The percentage of this NhlStatsStanding.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this NhlStatsStanding.


        :param percentage: The percentage of this NhlStatsStanding.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def conference_wins(self):
        """Gets the conference_wins of this NhlStatsStanding.  # noqa: E501


        :return: The conference_wins of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_wins

    @conference_wins.setter
    def conference_wins(self, conference_wins):
        """Sets the conference_wins of this NhlStatsStanding.


        :param conference_wins: The conference_wins of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_wins = conference_wins

    @property
    def conference_losses(self):
        """Gets the conference_losses of this NhlStatsStanding.  # noqa: E501


        :return: The conference_losses of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_losses

    @conference_losses.setter
    def conference_losses(self, conference_losses):
        """Sets the conference_losses of this NhlStatsStanding.


        :param conference_losses: The conference_losses of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_losses = conference_losses

    @property
    def division_wins(self):
        """Gets the division_wins of this NhlStatsStanding.  # noqa: E501


        :return: The division_wins of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_wins

    @division_wins.setter
    def division_wins(self, division_wins):
        """Sets the division_wins of this NhlStatsStanding.


        :param division_wins: The division_wins of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_wins = division_wins

    @property
    def division_losses(self):
        """Gets the division_losses of this NhlStatsStanding.  # noqa: E501


        :return: The division_losses of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_losses

    @division_losses.setter
    def division_losses(self, division_losses):
        """Sets the division_losses of this NhlStatsStanding.


        :param division_losses: The division_losses of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_losses = division_losses

    @property
    def shutout_wins(self):
        """Gets the shutout_wins of this NhlStatsStanding.  # noqa: E501


        :return: The shutout_wins of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._shutout_wins

    @shutout_wins.setter
    def shutout_wins(self, shutout_wins):
        """Sets the shutout_wins of this NhlStatsStanding.


        :param shutout_wins: The shutout_wins of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._shutout_wins = shutout_wins

    @property
    def conference_rank(self):
        """Gets the conference_rank of this NhlStatsStanding.  # noqa: E501


        :return: The conference_rank of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_rank

    @conference_rank.setter
    def conference_rank(self, conference_rank):
        """Sets the conference_rank of this NhlStatsStanding.


        :param conference_rank: The conference_rank of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_rank = conference_rank

    @property
    def division_rank(self):
        """Gets the division_rank of this NhlStatsStanding.  # noqa: E501


        :return: The division_rank of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_rank

    @division_rank.setter
    def division_rank(self, division_rank):
        """Sets the division_rank of this NhlStatsStanding.


        :param division_rank: The division_rank of this NhlStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_rank = division_rank

    @property
    def global_team_id(self):
        """Gets the global_team_id of this NhlStatsStanding.  # noqa: E501


        :return: The global_team_id of this NhlStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this NhlStatsStanding.


        :param global_team_id: The global_team_id of this NhlStatsStanding.  # noqa: E501
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
        if issubclass(NhlStatsStanding, dict):
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
        if not isinstance(other, NhlStatsStanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
