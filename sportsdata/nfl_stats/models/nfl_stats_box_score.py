# coding: utf-8

"""
    NFL v3 Stats

    NFL rosters, player stats, team stats, and fantasy stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflStatsBoxScore(object):
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
        'score': 'NflStatsScore',
        'game': 'NflStatsGame',
        'scoring_plays': 'list[NflStatsScoringPlay]',
        'scoring_details': 'list[NflStatsScoringDetail]',
        'away_fantasy_defense': 'NflStatsFantasyDefenseGame',
        'home_fantasy_defense': 'NflStatsFantasyDefenseGame',
        'away_passing': 'list[NflStatsPlayerPassing]',
        'away_rushing': 'list[NflStatsPlayerRushing]',
        'away_receiving': 'list[NflStatsPlayerReceiving]',
        'away_kicking': 'list[NflStatsPlayerKicking]',
        'away_punting': 'list[NflStatsPlayerPunting]',
        'away_kick_punt_returns': 'list[NflStatsPlayerKickPuntReturns]',
        'away_defense': 'list[NflStatsPlayerDefense]',
        'home_passing': 'list[NflStatsPlayerPassing]',
        'home_rushing': 'list[NflStatsPlayerRushing]',
        'home_receiving': 'list[NflStatsPlayerReceiving]',
        'home_kicking': 'list[NflStatsPlayerKicking]',
        'home_punting': 'list[NflStatsPlayerPunting]',
        'home_kick_punt_returns': 'list[NflStatsPlayerKickPuntReturns]',
        'home_defense': 'list[NflStatsPlayerDefense]'
    }

    attribute_map = {
        'score': 'Score',
        'game': 'Game',
        'scoring_plays': 'ScoringPlays',
        'scoring_details': 'ScoringDetails',
        'away_fantasy_defense': 'AwayFantasyDefense',
        'home_fantasy_defense': 'HomeFantasyDefense',
        'away_passing': 'AwayPassing',
        'away_rushing': 'AwayRushing',
        'away_receiving': 'AwayReceiving',
        'away_kicking': 'AwayKicking',
        'away_punting': 'AwayPunting',
        'away_kick_punt_returns': 'AwayKickPuntReturns',
        'away_defense': 'AwayDefense',
        'home_passing': 'HomePassing',
        'home_rushing': 'HomeRushing',
        'home_receiving': 'HomeReceiving',
        'home_kicking': 'HomeKicking',
        'home_punting': 'HomePunting',
        'home_kick_punt_returns': 'HomeKickPuntReturns',
        'home_defense': 'HomeDefense'
    }

    def __init__(self, score=None, game=None, scoring_plays=None, scoring_details=None, away_fantasy_defense=None, home_fantasy_defense=None, away_passing=None, away_rushing=None, away_receiving=None, away_kicking=None, away_punting=None, away_kick_punt_returns=None, away_defense=None, home_passing=None, home_rushing=None, home_receiving=None, home_kicking=None, home_punting=None, home_kick_punt_returns=None, home_defense=None):  # noqa: E501
        """NflStatsBoxScore - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._game = None
        self._scoring_plays = None
        self._scoring_details = None
        self._away_fantasy_defense = None
        self._home_fantasy_defense = None
        self._away_passing = None
        self._away_rushing = None
        self._away_receiving = None
        self._away_kicking = None
        self._away_punting = None
        self._away_kick_punt_returns = None
        self._away_defense = None
        self._home_passing = None
        self._home_rushing = None
        self._home_receiving = None
        self._home_kicking = None
        self._home_punting = None
        self._home_kick_punt_returns = None
        self._home_defense = None
        self.discriminator = None
        if score is not None:
            self.score = score
        if game is not None:
            self.game = game
        if scoring_plays is not None:
            self.scoring_plays = scoring_plays
        if scoring_details is not None:
            self.scoring_details = scoring_details
        if away_fantasy_defense is not None:
            self.away_fantasy_defense = away_fantasy_defense
        if home_fantasy_defense is not None:
            self.home_fantasy_defense = home_fantasy_defense
        if away_passing is not None:
            self.away_passing = away_passing
        if away_rushing is not None:
            self.away_rushing = away_rushing
        if away_receiving is not None:
            self.away_receiving = away_receiving
        if away_kicking is not None:
            self.away_kicking = away_kicking
        if away_punting is not None:
            self.away_punting = away_punting
        if away_kick_punt_returns is not None:
            self.away_kick_punt_returns = away_kick_punt_returns
        if away_defense is not None:
            self.away_defense = away_defense
        if home_passing is not None:
            self.home_passing = home_passing
        if home_rushing is not None:
            self.home_rushing = home_rushing
        if home_receiving is not None:
            self.home_receiving = home_receiving
        if home_kicking is not None:
            self.home_kicking = home_kicking
        if home_punting is not None:
            self.home_punting = home_punting
        if home_kick_punt_returns is not None:
            self.home_kick_punt_returns = home_kick_punt_returns
        if home_defense is not None:
            self.home_defense = home_defense

    @property
    def score(self):
        """Gets the score of this NflStatsBoxScore.  # noqa: E501


        :return: The score of this NflStatsBoxScore.  # noqa: E501
        :rtype: NflStatsScore
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this NflStatsBoxScore.


        :param score: The score of this NflStatsBoxScore.  # noqa: E501
        :type: NflStatsScore
        """

        self._score = score

    @property
    def game(self):
        """Gets the game of this NflStatsBoxScore.  # noqa: E501


        :return: The game of this NflStatsBoxScore.  # noqa: E501
        :rtype: NflStatsGame
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this NflStatsBoxScore.


        :param game: The game of this NflStatsBoxScore.  # noqa: E501
        :type: NflStatsGame
        """

        self._game = game

    @property
    def scoring_plays(self):
        """Gets the scoring_plays of this NflStatsBoxScore.  # noqa: E501


        :return: The scoring_plays of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsScoringPlay]
        """
        return self._scoring_plays

    @scoring_plays.setter
    def scoring_plays(self, scoring_plays):
        """Sets the scoring_plays of this NflStatsBoxScore.


        :param scoring_plays: The scoring_plays of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsScoringPlay]
        """

        self._scoring_plays = scoring_plays

    @property
    def scoring_details(self):
        """Gets the scoring_details of this NflStatsBoxScore.  # noqa: E501


        :return: The scoring_details of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsScoringDetail]
        """
        return self._scoring_details

    @scoring_details.setter
    def scoring_details(self, scoring_details):
        """Sets the scoring_details of this NflStatsBoxScore.


        :param scoring_details: The scoring_details of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsScoringDetail]
        """

        self._scoring_details = scoring_details

    @property
    def away_fantasy_defense(self):
        """Gets the away_fantasy_defense of this NflStatsBoxScore.  # noqa: E501


        :return: The away_fantasy_defense of this NflStatsBoxScore.  # noqa: E501
        :rtype: NflStatsFantasyDefenseGame
        """
        return self._away_fantasy_defense

    @away_fantasy_defense.setter
    def away_fantasy_defense(self, away_fantasy_defense):
        """Sets the away_fantasy_defense of this NflStatsBoxScore.


        :param away_fantasy_defense: The away_fantasy_defense of this NflStatsBoxScore.  # noqa: E501
        :type: NflStatsFantasyDefenseGame
        """

        self._away_fantasy_defense = away_fantasy_defense

    @property
    def home_fantasy_defense(self):
        """Gets the home_fantasy_defense of this NflStatsBoxScore.  # noqa: E501


        :return: The home_fantasy_defense of this NflStatsBoxScore.  # noqa: E501
        :rtype: NflStatsFantasyDefenseGame
        """
        return self._home_fantasy_defense

    @home_fantasy_defense.setter
    def home_fantasy_defense(self, home_fantasy_defense):
        """Sets the home_fantasy_defense of this NflStatsBoxScore.


        :param home_fantasy_defense: The home_fantasy_defense of this NflStatsBoxScore.  # noqa: E501
        :type: NflStatsFantasyDefenseGame
        """

        self._home_fantasy_defense = home_fantasy_defense

    @property
    def away_passing(self):
        """Gets the away_passing of this NflStatsBoxScore.  # noqa: E501


        :return: The away_passing of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerPassing]
        """
        return self._away_passing

    @away_passing.setter
    def away_passing(self, away_passing):
        """Sets the away_passing of this NflStatsBoxScore.


        :param away_passing: The away_passing of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerPassing]
        """

        self._away_passing = away_passing

    @property
    def away_rushing(self):
        """Gets the away_rushing of this NflStatsBoxScore.  # noqa: E501


        :return: The away_rushing of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerRushing]
        """
        return self._away_rushing

    @away_rushing.setter
    def away_rushing(self, away_rushing):
        """Sets the away_rushing of this NflStatsBoxScore.


        :param away_rushing: The away_rushing of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerRushing]
        """

        self._away_rushing = away_rushing

    @property
    def away_receiving(self):
        """Gets the away_receiving of this NflStatsBoxScore.  # noqa: E501


        :return: The away_receiving of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerReceiving]
        """
        return self._away_receiving

    @away_receiving.setter
    def away_receiving(self, away_receiving):
        """Sets the away_receiving of this NflStatsBoxScore.


        :param away_receiving: The away_receiving of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerReceiving]
        """

        self._away_receiving = away_receiving

    @property
    def away_kicking(self):
        """Gets the away_kicking of this NflStatsBoxScore.  # noqa: E501


        :return: The away_kicking of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerKicking]
        """
        return self._away_kicking

    @away_kicking.setter
    def away_kicking(self, away_kicking):
        """Sets the away_kicking of this NflStatsBoxScore.


        :param away_kicking: The away_kicking of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerKicking]
        """

        self._away_kicking = away_kicking

    @property
    def away_punting(self):
        """Gets the away_punting of this NflStatsBoxScore.  # noqa: E501


        :return: The away_punting of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerPunting]
        """
        return self._away_punting

    @away_punting.setter
    def away_punting(self, away_punting):
        """Sets the away_punting of this NflStatsBoxScore.


        :param away_punting: The away_punting of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerPunting]
        """

        self._away_punting = away_punting

    @property
    def away_kick_punt_returns(self):
        """Gets the away_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501


        :return: The away_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerKickPuntReturns]
        """
        return self._away_kick_punt_returns

    @away_kick_punt_returns.setter
    def away_kick_punt_returns(self, away_kick_punt_returns):
        """Sets the away_kick_punt_returns of this NflStatsBoxScore.


        :param away_kick_punt_returns: The away_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerKickPuntReturns]
        """

        self._away_kick_punt_returns = away_kick_punt_returns

    @property
    def away_defense(self):
        """Gets the away_defense of this NflStatsBoxScore.  # noqa: E501


        :return: The away_defense of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerDefense]
        """
        return self._away_defense

    @away_defense.setter
    def away_defense(self, away_defense):
        """Sets the away_defense of this NflStatsBoxScore.


        :param away_defense: The away_defense of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerDefense]
        """

        self._away_defense = away_defense

    @property
    def home_passing(self):
        """Gets the home_passing of this NflStatsBoxScore.  # noqa: E501


        :return: The home_passing of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerPassing]
        """
        return self._home_passing

    @home_passing.setter
    def home_passing(self, home_passing):
        """Sets the home_passing of this NflStatsBoxScore.


        :param home_passing: The home_passing of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerPassing]
        """

        self._home_passing = home_passing

    @property
    def home_rushing(self):
        """Gets the home_rushing of this NflStatsBoxScore.  # noqa: E501


        :return: The home_rushing of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerRushing]
        """
        return self._home_rushing

    @home_rushing.setter
    def home_rushing(self, home_rushing):
        """Sets the home_rushing of this NflStatsBoxScore.


        :param home_rushing: The home_rushing of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerRushing]
        """

        self._home_rushing = home_rushing

    @property
    def home_receiving(self):
        """Gets the home_receiving of this NflStatsBoxScore.  # noqa: E501


        :return: The home_receiving of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerReceiving]
        """
        return self._home_receiving

    @home_receiving.setter
    def home_receiving(self, home_receiving):
        """Sets the home_receiving of this NflStatsBoxScore.


        :param home_receiving: The home_receiving of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerReceiving]
        """

        self._home_receiving = home_receiving

    @property
    def home_kicking(self):
        """Gets the home_kicking of this NflStatsBoxScore.  # noqa: E501


        :return: The home_kicking of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerKicking]
        """
        return self._home_kicking

    @home_kicking.setter
    def home_kicking(self, home_kicking):
        """Sets the home_kicking of this NflStatsBoxScore.


        :param home_kicking: The home_kicking of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerKicking]
        """

        self._home_kicking = home_kicking

    @property
    def home_punting(self):
        """Gets the home_punting of this NflStatsBoxScore.  # noqa: E501


        :return: The home_punting of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerPunting]
        """
        return self._home_punting

    @home_punting.setter
    def home_punting(self, home_punting):
        """Sets the home_punting of this NflStatsBoxScore.


        :param home_punting: The home_punting of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerPunting]
        """

        self._home_punting = home_punting

    @property
    def home_kick_punt_returns(self):
        """Gets the home_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501


        :return: The home_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerKickPuntReturns]
        """
        return self._home_kick_punt_returns

    @home_kick_punt_returns.setter
    def home_kick_punt_returns(self, home_kick_punt_returns):
        """Sets the home_kick_punt_returns of this NflStatsBoxScore.


        :param home_kick_punt_returns: The home_kick_punt_returns of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerKickPuntReturns]
        """

        self._home_kick_punt_returns = home_kick_punt_returns

    @property
    def home_defense(self):
        """Gets the home_defense of this NflStatsBoxScore.  # noqa: E501


        :return: The home_defense of this NflStatsBoxScore.  # noqa: E501
        :rtype: list[NflStatsPlayerDefense]
        """
        return self._home_defense

    @home_defense.setter
    def home_defense(self, home_defense):
        """Sets the home_defense of this NflStatsBoxScore.


        :param home_defense: The home_defense of this NflStatsBoxScore.  # noqa: E501
        :type: list[NflStatsPlayerDefense]
        """

        self._home_defense = home_defense

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
        if issubclass(NflStatsBoxScore, dict):
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
        if not isinstance(other, NflStatsBoxScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
