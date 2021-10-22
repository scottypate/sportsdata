# coding: utf-8

"""
    NFL v3 Play-by-Play

    NFL play-by-play API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflPlayByPlayScoringPlay(object):
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
        'game_key': 'str',
        'season_type': 'int',
        'scoring_play_id': 'int',
        'season': 'int',
        'week': 'int',
        'away_team': 'str',
        'home_team': 'str',
        '_date': 'str',
        'sequence': 'int',
        'team': 'str',
        'quarter': 'str',
        'time_remaining': 'str',
        'play_description': 'str',
        'away_score': 'int',
        'home_score': 'int',
        'score_id': 'int'
    }

    attribute_map = {
        'game_key': 'GameKey',
        'season_type': 'SeasonType',
        'scoring_play_id': 'ScoringPlayID',
        'season': 'Season',
        'week': 'Week',
        'away_team': 'AwayTeam',
        'home_team': 'HomeTeam',
        '_date': 'Date',
        'sequence': 'Sequence',
        'team': 'Team',
        'quarter': 'Quarter',
        'time_remaining': 'TimeRemaining',
        'play_description': 'PlayDescription',
        'away_score': 'AwayScore',
        'home_score': 'HomeScore',
        'score_id': 'ScoreID'
    }

    def __init__(self, game_key=None, season_type=None, scoring_play_id=None, season=None, week=None, away_team=None, home_team=None, _date=None, sequence=None, team=None, quarter=None, time_remaining=None, play_description=None, away_score=None, home_score=None, score_id=None):  # noqa: E501
        """NflPlayByPlayScoringPlay - a model defined in Swagger"""  # noqa: E501
        self._game_key = None
        self._season_type = None
        self._scoring_play_id = None
        self._season = None
        self._week = None
        self._away_team = None
        self._home_team = None
        self.__date = None
        self._sequence = None
        self._team = None
        self._quarter = None
        self._time_remaining = None
        self._play_description = None
        self._away_score = None
        self._home_score = None
        self._score_id = None
        self.discriminator = None
        if game_key is not None:
            self.game_key = game_key
        if season_type is not None:
            self.season_type = season_type
        if scoring_play_id is not None:
            self.scoring_play_id = scoring_play_id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if away_team is not None:
            self.away_team = away_team
        if home_team is not None:
            self.home_team = home_team
        if _date is not None:
            self._date = _date
        if sequence is not None:
            self.sequence = sequence
        if team is not None:
            self.team = team
        if quarter is not None:
            self.quarter = quarter
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if play_description is not None:
            self.play_description = play_description
        if away_score is not None:
            self.away_score = away_score
        if home_score is not None:
            self.home_score = home_score
        if score_id is not None:
            self.score_id = score_id

    @property
    def game_key(self):
        """Gets the game_key of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The game_key of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._game_key

    @game_key.setter
    def game_key(self, game_key):
        """Sets the game_key of this NflPlayByPlayScoringPlay.


        :param game_key: The game_key of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._game_key = game_key

    @property
    def season_type(self):
        """Gets the season_type of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The season_type of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this NflPlayByPlayScoringPlay.


        :param season_type: The season_type of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def scoring_play_id(self):
        """Gets the scoring_play_id of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The scoring_play_id of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._scoring_play_id

    @scoring_play_id.setter
    def scoring_play_id(self, scoring_play_id):
        """Sets the scoring_play_id of this NflPlayByPlayScoringPlay.


        :param scoring_play_id: The scoring_play_id of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._scoring_play_id = scoring_play_id

    @property
    def season(self):
        """Gets the season of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The season of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NflPlayByPlayScoringPlay.


        :param season: The season of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The week of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this NflPlayByPlayScoringPlay.


        :param week: The week of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def away_team(self):
        """Gets the away_team of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The away_team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this NflPlayByPlayScoringPlay.


        :param away_team: The away_team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def home_team(self):
        """Gets the home_team of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The home_team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this NflPlayByPlayScoringPlay.


        :param home_team: The home_team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def _date(self):
        """Gets the _date of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The _date of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this NflPlayByPlayScoringPlay.


        :param _date: The _date of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def sequence(self):
        """Gets the sequence of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The sequence of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this NflPlayByPlayScoringPlay.


        :param sequence: The sequence of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def team(self):
        """Gets the team of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this NflPlayByPlayScoringPlay.


        :param team: The team of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def quarter(self):
        """Gets the quarter of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The quarter of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._quarter

    @quarter.setter
    def quarter(self, quarter):
        """Sets the quarter of this NflPlayByPlayScoringPlay.


        :param quarter: The quarter of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._quarter = quarter

    @property
    def time_remaining(self):
        """Gets the time_remaining of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The time_remaining of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this NflPlayByPlayScoringPlay.


        :param time_remaining: The time_remaining of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._time_remaining = time_remaining

    @property
    def play_description(self):
        """Gets the play_description of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The play_description of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: str
        """
        return self._play_description

    @play_description.setter
    def play_description(self, play_description):
        """Sets the play_description of this NflPlayByPlayScoringPlay.


        :param play_description: The play_description of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: str
        """

        self._play_description = play_description

    @property
    def away_score(self):
        """Gets the away_score of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The away_score of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this NflPlayByPlayScoringPlay.


        :param away_score: The away_score of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def home_score(self):
        """Gets the home_score of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The home_score of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this NflPlayByPlayScoringPlay.


        :param home_score: The home_score of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def score_id(self):
        """Gets the score_id of this NflPlayByPlayScoringPlay.  # noqa: E501


        :return: The score_id of this NflPlayByPlayScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._score_id

    @score_id.setter
    def score_id(self, score_id):
        """Sets the score_id of this NflPlayByPlayScoringPlay.


        :param score_id: The score_id of this NflPlayByPlayScoringPlay.  # noqa: E501
        :type: int
        """

        self._score_id = score_id

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
        if issubclass(NflPlayByPlayScoringPlay, dict):
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
        if not isinstance(other, NflPlayByPlayScoringPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other