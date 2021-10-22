# coding: utf-8

"""
    MLB v3 Scores

    MLB scores API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbScoresStanding(object):
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
        'league': 'str',
        'division': 'str',
        'wins': 'int',
        'losses': 'int',
        'percentage': 'float',
        'division_wins': 'int',
        'division_losses': 'int',
        'games_behind': 'float',
        'last_ten_games_wins': 'int',
        'last_ten_games_losses': 'int',
        'streak': 'str',
        'league_rank': 'int',
        'division_rank': 'int',
        'wild_card_rank': 'int',
        'wild_card_games_behind': 'float',
        'home_wins': 'int',
        'home_losses': 'int',
        'away_wins': 'int',
        'away_losses': 'int',
        'day_wins': 'int',
        'day_losses': 'int',
        'night_wins': 'int',
        'night_losses': 'int',
        'runs_scored': 'int',
        'runs_against': 'int',
        'global_team_id': 'int'
    }

    attribute_map = {
        'season': 'Season',
        'season_type': 'SeasonType',
        'team_id': 'TeamID',
        'key': 'Key',
        'city': 'City',
        'name': 'Name',
        'league': 'League',
        'division': 'Division',
        'wins': 'Wins',
        'losses': 'Losses',
        'percentage': 'Percentage',
        'division_wins': 'DivisionWins',
        'division_losses': 'DivisionLosses',
        'games_behind': 'GamesBehind',
        'last_ten_games_wins': 'LastTenGamesWins',
        'last_ten_games_losses': 'LastTenGamesLosses',
        'streak': 'Streak',
        'league_rank': 'LeagueRank',
        'division_rank': 'DivisionRank',
        'wild_card_rank': 'WildCardRank',
        'wild_card_games_behind': 'WildCardGamesBehind',
        'home_wins': 'HomeWins',
        'home_losses': 'HomeLosses',
        'away_wins': 'AwayWins',
        'away_losses': 'AwayLosses',
        'day_wins': 'DayWins',
        'day_losses': 'DayLosses',
        'night_wins': 'NightWins',
        'night_losses': 'NightLosses',
        'runs_scored': 'RunsScored',
        'runs_against': 'RunsAgainst',
        'global_team_id': 'GlobalTeamID'
    }

    def __init__(self, season=None, season_type=None, team_id=None, key=None, city=None, name=None, league=None, division=None, wins=None, losses=None, percentage=None, division_wins=None, division_losses=None, games_behind=None, last_ten_games_wins=None, last_ten_games_losses=None, streak=None, league_rank=None, division_rank=None, wild_card_rank=None, wild_card_games_behind=None, home_wins=None, home_losses=None, away_wins=None, away_losses=None, day_wins=None, day_losses=None, night_wins=None, night_losses=None, runs_scored=None, runs_against=None, global_team_id=None):  # noqa: E501
        """MlbScoresStanding - a model defined in Swagger"""  # noqa: E501
        self._season = None
        self._season_type = None
        self._team_id = None
        self._key = None
        self._city = None
        self._name = None
        self._league = None
        self._division = None
        self._wins = None
        self._losses = None
        self._percentage = None
        self._division_wins = None
        self._division_losses = None
        self._games_behind = None
        self._last_ten_games_wins = None
        self._last_ten_games_losses = None
        self._streak = None
        self._league_rank = None
        self._division_rank = None
        self._wild_card_rank = None
        self._wild_card_games_behind = None
        self._home_wins = None
        self._home_losses = None
        self._away_wins = None
        self._away_losses = None
        self._day_wins = None
        self._day_losses = None
        self._night_wins = None
        self._night_losses = None
        self._runs_scored = None
        self._runs_against = None
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
        if league is not None:
            self.league = league
        if division is not None:
            self.division = division
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if percentage is not None:
            self.percentage = percentage
        if division_wins is not None:
            self.division_wins = division_wins
        if division_losses is not None:
            self.division_losses = division_losses
        if games_behind is not None:
            self.games_behind = games_behind
        if last_ten_games_wins is not None:
            self.last_ten_games_wins = last_ten_games_wins
        if last_ten_games_losses is not None:
            self.last_ten_games_losses = last_ten_games_losses
        if streak is not None:
            self.streak = streak
        if league_rank is not None:
            self.league_rank = league_rank
        if division_rank is not None:
            self.division_rank = division_rank
        if wild_card_rank is not None:
            self.wild_card_rank = wild_card_rank
        if wild_card_games_behind is not None:
            self.wild_card_games_behind = wild_card_games_behind
        if home_wins is not None:
            self.home_wins = home_wins
        if home_losses is not None:
            self.home_losses = home_losses
        if away_wins is not None:
            self.away_wins = away_wins
        if away_losses is not None:
            self.away_losses = away_losses
        if day_wins is not None:
            self.day_wins = day_wins
        if day_losses is not None:
            self.day_losses = day_losses
        if night_wins is not None:
            self.night_wins = night_wins
        if night_losses is not None:
            self.night_losses = night_losses
        if runs_scored is not None:
            self.runs_scored = runs_scored
        if runs_against is not None:
            self.runs_against = runs_against
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def season(self):
        """Gets the season of this MlbScoresStanding.  # noqa: E501


        :return: The season of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this MlbScoresStanding.


        :param season: The season of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this MlbScoresStanding.  # noqa: E501


        :return: The season_type of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this MlbScoresStanding.


        :param season_type: The season_type of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def team_id(self):
        """Gets the team_id of this MlbScoresStanding.  # noqa: E501


        :return: The team_id of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this MlbScoresStanding.


        :param team_id: The team_id of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def key(self):
        """Gets the key of this MlbScoresStanding.  # noqa: E501


        :return: The key of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MlbScoresStanding.


        :param key: The key of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def city(self):
        """Gets the city of this MlbScoresStanding.  # noqa: E501


        :return: The city of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this MlbScoresStanding.


        :param city: The city of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def name(self):
        """Gets the name of this MlbScoresStanding.  # noqa: E501


        :return: The name of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MlbScoresStanding.


        :param name: The name of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def league(self):
        """Gets the league of this MlbScoresStanding.  # noqa: E501


        :return: The league of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this MlbScoresStanding.


        :param league: The league of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._league = league

    @property
    def division(self):
        """Gets the division of this MlbScoresStanding.  # noqa: E501


        :return: The division of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this MlbScoresStanding.


        :param division: The division of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def wins(self):
        """Gets the wins of this MlbScoresStanding.  # noqa: E501


        :return: The wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this MlbScoresStanding.


        :param wins: The wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this MlbScoresStanding.  # noqa: E501


        :return: The losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this MlbScoresStanding.


        :param losses: The losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def percentage(self):
        """Gets the percentage of this MlbScoresStanding.  # noqa: E501


        :return: The percentage of this MlbScoresStanding.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this MlbScoresStanding.


        :param percentage: The percentage of this MlbScoresStanding.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def division_wins(self):
        """Gets the division_wins of this MlbScoresStanding.  # noqa: E501


        :return: The division_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_wins

    @division_wins.setter
    def division_wins(self, division_wins):
        """Sets the division_wins of this MlbScoresStanding.


        :param division_wins: The division_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._division_wins = division_wins

    @property
    def division_losses(self):
        """Gets the division_losses of this MlbScoresStanding.  # noqa: E501


        :return: The division_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_losses

    @division_losses.setter
    def division_losses(self, division_losses):
        """Sets the division_losses of this MlbScoresStanding.


        :param division_losses: The division_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._division_losses = division_losses

    @property
    def games_behind(self):
        """Gets the games_behind of this MlbScoresStanding.  # noqa: E501


        :return: The games_behind of this MlbScoresStanding.  # noqa: E501
        :rtype: float
        """
        return self._games_behind

    @games_behind.setter
    def games_behind(self, games_behind):
        """Sets the games_behind of this MlbScoresStanding.


        :param games_behind: The games_behind of this MlbScoresStanding.  # noqa: E501
        :type: float
        """

        self._games_behind = games_behind

    @property
    def last_ten_games_wins(self):
        """Gets the last_ten_games_wins of this MlbScoresStanding.  # noqa: E501


        :return: The last_ten_games_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._last_ten_games_wins

    @last_ten_games_wins.setter
    def last_ten_games_wins(self, last_ten_games_wins):
        """Sets the last_ten_games_wins of this MlbScoresStanding.


        :param last_ten_games_wins: The last_ten_games_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._last_ten_games_wins = last_ten_games_wins

    @property
    def last_ten_games_losses(self):
        """Gets the last_ten_games_losses of this MlbScoresStanding.  # noqa: E501


        :return: The last_ten_games_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._last_ten_games_losses

    @last_ten_games_losses.setter
    def last_ten_games_losses(self, last_ten_games_losses):
        """Sets the last_ten_games_losses of this MlbScoresStanding.


        :param last_ten_games_losses: The last_ten_games_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._last_ten_games_losses = last_ten_games_losses

    @property
    def streak(self):
        """Gets the streak of this MlbScoresStanding.  # noqa: E501


        :return: The streak of this MlbScoresStanding.  # noqa: E501
        :rtype: str
        """
        return self._streak

    @streak.setter
    def streak(self, streak):
        """Sets the streak of this MlbScoresStanding.


        :param streak: The streak of this MlbScoresStanding.  # noqa: E501
        :type: str
        """

        self._streak = streak

    @property
    def league_rank(self):
        """Gets the league_rank of this MlbScoresStanding.  # noqa: E501


        :return: The league_rank of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._league_rank

    @league_rank.setter
    def league_rank(self, league_rank):
        """Sets the league_rank of this MlbScoresStanding.


        :param league_rank: The league_rank of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._league_rank = league_rank

    @property
    def division_rank(self):
        """Gets the division_rank of this MlbScoresStanding.  # noqa: E501


        :return: The division_rank of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._division_rank

    @division_rank.setter
    def division_rank(self, division_rank):
        """Sets the division_rank of this MlbScoresStanding.


        :param division_rank: The division_rank of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._division_rank = division_rank

    @property
    def wild_card_rank(self):
        """Gets the wild_card_rank of this MlbScoresStanding.  # noqa: E501


        :return: The wild_card_rank of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._wild_card_rank

    @wild_card_rank.setter
    def wild_card_rank(self, wild_card_rank):
        """Sets the wild_card_rank of this MlbScoresStanding.


        :param wild_card_rank: The wild_card_rank of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._wild_card_rank = wild_card_rank

    @property
    def wild_card_games_behind(self):
        """Gets the wild_card_games_behind of this MlbScoresStanding.  # noqa: E501


        :return: The wild_card_games_behind of this MlbScoresStanding.  # noqa: E501
        :rtype: float
        """
        return self._wild_card_games_behind

    @wild_card_games_behind.setter
    def wild_card_games_behind(self, wild_card_games_behind):
        """Sets the wild_card_games_behind of this MlbScoresStanding.


        :param wild_card_games_behind: The wild_card_games_behind of this MlbScoresStanding.  # noqa: E501
        :type: float
        """

        self._wild_card_games_behind = wild_card_games_behind

    @property
    def home_wins(self):
        """Gets the home_wins of this MlbScoresStanding.  # noqa: E501


        :return: The home_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._home_wins

    @home_wins.setter
    def home_wins(self, home_wins):
        """Sets the home_wins of this MlbScoresStanding.


        :param home_wins: The home_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._home_wins = home_wins

    @property
    def home_losses(self):
        """Gets the home_losses of this MlbScoresStanding.  # noqa: E501


        :return: The home_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._home_losses

    @home_losses.setter
    def home_losses(self, home_losses):
        """Sets the home_losses of this MlbScoresStanding.


        :param home_losses: The home_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._home_losses = home_losses

    @property
    def away_wins(self):
        """Gets the away_wins of this MlbScoresStanding.  # noqa: E501


        :return: The away_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._away_wins

    @away_wins.setter
    def away_wins(self, away_wins):
        """Sets the away_wins of this MlbScoresStanding.


        :param away_wins: The away_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._away_wins = away_wins

    @property
    def away_losses(self):
        """Gets the away_losses of this MlbScoresStanding.  # noqa: E501


        :return: The away_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._away_losses

    @away_losses.setter
    def away_losses(self, away_losses):
        """Sets the away_losses of this MlbScoresStanding.


        :param away_losses: The away_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._away_losses = away_losses

    @property
    def day_wins(self):
        """Gets the day_wins of this MlbScoresStanding.  # noqa: E501


        :return: The day_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._day_wins

    @day_wins.setter
    def day_wins(self, day_wins):
        """Sets the day_wins of this MlbScoresStanding.


        :param day_wins: The day_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._day_wins = day_wins

    @property
    def day_losses(self):
        """Gets the day_losses of this MlbScoresStanding.  # noqa: E501


        :return: The day_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._day_losses

    @day_losses.setter
    def day_losses(self, day_losses):
        """Sets the day_losses of this MlbScoresStanding.


        :param day_losses: The day_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._day_losses = day_losses

    @property
    def night_wins(self):
        """Gets the night_wins of this MlbScoresStanding.  # noqa: E501


        :return: The night_wins of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._night_wins

    @night_wins.setter
    def night_wins(self, night_wins):
        """Sets the night_wins of this MlbScoresStanding.


        :param night_wins: The night_wins of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._night_wins = night_wins

    @property
    def night_losses(self):
        """Gets the night_losses of this MlbScoresStanding.  # noqa: E501


        :return: The night_losses of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._night_losses

    @night_losses.setter
    def night_losses(self, night_losses):
        """Sets the night_losses of this MlbScoresStanding.


        :param night_losses: The night_losses of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._night_losses = night_losses

    @property
    def runs_scored(self):
        """Gets the runs_scored of this MlbScoresStanding.  # noqa: E501


        :return: The runs_scored of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._runs_scored

    @runs_scored.setter
    def runs_scored(self, runs_scored):
        """Sets the runs_scored of this MlbScoresStanding.


        :param runs_scored: The runs_scored of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._runs_scored = runs_scored

    @property
    def runs_against(self):
        """Gets the runs_against of this MlbScoresStanding.  # noqa: E501


        :return: The runs_against of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._runs_against

    @runs_against.setter
    def runs_against(self, runs_against):
        """Sets the runs_against of this MlbScoresStanding.


        :param runs_against: The runs_against of this MlbScoresStanding.  # noqa: E501
        :type: int
        """

        self._runs_against = runs_against

    @property
    def global_team_id(self):
        """Gets the global_team_id of this MlbScoresStanding.  # noqa: E501


        :return: The global_team_id of this MlbScoresStanding.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this MlbScoresStanding.


        :param global_team_id: The global_team_id of this MlbScoresStanding.  # noqa: E501
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
        if issubclass(MlbScoresStanding, dict):
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
        if not isinstance(other, MlbScoresStanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
