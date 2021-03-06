# coding: utf-8

"""
    NHL v3 Projections

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NhlProjectionsScoringPlay(object):
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
        'scoring_play_id': 'int',
        'period_id': 'int',
        'sequence': 'int',
        'time_remaining_minutes': 'int',
        'time_remaining_seconds': 'int',
        'scored_by_team_id': 'int',
        'allowed_by_team_id': 'int',
        'scored_by_player_id': 'int',
        'assisted_by_player_id1': 'int',
        'assisted_by_player_id2': 'int',
        'power_play': 'bool',
        'short_handed': 'bool',
        'empty_net': 'bool',
        'away_team_score': 'int',
        'home_team_score': 'int'
    }

    attribute_map = {
        'scoring_play_id': 'ScoringPlayID',
        'period_id': 'PeriodID',
        'sequence': 'Sequence',
        'time_remaining_minutes': 'TimeRemainingMinutes',
        'time_remaining_seconds': 'TimeRemainingSeconds',
        'scored_by_team_id': 'ScoredByTeamID',
        'allowed_by_team_id': 'AllowedByTeamID',
        'scored_by_player_id': 'ScoredByPlayerID',
        'assisted_by_player_id1': 'AssistedByPlayerID1',
        'assisted_by_player_id2': 'AssistedByPlayerID2',
        'power_play': 'PowerPlay',
        'short_handed': 'ShortHanded',
        'empty_net': 'EmptyNet',
        'away_team_score': 'AwayTeamScore',
        'home_team_score': 'HomeTeamScore'
    }

    def __init__(self, scoring_play_id=None, period_id=None, sequence=None, time_remaining_minutes=None, time_remaining_seconds=None, scored_by_team_id=None, allowed_by_team_id=None, scored_by_player_id=None, assisted_by_player_id1=None, assisted_by_player_id2=None, power_play=None, short_handed=None, empty_net=None, away_team_score=None, home_team_score=None):  # noqa: E501
        """NhlProjectionsScoringPlay - a model defined in Swagger"""  # noqa: E501
        self._scoring_play_id = None
        self._period_id = None
        self._sequence = None
        self._time_remaining_minutes = None
        self._time_remaining_seconds = None
        self._scored_by_team_id = None
        self._allowed_by_team_id = None
        self._scored_by_player_id = None
        self._assisted_by_player_id1 = None
        self._assisted_by_player_id2 = None
        self._power_play = None
        self._short_handed = None
        self._empty_net = None
        self._away_team_score = None
        self._home_team_score = None
        self.discriminator = None
        if scoring_play_id is not None:
            self.scoring_play_id = scoring_play_id
        if period_id is not None:
            self.period_id = period_id
        if sequence is not None:
            self.sequence = sequence
        if time_remaining_minutes is not None:
            self.time_remaining_minutes = time_remaining_minutes
        if time_remaining_seconds is not None:
            self.time_remaining_seconds = time_remaining_seconds
        if scored_by_team_id is not None:
            self.scored_by_team_id = scored_by_team_id
        if allowed_by_team_id is not None:
            self.allowed_by_team_id = allowed_by_team_id
        if scored_by_player_id is not None:
            self.scored_by_player_id = scored_by_player_id
        if assisted_by_player_id1 is not None:
            self.assisted_by_player_id1 = assisted_by_player_id1
        if assisted_by_player_id2 is not None:
            self.assisted_by_player_id2 = assisted_by_player_id2
        if power_play is not None:
            self.power_play = power_play
        if short_handed is not None:
            self.short_handed = short_handed
        if empty_net is not None:
            self.empty_net = empty_net
        if away_team_score is not None:
            self.away_team_score = away_team_score
        if home_team_score is not None:
            self.home_team_score = home_team_score

    @property
    def scoring_play_id(self):
        """Gets the scoring_play_id of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The scoring_play_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._scoring_play_id

    @scoring_play_id.setter
    def scoring_play_id(self, scoring_play_id):
        """Sets the scoring_play_id of this NhlProjectionsScoringPlay.


        :param scoring_play_id: The scoring_play_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._scoring_play_id = scoring_play_id

    @property
    def period_id(self):
        """Gets the period_id of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The period_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this NhlProjectionsScoringPlay.


        :param period_id: The period_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._period_id = period_id

    @property
    def sequence(self):
        """Gets the sequence of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The sequence of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this NhlProjectionsScoringPlay.


        :param sequence: The sequence of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def time_remaining_minutes(self):
        """Gets the time_remaining_minutes of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The time_remaining_minutes of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_minutes

    @time_remaining_minutes.setter
    def time_remaining_minutes(self, time_remaining_minutes):
        """Sets the time_remaining_minutes of this NhlProjectionsScoringPlay.


        :param time_remaining_minutes: The time_remaining_minutes of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._time_remaining_minutes = time_remaining_minutes

    @property
    def time_remaining_seconds(self):
        """Gets the time_remaining_seconds of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The time_remaining_seconds of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_seconds

    @time_remaining_seconds.setter
    def time_remaining_seconds(self, time_remaining_seconds):
        """Sets the time_remaining_seconds of this NhlProjectionsScoringPlay.


        :param time_remaining_seconds: The time_remaining_seconds of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._time_remaining_seconds = time_remaining_seconds

    @property
    def scored_by_team_id(self):
        """Gets the scored_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The scored_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._scored_by_team_id

    @scored_by_team_id.setter
    def scored_by_team_id(self, scored_by_team_id):
        """Sets the scored_by_team_id of this NhlProjectionsScoringPlay.


        :param scored_by_team_id: The scored_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._scored_by_team_id = scored_by_team_id

    @property
    def allowed_by_team_id(self):
        """Gets the allowed_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The allowed_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._allowed_by_team_id

    @allowed_by_team_id.setter
    def allowed_by_team_id(self, allowed_by_team_id):
        """Sets the allowed_by_team_id of this NhlProjectionsScoringPlay.


        :param allowed_by_team_id: The allowed_by_team_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._allowed_by_team_id = allowed_by_team_id

    @property
    def scored_by_player_id(self):
        """Gets the scored_by_player_id of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The scored_by_player_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._scored_by_player_id

    @scored_by_player_id.setter
    def scored_by_player_id(self, scored_by_player_id):
        """Sets the scored_by_player_id of this NhlProjectionsScoringPlay.


        :param scored_by_player_id: The scored_by_player_id of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._scored_by_player_id = scored_by_player_id

    @property
    def assisted_by_player_id1(self):
        """Gets the assisted_by_player_id1 of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The assisted_by_player_id1 of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._assisted_by_player_id1

    @assisted_by_player_id1.setter
    def assisted_by_player_id1(self, assisted_by_player_id1):
        """Sets the assisted_by_player_id1 of this NhlProjectionsScoringPlay.


        :param assisted_by_player_id1: The assisted_by_player_id1 of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._assisted_by_player_id1 = assisted_by_player_id1

    @property
    def assisted_by_player_id2(self):
        """Gets the assisted_by_player_id2 of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The assisted_by_player_id2 of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._assisted_by_player_id2

    @assisted_by_player_id2.setter
    def assisted_by_player_id2(self, assisted_by_player_id2):
        """Sets the assisted_by_player_id2 of this NhlProjectionsScoringPlay.


        :param assisted_by_player_id2: The assisted_by_player_id2 of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._assisted_by_player_id2 = assisted_by_player_id2

    @property
    def power_play(self):
        """Gets the power_play of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The power_play of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: bool
        """
        return self._power_play

    @power_play.setter
    def power_play(self, power_play):
        """Sets the power_play of this NhlProjectionsScoringPlay.


        :param power_play: The power_play of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: bool
        """

        self._power_play = power_play

    @property
    def short_handed(self):
        """Gets the short_handed of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The short_handed of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: bool
        """
        return self._short_handed

    @short_handed.setter
    def short_handed(self, short_handed):
        """Sets the short_handed of this NhlProjectionsScoringPlay.


        :param short_handed: The short_handed of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: bool
        """

        self._short_handed = short_handed

    @property
    def empty_net(self):
        """Gets the empty_net of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The empty_net of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: bool
        """
        return self._empty_net

    @empty_net.setter
    def empty_net(self, empty_net):
        """Sets the empty_net of this NhlProjectionsScoringPlay.


        :param empty_net: The empty_net of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: bool
        """

        self._empty_net = empty_net

    @property
    def away_team_score(self):
        """Gets the away_team_score of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The away_team_score of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this NhlProjectionsScoringPlay.


        :param away_team_score: The away_team_score of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._away_team_score = away_team_score

    @property
    def home_team_score(self):
        """Gets the home_team_score of this NhlProjectionsScoringPlay.  # noqa: E501


        :return: The home_team_score of this NhlProjectionsScoringPlay.  # noqa: E501
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this NhlProjectionsScoringPlay.


        :param home_team_score: The home_team_score of this NhlProjectionsScoringPlay.  # noqa: E501
        :type: int
        """

        self._home_team_score = home_team_score

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
        if issubclass(NhlProjectionsScoringPlay, dict):
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
        if not isinstance(other, NhlProjectionsScoringPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
