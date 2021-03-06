# coding: utf-8

"""
    CS:GO v3 Scores

    CS:GO v3 Scores  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CsgoScoresGame(object):
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
        'round_id': 'int',
        'season': 'int',
        'season_type': 'int',
        'group': 'str',
        'team_a_id': 'int',
        'team_b_id': 'int',
        'venue_id': 'int',
        'day': 'str',
        'date_time': 'str',
        'status': 'str',
        'week': 'int',
        'best_of': 'str',
        'winner': 'str',
        'venue_type': 'str',
        'team_a_key': 'str',
        'team_a_name': 'str',
        'team_a_score': 'int',
        'team_b_key': 'str',
        'team_b_name': 'str',
        'team_b_score': 'int',
        'team_a_money_line': 'int',
        'team_b_money_line': 'int',
        'draw_money_line': 'int',
        'point_spread': 'float',
        'team_a_point_spread_payout': 'int',
        'team_b_point_spread_payout': 'int',
        'updated': 'str',
        'updated_utc': 'str',
        'is_closed': 'bool'
    }

    attribute_map = {
        'game_id': 'GameId',
        'round_id': 'RoundId',
        'season': 'Season',
        'season_type': 'SeasonType',
        'group': 'Group',
        'team_a_id': 'TeamAId',
        'team_b_id': 'TeamBId',
        'venue_id': 'VenueId',
        'day': 'Day',
        'date_time': 'DateTime',
        'status': 'Status',
        'week': 'Week',
        'best_of': 'BestOf',
        'winner': 'Winner',
        'venue_type': 'VenueType',
        'team_a_key': 'TeamAKey',
        'team_a_name': 'TeamAName',
        'team_a_score': 'TeamAScore',
        'team_b_key': 'TeamBKey',
        'team_b_name': 'TeamBName',
        'team_b_score': 'TeamBScore',
        'team_a_money_line': 'TeamAMoneyLine',
        'team_b_money_line': 'TeamBMoneyLine',
        'draw_money_line': 'DrawMoneyLine',
        'point_spread': 'PointSpread',
        'team_a_point_spread_payout': 'TeamAPointSpreadPayout',
        'team_b_point_spread_payout': 'TeamBPointSpreadPayout',
        'updated': 'Updated',
        'updated_utc': 'UpdatedUtc',
        'is_closed': 'IsClosed'
    }

    def __init__(self, game_id=None, round_id=None, season=None, season_type=None, group=None, team_a_id=None, team_b_id=None, venue_id=None, day=None, date_time=None, status=None, week=None, best_of=None, winner=None, venue_type=None, team_a_key=None, team_a_name=None, team_a_score=None, team_b_key=None, team_b_name=None, team_b_score=None, team_a_money_line=None, team_b_money_line=None, draw_money_line=None, point_spread=None, team_a_point_spread_payout=None, team_b_point_spread_payout=None, updated=None, updated_utc=None, is_closed=None):  # noqa: E501
        """CsgoScoresGame - a model defined in Swagger"""  # noqa: E501
        self._game_id = None
        self._round_id = None
        self._season = None
        self._season_type = None
        self._group = None
        self._team_a_id = None
        self._team_b_id = None
        self._venue_id = None
        self._day = None
        self._date_time = None
        self._status = None
        self._week = None
        self._best_of = None
        self._winner = None
        self._venue_type = None
        self._team_a_key = None
        self._team_a_name = None
        self._team_a_score = None
        self._team_b_key = None
        self._team_b_name = None
        self._team_b_score = None
        self._team_a_money_line = None
        self._team_b_money_line = None
        self._draw_money_line = None
        self._point_spread = None
        self._team_a_point_spread_payout = None
        self._team_b_point_spread_payout = None
        self._updated = None
        self._updated_utc = None
        self._is_closed = None
        self.discriminator = None
        if game_id is not None:
            self.game_id = game_id
        if round_id is not None:
            self.round_id = round_id
        if season is not None:
            self.season = season
        if season_type is not None:
            self.season_type = season_type
        if group is not None:
            self.group = group
        if team_a_id is not None:
            self.team_a_id = team_a_id
        if team_b_id is not None:
            self.team_b_id = team_b_id
        if venue_id is not None:
            self.venue_id = venue_id
        if day is not None:
            self.day = day
        if date_time is not None:
            self.date_time = date_time
        if status is not None:
            self.status = status
        if week is not None:
            self.week = week
        if best_of is not None:
            self.best_of = best_of
        if winner is not None:
            self.winner = winner
        if venue_type is not None:
            self.venue_type = venue_type
        if team_a_key is not None:
            self.team_a_key = team_a_key
        if team_a_name is not None:
            self.team_a_name = team_a_name
        if team_a_score is not None:
            self.team_a_score = team_a_score
        if team_b_key is not None:
            self.team_b_key = team_b_key
        if team_b_name is not None:
            self.team_b_name = team_b_name
        if team_b_score is not None:
            self.team_b_score = team_b_score
        if team_a_money_line is not None:
            self.team_a_money_line = team_a_money_line
        if team_b_money_line is not None:
            self.team_b_money_line = team_b_money_line
        if draw_money_line is not None:
            self.draw_money_line = draw_money_line
        if point_spread is not None:
            self.point_spread = point_spread
        if team_a_point_spread_payout is not None:
            self.team_a_point_spread_payout = team_a_point_spread_payout
        if team_b_point_spread_payout is not None:
            self.team_b_point_spread_payout = team_b_point_spread_payout
        if updated is not None:
            self.updated = updated
        if updated_utc is not None:
            self.updated_utc = updated_utc
        if is_closed is not None:
            self.is_closed = is_closed

    @property
    def game_id(self):
        """Gets the game_id of this CsgoScoresGame.  # noqa: E501


        :return: The game_id of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this CsgoScoresGame.


        :param game_id: The game_id of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def round_id(self):
        """Gets the round_id of this CsgoScoresGame.  # noqa: E501


        :return: The round_id of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this CsgoScoresGame.


        :param round_id: The round_id of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._round_id = round_id

    @property
    def season(self):
        """Gets the season of this CsgoScoresGame.  # noqa: E501


        :return: The season of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this CsgoScoresGame.


        :param season: The season of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this CsgoScoresGame.  # noqa: E501


        :return: The season_type of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this CsgoScoresGame.


        :param season_type: The season_type of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def group(self):
        """Gets the group of this CsgoScoresGame.  # noqa: E501


        :return: The group of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this CsgoScoresGame.


        :param group: The group of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def team_a_id(self):
        """Gets the team_a_id of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_id of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_a_id

    @team_a_id.setter
    def team_a_id(self, team_a_id):
        """Sets the team_a_id of this CsgoScoresGame.


        :param team_a_id: The team_a_id of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_a_id = team_a_id

    @property
    def team_b_id(self):
        """Gets the team_b_id of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_id of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_b_id

    @team_b_id.setter
    def team_b_id(self, team_b_id):
        """Sets the team_b_id of this CsgoScoresGame.


        :param team_b_id: The team_b_id of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_b_id = team_b_id

    @property
    def venue_id(self):
        """Gets the venue_id of this CsgoScoresGame.  # noqa: E501


        :return: The venue_id of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this CsgoScoresGame.


        :param venue_id: The venue_id of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._venue_id = venue_id

    @property
    def day(self):
        """Gets the day of this CsgoScoresGame.  # noqa: E501


        :return: The day of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this CsgoScoresGame.


        :param day: The day of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def date_time(self):
        """Gets the date_time of this CsgoScoresGame.  # noqa: E501


        :return: The date_time of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CsgoScoresGame.


        :param date_time: The date_time of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def status(self):
        """Gets the status of this CsgoScoresGame.  # noqa: E501


        :return: The status of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CsgoScoresGame.


        :param status: The status of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def week(self):
        """Gets the week of this CsgoScoresGame.  # noqa: E501


        :return: The week of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this CsgoScoresGame.


        :param week: The week of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def best_of(self):
        """Gets the best_of of this CsgoScoresGame.  # noqa: E501


        :return: The best_of of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of):
        """Sets the best_of of this CsgoScoresGame.


        :param best_of: The best_of of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._best_of = best_of

    @property
    def winner(self):
        """Gets the winner of this CsgoScoresGame.  # noqa: E501


        :return: The winner of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this CsgoScoresGame.


        :param winner: The winner of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._winner = winner

    @property
    def venue_type(self):
        """Gets the venue_type of this CsgoScoresGame.  # noqa: E501


        :return: The venue_type of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._venue_type

    @venue_type.setter
    def venue_type(self, venue_type):
        """Sets the venue_type of this CsgoScoresGame.


        :param venue_type: The venue_type of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._venue_type = venue_type

    @property
    def team_a_key(self):
        """Gets the team_a_key of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_key of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._team_a_key

    @team_a_key.setter
    def team_a_key(self, team_a_key):
        """Sets the team_a_key of this CsgoScoresGame.


        :param team_a_key: The team_a_key of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._team_a_key = team_a_key

    @property
    def team_a_name(self):
        """Gets the team_a_name of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_name of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._team_a_name

    @team_a_name.setter
    def team_a_name(self, team_a_name):
        """Sets the team_a_name of this CsgoScoresGame.


        :param team_a_name: The team_a_name of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._team_a_name = team_a_name

    @property
    def team_a_score(self):
        """Gets the team_a_score of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_score of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_a_score

    @team_a_score.setter
    def team_a_score(self, team_a_score):
        """Sets the team_a_score of this CsgoScoresGame.


        :param team_a_score: The team_a_score of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_a_score = team_a_score

    @property
    def team_b_key(self):
        """Gets the team_b_key of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_key of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._team_b_key

    @team_b_key.setter
    def team_b_key(self, team_b_key):
        """Sets the team_b_key of this CsgoScoresGame.


        :param team_b_key: The team_b_key of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._team_b_key = team_b_key

    @property
    def team_b_name(self):
        """Gets the team_b_name of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_name of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._team_b_name

    @team_b_name.setter
    def team_b_name(self, team_b_name):
        """Sets the team_b_name of this CsgoScoresGame.


        :param team_b_name: The team_b_name of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._team_b_name = team_b_name

    @property
    def team_b_score(self):
        """Gets the team_b_score of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_score of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_b_score

    @team_b_score.setter
    def team_b_score(self, team_b_score):
        """Sets the team_b_score of this CsgoScoresGame.


        :param team_b_score: The team_b_score of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_b_score = team_b_score

    @property
    def team_a_money_line(self):
        """Gets the team_a_money_line of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_money_line of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_a_money_line

    @team_a_money_line.setter
    def team_a_money_line(self, team_a_money_line):
        """Sets the team_a_money_line of this CsgoScoresGame.


        :param team_a_money_line: The team_a_money_line of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_a_money_line = team_a_money_line

    @property
    def team_b_money_line(self):
        """Gets the team_b_money_line of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_money_line of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_b_money_line

    @team_b_money_line.setter
    def team_b_money_line(self, team_b_money_line):
        """Sets the team_b_money_line of this CsgoScoresGame.


        :param team_b_money_line: The team_b_money_line of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_b_money_line = team_b_money_line

    @property
    def draw_money_line(self):
        """Gets the draw_money_line of this CsgoScoresGame.  # noqa: E501


        :return: The draw_money_line of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._draw_money_line

    @draw_money_line.setter
    def draw_money_line(self, draw_money_line):
        """Sets the draw_money_line of this CsgoScoresGame.


        :param draw_money_line: The draw_money_line of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._draw_money_line = draw_money_line

    @property
    def point_spread(self):
        """Gets the point_spread of this CsgoScoresGame.  # noqa: E501


        :return: The point_spread of this CsgoScoresGame.  # noqa: E501
        :rtype: float
        """
        return self._point_spread

    @point_spread.setter
    def point_spread(self, point_spread):
        """Sets the point_spread of this CsgoScoresGame.


        :param point_spread: The point_spread of this CsgoScoresGame.  # noqa: E501
        :type: float
        """

        self._point_spread = point_spread

    @property
    def team_a_point_spread_payout(self):
        """Gets the team_a_point_spread_payout of this CsgoScoresGame.  # noqa: E501


        :return: The team_a_point_spread_payout of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_a_point_spread_payout

    @team_a_point_spread_payout.setter
    def team_a_point_spread_payout(self, team_a_point_spread_payout):
        """Sets the team_a_point_spread_payout of this CsgoScoresGame.


        :param team_a_point_spread_payout: The team_a_point_spread_payout of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_a_point_spread_payout = team_a_point_spread_payout

    @property
    def team_b_point_spread_payout(self):
        """Gets the team_b_point_spread_payout of this CsgoScoresGame.  # noqa: E501


        :return: The team_b_point_spread_payout of this CsgoScoresGame.  # noqa: E501
        :rtype: int
        """
        return self._team_b_point_spread_payout

    @team_b_point_spread_payout.setter
    def team_b_point_spread_payout(self, team_b_point_spread_payout):
        """Sets the team_b_point_spread_payout of this CsgoScoresGame.


        :param team_b_point_spread_payout: The team_b_point_spread_payout of this CsgoScoresGame.  # noqa: E501
        :type: int
        """

        self._team_b_point_spread_payout = team_b_point_spread_payout

    @property
    def updated(self):
        """Gets the updated of this CsgoScoresGame.  # noqa: E501


        :return: The updated of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CsgoScoresGame.


        :param updated: The updated of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def updated_utc(self):
        """Gets the updated_utc of this CsgoScoresGame.  # noqa: E501


        :return: The updated_utc of this CsgoScoresGame.  # noqa: E501
        :rtype: str
        """
        return self._updated_utc

    @updated_utc.setter
    def updated_utc(self, updated_utc):
        """Sets the updated_utc of this CsgoScoresGame.


        :param updated_utc: The updated_utc of this CsgoScoresGame.  # noqa: E501
        :type: str
        """

        self._updated_utc = updated_utc

    @property
    def is_closed(self):
        """Gets the is_closed of this CsgoScoresGame.  # noqa: E501


        :return: The is_closed of this CsgoScoresGame.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this CsgoScoresGame.


        :param is_closed: The is_closed of this CsgoScoresGame.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

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
        if issubclass(CsgoScoresGame, dict):
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
        if not isinstance(other, CsgoScoresGame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
