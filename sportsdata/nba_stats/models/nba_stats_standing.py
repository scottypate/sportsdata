# coding: utf-8

"""
    NBA v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NbaStatsStanding(object):
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
        'percentage': 'float',
        'conference_wins': 'int',
        'conference_losses': 'int',
        'division_wins': 'int',
        'division_losses': 'int',
        'home_wins': 'int',
        'home_losses': 'int',
        'away_wins': 'int',
        'away_losses': 'int',
        'last_ten_wins': 'int',
        'last_ten_losses': 'int',
        'points_per_game_for': 'float',
        'points_per_game_against': 'float',
        'streak': 'int',
        'games_back': 'float',
        'streak_description': 'str',
        'global_team_id': 'int',
        'conference_rank': 'int',
        'division_rank': 'int'
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
        'percentage': 'Percentage',
        'conference_wins': 'ConferenceWins',
        'conference_losses': 'ConferenceLosses',
        'division_wins': 'DivisionWins',
        'division_losses': 'DivisionLosses',
        'home_wins': 'HomeWins',
        'home_losses': 'HomeLosses',
        'away_wins': 'AwayWins',
        'away_losses': 'AwayLosses',
        'last_ten_wins': 'LastTenWins',
        'last_ten_losses': 'LastTenLosses',
        'points_per_game_for': 'PointsPerGameFor',
        'points_per_game_against': 'PointsPerGameAgainst',
        'streak': 'Streak',
        'games_back': 'GamesBack',
        'streak_description': 'StreakDescription',
        'global_team_id': 'GlobalTeamID',
        'conference_rank': 'ConferenceRank',
        'division_rank': 'DivisionRank'
    }

    def __init__(self, season=None, season_type=None, team_id=None, key=None, city=None, name=None, conference=None, division=None, wins=None, losses=None, percentage=None, conference_wins=None, conference_losses=None, division_wins=None, division_losses=None, home_wins=None, home_losses=None, away_wins=None, away_losses=None, last_ten_wins=None, last_ten_losses=None, points_per_game_for=None, points_per_game_against=None, streak=None, games_back=None, streak_description=None, global_team_id=None, conference_rank=None, division_rank=None):  # noqa: E501
        """NbaStatsStanding - a model defined in Swagger"""  # noqa: E501
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
        self._percentage = None
        self._conference_wins = None
        self._conference_losses = None
        self._division_wins = None
        self._division_losses = None
        self._home_wins = None
        self._home_losses = None
        self._away_wins = None
        self._away_losses = None
        self._last_ten_wins = None
        self._last_ten_losses = None
        self._points_per_game_for = None
        self._points_per_game_against = None
        self._streak = None
        self._games_back = None
        self._streak_description = None
        self._global_team_id = None
        self._conference_rank = None
        self._division_rank = None
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
        if home_wins is not None:
            self.home_wins = home_wins
        if home_losses is not None:
            self.home_losses = home_losses
        if away_wins is not None:
            self.away_wins = away_wins
        if away_losses is not None:
            self.away_losses = away_losses
        if last_ten_wins is not None:
            self.last_ten_wins = last_ten_wins
        if last_ten_losses is not None:
            self.last_ten_losses = last_ten_losses
        if points_per_game_for is not None:
            self.points_per_game_for = points_per_game_for
        if points_per_game_against is not None:
            self.points_per_game_against = points_per_game_against
        if streak is not None:
            self.streak = streak
        if games_back is not None:
            self.games_back = games_back
        if streak_description is not None:
            self.streak_description = streak_description
        if global_team_id is not None:
            self.global_team_id = global_team_id
        if conference_rank is not None:
            self.conference_rank = conference_rank
        if division_rank is not None:
            self.division_rank = division_rank

    @property
    def season(self):
        """Gets the season of this NbaStatsStanding.  # noqa: E501


        :return: The season of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NbaStatsStanding.


        :param season: The season of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this NbaStatsStanding.  # noqa: E501


        :return: The season_type of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this NbaStatsStanding.


        :param season_type: The season_type of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def team_id(self):
        """Gets the team_id of this NbaStatsStanding.  # noqa: E501


        :return: The team_id of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NbaStatsStanding.


        :param team_id: The team_id of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def key(self):
        """Gets the key of this NbaStatsStanding.  # noqa: E501


        :return: The key of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NbaStatsStanding.


        :param key: The key of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def city(self):
        """Gets the city of this NbaStatsStanding.  # noqa: E501


        :return: The city of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this NbaStatsStanding.


        :param city: The city of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def name(self):
        """Gets the name of this NbaStatsStanding.  # noqa: E501


        :return: The name of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NbaStatsStanding.


        :param name: The name of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def conference(self):
        """Gets the conference of this NbaStatsStanding.  # noqa: E501


        :return: The conference of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this NbaStatsStanding.


        :param conference: The conference of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def division(self):
        """Gets the division of this NbaStatsStanding.  # noqa: E501


        :return: The division of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this NbaStatsStanding.


        :param division: The division of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def wins(self):
        """Gets the wins of this NbaStatsStanding.  # noqa: E501


        :return: The wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this NbaStatsStanding.


        :param wins: The wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this NbaStatsStanding.  # noqa: E501


        :return: The losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this NbaStatsStanding.


        :param losses: The losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def percentage(self):
        """Gets the percentage of this NbaStatsStanding.  # noqa: E501


        :return: The percentage of this NbaStatsStanding.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this NbaStatsStanding.


        :param percentage: The percentage of this NbaStatsStanding.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def conference_wins(self):
        """Gets the conference_wins of this NbaStatsStanding.  # noqa: E501


        :return: The conference_wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_wins

    @conference_wins.setter
    def conference_wins(self, conference_wins):
        """Sets the conference_wins of this NbaStatsStanding.


        :param conference_wins: The conference_wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_wins = conference_wins

    @property
    def conference_losses(self):
        """Gets the conference_losses of this NbaStatsStanding.  # noqa: E501


        :return: The conference_losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_losses

    @conference_losses.setter
    def conference_losses(self, conference_losses):
        """Sets the conference_losses of this NbaStatsStanding.


        :param conference_losses: The conference_losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_losses = conference_losses

    @property
    def division_wins(self):
        """Gets the division_wins of this NbaStatsStanding.  # noqa: E501


        :return: The division_wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_wins

    @division_wins.setter
    def division_wins(self, division_wins):
        """Sets the division_wins of this NbaStatsStanding.


        :param division_wins: The division_wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_wins = division_wins

    @property
    def division_losses(self):
        """Gets the division_losses of this NbaStatsStanding.  # noqa: E501


        :return: The division_losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_losses

    @division_losses.setter
    def division_losses(self, division_losses):
        """Sets the division_losses of this NbaStatsStanding.


        :param division_losses: The division_losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_losses = division_losses

    @property
    def home_wins(self):
        """Gets the home_wins of this NbaStatsStanding.  # noqa: E501


        :return: The home_wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._home_wins

    @home_wins.setter
    def home_wins(self, home_wins):
        """Sets the home_wins of this NbaStatsStanding.


        :param home_wins: The home_wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._home_wins = home_wins

    @property
    def home_losses(self):
        """Gets the home_losses of this NbaStatsStanding.  # noqa: E501


        :return: The home_losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._home_losses

    @home_losses.setter
    def home_losses(self, home_losses):
        """Sets the home_losses of this NbaStatsStanding.


        :param home_losses: The home_losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._home_losses = home_losses

    @property
    def away_wins(self):
        """Gets the away_wins of this NbaStatsStanding.  # noqa: E501


        :return: The away_wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._away_wins

    @away_wins.setter
    def away_wins(self, away_wins):
        """Sets the away_wins of this NbaStatsStanding.


        :param away_wins: The away_wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._away_wins = away_wins

    @property
    def away_losses(self):
        """Gets the away_losses of this NbaStatsStanding.  # noqa: E501


        :return: The away_losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._away_losses

    @away_losses.setter
    def away_losses(self, away_losses):
        """Sets the away_losses of this NbaStatsStanding.


        :param away_losses: The away_losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._away_losses = away_losses

    @property
    def last_ten_wins(self):
        """Gets the last_ten_wins of this NbaStatsStanding.  # noqa: E501


        :return: The last_ten_wins of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._last_ten_wins

    @last_ten_wins.setter
    def last_ten_wins(self, last_ten_wins):
        """Sets the last_ten_wins of this NbaStatsStanding.


        :param last_ten_wins: The last_ten_wins of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._last_ten_wins = last_ten_wins

    @property
    def last_ten_losses(self):
        """Gets the last_ten_losses of this NbaStatsStanding.  # noqa: E501


        :return: The last_ten_losses of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._last_ten_losses

    @last_ten_losses.setter
    def last_ten_losses(self, last_ten_losses):
        """Sets the last_ten_losses of this NbaStatsStanding.


        :param last_ten_losses: The last_ten_losses of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._last_ten_losses = last_ten_losses

    @property
    def points_per_game_for(self):
        """Gets the points_per_game_for of this NbaStatsStanding.  # noqa: E501


        :return: The points_per_game_for of this NbaStatsStanding.  # noqa: E501
        :rtype: float
        """
        return self._points_per_game_for

    @points_per_game_for.setter
    def points_per_game_for(self, points_per_game_for):
        """Sets the points_per_game_for of this NbaStatsStanding.


        :param points_per_game_for: The points_per_game_for of this NbaStatsStanding.  # noqa: E501
        :type: float
        """

        self._points_per_game_for = points_per_game_for

    @property
    def points_per_game_against(self):
        """Gets the points_per_game_against of this NbaStatsStanding.  # noqa: E501


        :return: The points_per_game_against of this NbaStatsStanding.  # noqa: E501
        :rtype: float
        """
        return self._points_per_game_against

    @points_per_game_against.setter
    def points_per_game_against(self, points_per_game_against):
        """Sets the points_per_game_against of this NbaStatsStanding.


        :param points_per_game_against: The points_per_game_against of this NbaStatsStanding.  # noqa: E501
        :type: float
        """

        self._points_per_game_against = points_per_game_against

    @property
    def streak(self):
        """Gets the streak of this NbaStatsStanding.  # noqa: E501


        :return: The streak of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._streak

    @streak.setter
    def streak(self, streak):
        """Sets the streak of this NbaStatsStanding.


        :param streak: The streak of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._streak = streak

    @property
    def games_back(self):
        """Gets the games_back of this NbaStatsStanding.  # noqa: E501


        :return: The games_back of this NbaStatsStanding.  # noqa: E501
        :rtype: float
        """
        return self._games_back

    @games_back.setter
    def games_back(self, games_back):
        """Sets the games_back of this NbaStatsStanding.


        :param games_back: The games_back of this NbaStatsStanding.  # noqa: E501
        :type: float
        """

        self._games_back = games_back

    @property
    def streak_description(self):
        """Gets the streak_description of this NbaStatsStanding.  # noqa: E501


        :return: The streak_description of this NbaStatsStanding.  # noqa: E501
        :rtype: str
        """
        return self._streak_description

    @streak_description.setter
    def streak_description(self, streak_description):
        """Sets the streak_description of this NbaStatsStanding.


        :param streak_description: The streak_description of this NbaStatsStanding.  # noqa: E501
        :type: str
        """

        self._streak_description = streak_description

    @property
    def global_team_id(self):
        """Gets the global_team_id of this NbaStatsStanding.  # noqa: E501


        :return: The global_team_id of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this NbaStatsStanding.


        :param global_team_id: The global_team_id of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

    @property
    def conference_rank(self):
        """Gets the conference_rank of this NbaStatsStanding.  # noqa: E501


        :return: The conference_rank of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._conference_rank

    @conference_rank.setter
    def conference_rank(self, conference_rank):
        """Sets the conference_rank of this NbaStatsStanding.


        :param conference_rank: The conference_rank of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._conference_rank = conference_rank

    @property
    def division_rank(self):
        """Gets the division_rank of this NbaStatsStanding.  # noqa: E501


        :return: The division_rank of this NbaStatsStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_rank

    @division_rank.setter
    def division_rank(self, division_rank):
        """Sets the division_rank of this NbaStatsStanding.


        :param division_rank: The division_rank of this NbaStatsStanding.  # noqa: E501
        :type: int
        """

        self._division_rank = division_rank

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
        if issubclass(NbaStatsStanding, dict):
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
        if not isinstance(other, NbaStatsStanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
