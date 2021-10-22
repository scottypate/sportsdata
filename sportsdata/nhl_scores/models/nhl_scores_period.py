# coding: utf-8

"""
    NHL v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NhlScoresPeriod(object):
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
        'period_id': 'int',
        'game_id': 'int',
        'name': 'str',
        'away_score': 'int',
        'home_score': 'int',
        'scoring_plays': 'list[NhlScoresScoringPlay]',
        'penalties': 'list[NhlScoresPenalty]'
    }

    attribute_map = {
        'period_id': 'PeriodID',
        'game_id': 'GameID',
        'name': 'Name',
        'away_score': 'AwayScore',
        'home_score': 'HomeScore',
        'scoring_plays': 'ScoringPlays',
        'penalties': 'Penalties'
    }

    def __init__(self, period_id=None, game_id=None, name=None, away_score=None, home_score=None, scoring_plays=None, penalties=None):  # noqa: E501
        """NhlScoresPeriod - a model defined in Swagger"""  # noqa: E501
        self._period_id = None
        self._game_id = None
        self._name = None
        self._away_score = None
        self._home_score = None
        self._scoring_plays = None
        self._penalties = None
        self.discriminator = None
        if period_id is not None:
            self.period_id = period_id
        if game_id is not None:
            self.game_id = game_id
        if name is not None:
            self.name = name
        if away_score is not None:
            self.away_score = away_score
        if home_score is not None:
            self.home_score = home_score
        if scoring_plays is not None:
            self.scoring_plays = scoring_plays
        if penalties is not None:
            self.penalties = penalties

    @property
    def period_id(self):
        """Gets the period_id of this NhlScoresPeriod.  # noqa: E501


        :return: The period_id of this NhlScoresPeriod.  # noqa: E501
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this NhlScoresPeriod.


        :param period_id: The period_id of this NhlScoresPeriod.  # noqa: E501
        :type: int
        """

        self._period_id = period_id

    @property
    def game_id(self):
        """Gets the game_id of this NhlScoresPeriod.  # noqa: E501


        :return: The game_id of this NhlScoresPeriod.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this NhlScoresPeriod.


        :param game_id: The game_id of this NhlScoresPeriod.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def name(self):
        """Gets the name of this NhlScoresPeriod.  # noqa: E501


        :return: The name of this NhlScoresPeriod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NhlScoresPeriod.


        :param name: The name of this NhlScoresPeriod.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def away_score(self):
        """Gets the away_score of this NhlScoresPeriod.  # noqa: E501


        :return: The away_score of this NhlScoresPeriod.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this NhlScoresPeriod.


        :param away_score: The away_score of this NhlScoresPeriod.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def home_score(self):
        """Gets the home_score of this NhlScoresPeriod.  # noqa: E501


        :return: The home_score of this NhlScoresPeriod.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this NhlScoresPeriod.


        :param home_score: The home_score of this NhlScoresPeriod.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def scoring_plays(self):
        """Gets the scoring_plays of this NhlScoresPeriod.  # noqa: E501


        :return: The scoring_plays of this NhlScoresPeriod.  # noqa: E501
        :rtype: list[NhlScoresScoringPlay]
        """
        return self._scoring_plays

    @scoring_plays.setter
    def scoring_plays(self, scoring_plays):
        """Sets the scoring_plays of this NhlScoresPeriod.


        :param scoring_plays: The scoring_plays of this NhlScoresPeriod.  # noqa: E501
        :type: list[NhlScoresScoringPlay]
        """

        self._scoring_plays = scoring_plays

    @property
    def penalties(self):
        """Gets the penalties of this NhlScoresPeriod.  # noqa: E501


        :return: The penalties of this NhlScoresPeriod.  # noqa: E501
        :rtype: list[NhlScoresPenalty]
        """
        return self._penalties

    @penalties.setter
    def penalties(self, penalties):
        """Sets the penalties of this NhlScoresPeriod.


        :param penalties: The penalties of this NhlScoresPeriod.  # noqa: E501
        :type: list[NhlScoresPenalty]
        """

        self._penalties = penalties

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
        if issubclass(NhlScoresPeriod, dict):
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
        if not isinstance(other, NhlScoresPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
