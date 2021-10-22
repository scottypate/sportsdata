# coding: utf-8

"""
    CFB v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CfbOddsGame(object):
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
        'season': 'int',
        'season_type': 'int',
        'week': 'int',
        'status': 'str',
        'day': 'str',
        'date_time': 'str',
        'away_team': 'str',
        'home_team': 'str',
        'away_team_id': 'int',
        'home_team_id': 'int',
        'away_team_name': 'str',
        'home_team_name': 'str',
        'away_team_score': 'int',
        'home_team_score': 'int',
        'period': 'str',
        'time_remaining_minutes': 'int',
        'time_remaining_seconds': 'int',
        'point_spread': 'float',
        'over_under': 'float',
        'away_team_money_line': 'int',
        'home_team_money_line': 'int',
        'updated': 'str',
        'created': 'str',
        'global_game_id': 'int',
        'global_away_team_id': 'int',
        'global_home_team_id': 'int',
        'stadium_id': 'int',
        'stadium': 'CfbOddsStadium',
        'yard_line': 'int',
        'yard_line_territory': 'str',
        'down': 'int',
        'distance': 'int',
        'possession': 'str',
        'periods': 'list[CfbOddsPeriod]',
        'is_closed': 'bool',
        'game_end_date_time': 'str',
        'title': 'str',
        'home_rotation_number': 'int',
        'away_rotation_number': 'int',
        'channel': 'str',
        'neutral_venue': 'bool',
        'away_point_spread_payout': 'int',
        'home_point_spread_payout': 'int',
        'over_payout': 'int',
        'under_payout': 'int'
    }

    attribute_map = {
        'game_id': 'GameID',
        'season': 'Season',
        'season_type': 'SeasonType',
        'week': 'Week',
        'status': 'Status',
        'day': 'Day',
        'date_time': 'DateTime',
        'away_team': 'AwayTeam',
        'home_team': 'HomeTeam',
        'away_team_id': 'AwayTeamID',
        'home_team_id': 'HomeTeamID',
        'away_team_name': 'AwayTeamName',
        'home_team_name': 'HomeTeamName',
        'away_team_score': 'AwayTeamScore',
        'home_team_score': 'HomeTeamScore',
        'period': 'Period',
        'time_remaining_minutes': 'TimeRemainingMinutes',
        'time_remaining_seconds': 'TimeRemainingSeconds',
        'point_spread': 'PointSpread',
        'over_under': 'OverUnder',
        'away_team_money_line': 'AwayTeamMoneyLine',
        'home_team_money_line': 'HomeTeamMoneyLine',
        'updated': 'Updated',
        'created': 'Created',
        'global_game_id': 'GlobalGameID',
        'global_away_team_id': 'GlobalAwayTeamID',
        'global_home_team_id': 'GlobalHomeTeamID',
        'stadium_id': 'StadiumID',
        'stadium': 'Stadium',
        'yard_line': 'YardLine',
        'yard_line_territory': 'YardLineTerritory',
        'down': 'Down',
        'distance': 'Distance',
        'possession': 'Possession',
        'periods': 'Periods',
        'is_closed': 'IsClosed',
        'game_end_date_time': 'GameEndDateTime',
        'title': 'Title',
        'home_rotation_number': 'HomeRotationNumber',
        'away_rotation_number': 'AwayRotationNumber',
        'channel': 'Channel',
        'neutral_venue': 'NeutralVenue',
        'away_point_spread_payout': 'AwayPointSpreadPayout',
        'home_point_spread_payout': 'HomePointSpreadPayout',
        'over_payout': 'OverPayout',
        'under_payout': 'UnderPayout'
    }

    def __init__(self, game_id=None, season=None, season_type=None, week=None, status=None, day=None, date_time=None, away_team=None, home_team=None, away_team_id=None, home_team_id=None, away_team_name=None, home_team_name=None, away_team_score=None, home_team_score=None, period=None, time_remaining_minutes=None, time_remaining_seconds=None, point_spread=None, over_under=None, away_team_money_line=None, home_team_money_line=None, updated=None, created=None, global_game_id=None, global_away_team_id=None, global_home_team_id=None, stadium_id=None, stadium=None, yard_line=None, yard_line_territory=None, down=None, distance=None, possession=None, periods=None, is_closed=None, game_end_date_time=None, title=None, home_rotation_number=None, away_rotation_number=None, channel=None, neutral_venue=None, away_point_spread_payout=None, home_point_spread_payout=None, over_payout=None, under_payout=None):  # noqa: E501
        """CfbOddsGame - a model defined in Swagger"""  # noqa: E501
        self._game_id = None
        self._season = None
        self._season_type = None
        self._week = None
        self._status = None
        self._day = None
        self._date_time = None
        self._away_team = None
        self._home_team = None
        self._away_team_id = None
        self._home_team_id = None
        self._away_team_name = None
        self._home_team_name = None
        self._away_team_score = None
        self._home_team_score = None
        self._period = None
        self._time_remaining_minutes = None
        self._time_remaining_seconds = None
        self._point_spread = None
        self._over_under = None
        self._away_team_money_line = None
        self._home_team_money_line = None
        self._updated = None
        self._created = None
        self._global_game_id = None
        self._global_away_team_id = None
        self._global_home_team_id = None
        self._stadium_id = None
        self._stadium = None
        self._yard_line = None
        self._yard_line_territory = None
        self._down = None
        self._distance = None
        self._possession = None
        self._periods = None
        self._is_closed = None
        self._game_end_date_time = None
        self._title = None
        self._home_rotation_number = None
        self._away_rotation_number = None
        self._channel = None
        self._neutral_venue = None
        self._away_point_spread_payout = None
        self._home_point_spread_payout = None
        self._over_payout = None
        self._under_payout = None
        self.discriminator = None
        if game_id is not None:
            self.game_id = game_id
        if season is not None:
            self.season = season
        if season_type is not None:
            self.season_type = season_type
        if week is not None:
            self.week = week
        if status is not None:
            self.status = status
        if day is not None:
            self.day = day
        if date_time is not None:
            self.date_time = date_time
        if away_team is not None:
            self.away_team = away_team
        if home_team is not None:
            self.home_team = home_team
        if away_team_id is not None:
            self.away_team_id = away_team_id
        if home_team_id is not None:
            self.home_team_id = home_team_id
        if away_team_name is not None:
            self.away_team_name = away_team_name
        if home_team_name is not None:
            self.home_team_name = home_team_name
        if away_team_score is not None:
            self.away_team_score = away_team_score
        if home_team_score is not None:
            self.home_team_score = home_team_score
        if period is not None:
            self.period = period
        if time_remaining_minutes is not None:
            self.time_remaining_minutes = time_remaining_minutes
        if time_remaining_seconds is not None:
            self.time_remaining_seconds = time_remaining_seconds
        if point_spread is not None:
            self.point_spread = point_spread
        if over_under is not None:
            self.over_under = over_under
        if away_team_money_line is not None:
            self.away_team_money_line = away_team_money_line
        if home_team_money_line is not None:
            self.home_team_money_line = home_team_money_line
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if global_game_id is not None:
            self.global_game_id = global_game_id
        if global_away_team_id is not None:
            self.global_away_team_id = global_away_team_id
        if global_home_team_id is not None:
            self.global_home_team_id = global_home_team_id
        if stadium_id is not None:
            self.stadium_id = stadium_id
        if stadium is not None:
            self.stadium = stadium
        if yard_line is not None:
            self.yard_line = yard_line
        if yard_line_territory is not None:
            self.yard_line_territory = yard_line_territory
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if possession is not None:
            self.possession = possession
        if periods is not None:
            self.periods = periods
        if is_closed is not None:
            self.is_closed = is_closed
        if game_end_date_time is not None:
            self.game_end_date_time = game_end_date_time
        if title is not None:
            self.title = title
        if home_rotation_number is not None:
            self.home_rotation_number = home_rotation_number
        if away_rotation_number is not None:
            self.away_rotation_number = away_rotation_number
        if channel is not None:
            self.channel = channel
        if neutral_venue is not None:
            self.neutral_venue = neutral_venue
        if away_point_spread_payout is not None:
            self.away_point_spread_payout = away_point_spread_payout
        if home_point_spread_payout is not None:
            self.home_point_spread_payout = home_point_spread_payout
        if over_payout is not None:
            self.over_payout = over_payout
        if under_payout is not None:
            self.under_payout = under_payout

    @property
    def game_id(self):
        """Gets the game_id of this CfbOddsGame.  # noqa: E501


        :return: The game_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this CfbOddsGame.


        :param game_id: The game_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def season(self):
        """Gets the season of this CfbOddsGame.  # noqa: E501


        :return: The season of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this CfbOddsGame.


        :param season: The season of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this CfbOddsGame.  # noqa: E501


        :return: The season_type of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this CfbOddsGame.


        :param season_type: The season_type of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def week(self):
        """Gets the week of this CfbOddsGame.  # noqa: E501


        :return: The week of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this CfbOddsGame.


        :param week: The week of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def status(self):
        """Gets the status of this CfbOddsGame.  # noqa: E501


        :return: The status of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CfbOddsGame.


        :param status: The status of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def day(self):
        """Gets the day of this CfbOddsGame.  # noqa: E501


        :return: The day of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this CfbOddsGame.


        :param day: The day of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def date_time(self):
        """Gets the date_time of this CfbOddsGame.  # noqa: E501


        :return: The date_time of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CfbOddsGame.


        :param date_time: The date_time of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def away_team(self):
        """Gets the away_team of this CfbOddsGame.  # noqa: E501


        :return: The away_team of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this CfbOddsGame.


        :param away_team: The away_team of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def home_team(self):
        """Gets the home_team of this CfbOddsGame.  # noqa: E501


        :return: The home_team of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this CfbOddsGame.


        :param home_team: The home_team of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this CfbOddsGame.  # noqa: E501


        :return: The away_team_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this CfbOddsGame.


        :param away_team_id: The away_team_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._away_team_id = away_team_id

    @property
    def home_team_id(self):
        """Gets the home_team_id of this CfbOddsGame.  # noqa: E501


        :return: The home_team_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this CfbOddsGame.


        :param home_team_id: The home_team_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._home_team_id = home_team_id

    @property
    def away_team_name(self):
        """Gets the away_team_name of this CfbOddsGame.  # noqa: E501


        :return: The away_team_name of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._away_team_name

    @away_team_name.setter
    def away_team_name(self, away_team_name):
        """Sets the away_team_name of this CfbOddsGame.


        :param away_team_name: The away_team_name of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._away_team_name = away_team_name

    @property
    def home_team_name(self):
        """Gets the home_team_name of this CfbOddsGame.  # noqa: E501


        :return: The home_team_name of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._home_team_name

    @home_team_name.setter
    def home_team_name(self, home_team_name):
        """Sets the home_team_name of this CfbOddsGame.


        :param home_team_name: The home_team_name of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._home_team_name = home_team_name

    @property
    def away_team_score(self):
        """Gets the away_team_score of this CfbOddsGame.  # noqa: E501


        :return: The away_team_score of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this CfbOddsGame.


        :param away_team_score: The away_team_score of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._away_team_score = away_team_score

    @property
    def home_team_score(self):
        """Gets the home_team_score of this CfbOddsGame.  # noqa: E501


        :return: The home_team_score of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this CfbOddsGame.


        :param home_team_score: The home_team_score of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._home_team_score = home_team_score

    @property
    def period(self):
        """Gets the period of this CfbOddsGame.  # noqa: E501


        :return: The period of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CfbOddsGame.


        :param period: The period of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def time_remaining_minutes(self):
        """Gets the time_remaining_minutes of this CfbOddsGame.  # noqa: E501


        :return: The time_remaining_minutes of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_minutes

    @time_remaining_minutes.setter
    def time_remaining_minutes(self, time_remaining_minutes):
        """Sets the time_remaining_minutes of this CfbOddsGame.


        :param time_remaining_minutes: The time_remaining_minutes of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._time_remaining_minutes = time_remaining_minutes

    @property
    def time_remaining_seconds(self):
        """Gets the time_remaining_seconds of this CfbOddsGame.  # noqa: E501


        :return: The time_remaining_seconds of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_seconds

    @time_remaining_seconds.setter
    def time_remaining_seconds(self, time_remaining_seconds):
        """Sets the time_remaining_seconds of this CfbOddsGame.


        :param time_remaining_seconds: The time_remaining_seconds of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._time_remaining_seconds = time_remaining_seconds

    @property
    def point_spread(self):
        """Gets the point_spread of this CfbOddsGame.  # noqa: E501


        :return: The point_spread of this CfbOddsGame.  # noqa: E501
        :rtype: float
        """
        return self._point_spread

    @point_spread.setter
    def point_spread(self, point_spread):
        """Sets the point_spread of this CfbOddsGame.


        :param point_spread: The point_spread of this CfbOddsGame.  # noqa: E501
        :type: float
        """

        self._point_spread = point_spread

    @property
    def over_under(self):
        """Gets the over_under of this CfbOddsGame.  # noqa: E501


        :return: The over_under of this CfbOddsGame.  # noqa: E501
        :rtype: float
        """
        return self._over_under

    @over_under.setter
    def over_under(self, over_under):
        """Sets the over_under of this CfbOddsGame.


        :param over_under: The over_under of this CfbOddsGame.  # noqa: E501
        :type: float
        """

        self._over_under = over_under

    @property
    def away_team_money_line(self):
        """Gets the away_team_money_line of this CfbOddsGame.  # noqa: E501


        :return: The away_team_money_line of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._away_team_money_line

    @away_team_money_line.setter
    def away_team_money_line(self, away_team_money_line):
        """Sets the away_team_money_line of this CfbOddsGame.


        :param away_team_money_line: The away_team_money_line of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._away_team_money_line = away_team_money_line

    @property
    def home_team_money_line(self):
        """Gets the home_team_money_line of this CfbOddsGame.  # noqa: E501


        :return: The home_team_money_line of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._home_team_money_line

    @home_team_money_line.setter
    def home_team_money_line(self, home_team_money_line):
        """Sets the home_team_money_line of this CfbOddsGame.


        :param home_team_money_line: The home_team_money_line of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._home_team_money_line = home_team_money_line

    @property
    def updated(self):
        """Gets the updated of this CfbOddsGame.  # noqa: E501


        :return: The updated of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CfbOddsGame.


        :param updated: The updated of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this CfbOddsGame.  # noqa: E501


        :return: The created of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CfbOddsGame.


        :param created: The created of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def global_game_id(self):
        """Gets the global_game_id of this CfbOddsGame.  # noqa: E501


        :return: The global_game_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._global_game_id

    @global_game_id.setter
    def global_game_id(self, global_game_id):
        """Sets the global_game_id of this CfbOddsGame.


        :param global_game_id: The global_game_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._global_game_id = global_game_id

    @property
    def global_away_team_id(self):
        """Gets the global_away_team_id of this CfbOddsGame.  # noqa: E501


        :return: The global_away_team_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._global_away_team_id

    @global_away_team_id.setter
    def global_away_team_id(self, global_away_team_id):
        """Sets the global_away_team_id of this CfbOddsGame.


        :param global_away_team_id: The global_away_team_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._global_away_team_id = global_away_team_id

    @property
    def global_home_team_id(self):
        """Gets the global_home_team_id of this CfbOddsGame.  # noqa: E501


        :return: The global_home_team_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._global_home_team_id

    @global_home_team_id.setter
    def global_home_team_id(self, global_home_team_id):
        """Sets the global_home_team_id of this CfbOddsGame.


        :param global_home_team_id: The global_home_team_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._global_home_team_id = global_home_team_id

    @property
    def stadium_id(self):
        """Gets the stadium_id of this CfbOddsGame.  # noqa: E501


        :return: The stadium_id of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._stadium_id

    @stadium_id.setter
    def stadium_id(self, stadium_id):
        """Sets the stadium_id of this CfbOddsGame.


        :param stadium_id: The stadium_id of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._stadium_id = stadium_id

    @property
    def stadium(self):
        """Gets the stadium of this CfbOddsGame.  # noqa: E501


        :return: The stadium of this CfbOddsGame.  # noqa: E501
        :rtype: CfbOddsStadium
        """
        return self._stadium

    @stadium.setter
    def stadium(self, stadium):
        """Sets the stadium of this CfbOddsGame.


        :param stadium: The stadium of this CfbOddsGame.  # noqa: E501
        :type: CfbOddsStadium
        """

        self._stadium = stadium

    @property
    def yard_line(self):
        """Gets the yard_line of this CfbOddsGame.  # noqa: E501


        :return: The yard_line of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._yard_line

    @yard_line.setter
    def yard_line(self, yard_line):
        """Sets the yard_line of this CfbOddsGame.


        :param yard_line: The yard_line of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._yard_line = yard_line

    @property
    def yard_line_territory(self):
        """Gets the yard_line_territory of this CfbOddsGame.  # noqa: E501


        :return: The yard_line_territory of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._yard_line_territory

    @yard_line_territory.setter
    def yard_line_territory(self, yard_line_territory):
        """Sets the yard_line_territory of this CfbOddsGame.


        :param yard_line_territory: The yard_line_territory of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._yard_line_territory = yard_line_territory

    @property
    def down(self):
        """Gets the down of this CfbOddsGame.  # noqa: E501


        :return: The down of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this CfbOddsGame.


        :param down: The down of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this CfbOddsGame.  # noqa: E501


        :return: The distance of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this CfbOddsGame.


        :param distance: The distance of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def possession(self):
        """Gets the possession of this CfbOddsGame.  # noqa: E501


        :return: The possession of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._possession

    @possession.setter
    def possession(self, possession):
        """Sets the possession of this CfbOddsGame.


        :param possession: The possession of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._possession = possession

    @property
    def periods(self):
        """Gets the periods of this CfbOddsGame.  # noqa: E501


        :return: The periods of this CfbOddsGame.  # noqa: E501
        :rtype: list[CfbOddsPeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this CfbOddsGame.


        :param periods: The periods of this CfbOddsGame.  # noqa: E501
        :type: list[CfbOddsPeriod]
        """

        self._periods = periods

    @property
    def is_closed(self):
        """Gets the is_closed of this CfbOddsGame.  # noqa: E501


        :return: The is_closed of this CfbOddsGame.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this CfbOddsGame.


        :param is_closed: The is_closed of this CfbOddsGame.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def game_end_date_time(self):
        """Gets the game_end_date_time of this CfbOddsGame.  # noqa: E501


        :return: The game_end_date_time of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._game_end_date_time

    @game_end_date_time.setter
    def game_end_date_time(self, game_end_date_time):
        """Sets the game_end_date_time of this CfbOddsGame.


        :param game_end_date_time: The game_end_date_time of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._game_end_date_time = game_end_date_time

    @property
    def title(self):
        """Gets the title of this CfbOddsGame.  # noqa: E501


        :return: The title of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CfbOddsGame.


        :param title: The title of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def home_rotation_number(self):
        """Gets the home_rotation_number of this CfbOddsGame.  # noqa: E501


        :return: The home_rotation_number of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._home_rotation_number

    @home_rotation_number.setter
    def home_rotation_number(self, home_rotation_number):
        """Sets the home_rotation_number of this CfbOddsGame.


        :param home_rotation_number: The home_rotation_number of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._home_rotation_number = home_rotation_number

    @property
    def away_rotation_number(self):
        """Gets the away_rotation_number of this CfbOddsGame.  # noqa: E501


        :return: The away_rotation_number of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._away_rotation_number

    @away_rotation_number.setter
    def away_rotation_number(self, away_rotation_number):
        """Sets the away_rotation_number of this CfbOddsGame.


        :param away_rotation_number: The away_rotation_number of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._away_rotation_number = away_rotation_number

    @property
    def channel(self):
        """Gets the channel of this CfbOddsGame.  # noqa: E501


        :return: The channel of this CfbOddsGame.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CfbOddsGame.


        :param channel: The channel of this CfbOddsGame.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def neutral_venue(self):
        """Gets the neutral_venue of this CfbOddsGame.  # noqa: E501


        :return: The neutral_venue of this CfbOddsGame.  # noqa: E501
        :rtype: bool
        """
        return self._neutral_venue

    @neutral_venue.setter
    def neutral_venue(self, neutral_venue):
        """Sets the neutral_venue of this CfbOddsGame.


        :param neutral_venue: The neutral_venue of this CfbOddsGame.  # noqa: E501
        :type: bool
        """

        self._neutral_venue = neutral_venue

    @property
    def away_point_spread_payout(self):
        """Gets the away_point_spread_payout of this CfbOddsGame.  # noqa: E501


        :return: The away_point_spread_payout of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._away_point_spread_payout

    @away_point_spread_payout.setter
    def away_point_spread_payout(self, away_point_spread_payout):
        """Sets the away_point_spread_payout of this CfbOddsGame.


        :param away_point_spread_payout: The away_point_spread_payout of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._away_point_spread_payout = away_point_spread_payout

    @property
    def home_point_spread_payout(self):
        """Gets the home_point_spread_payout of this CfbOddsGame.  # noqa: E501


        :return: The home_point_spread_payout of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._home_point_spread_payout

    @home_point_spread_payout.setter
    def home_point_spread_payout(self, home_point_spread_payout):
        """Sets the home_point_spread_payout of this CfbOddsGame.


        :param home_point_spread_payout: The home_point_spread_payout of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._home_point_spread_payout = home_point_spread_payout

    @property
    def over_payout(self):
        """Gets the over_payout of this CfbOddsGame.  # noqa: E501


        :return: The over_payout of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._over_payout

    @over_payout.setter
    def over_payout(self, over_payout):
        """Sets the over_payout of this CfbOddsGame.


        :param over_payout: The over_payout of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._over_payout = over_payout

    @property
    def under_payout(self):
        """Gets the under_payout of this CfbOddsGame.  # noqa: E501


        :return: The under_payout of this CfbOddsGame.  # noqa: E501
        :rtype: int
        """
        return self._under_payout

    @under_payout.setter
    def under_payout(self, under_payout):
        """Sets the under_payout of this CfbOddsGame.


        :param under_payout: The under_payout of this CfbOddsGame.  # noqa: E501
        :type: int
        """

        self._under_payout = under_payout

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
        if issubclass(CfbOddsGame, dict):
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
        if not isinstance(other, CfbOddsGame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
