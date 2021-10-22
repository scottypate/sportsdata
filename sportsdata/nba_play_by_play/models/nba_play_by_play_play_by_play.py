# coding: utf-8

"""
    NBA v3 Play-by-Play

    NBA play-by-play API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NbaPlayByPlayPlayByPlay(object):
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
        'game': 'NbaPlayByPlayGame',
        'quarters': 'list[NbaPlayByPlayQuarter]',
        'plays': 'list[NbaPlayByPlayPlay]'
    }

    attribute_map = {
        'game': 'Game',
        'quarters': 'Quarters',
        'plays': 'Plays'
    }

    def __init__(self, game=None, quarters=None, plays=None):  # noqa: E501
        """NbaPlayByPlayPlayByPlay - a model defined in Swagger"""  # noqa: E501
        self._game = None
        self._quarters = None
        self._plays = None
        self.discriminator = None
        if game is not None:
            self.game = game
        if quarters is not None:
            self.quarters = quarters
        if plays is not None:
            self.plays = plays

    @property
    def game(self):
        """Gets the game of this NbaPlayByPlayPlayByPlay.  # noqa: E501


        :return: The game of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: NbaPlayByPlayGame
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this NbaPlayByPlayPlayByPlay.


        :param game: The game of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :type: NbaPlayByPlayGame
        """

        self._game = game

    @property
    def quarters(self):
        """Gets the quarters of this NbaPlayByPlayPlayByPlay.  # noqa: E501


        :return: The quarters of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: list[NbaPlayByPlayQuarter]
        """
        return self._quarters

    @quarters.setter
    def quarters(self, quarters):
        """Sets the quarters of this NbaPlayByPlayPlayByPlay.


        :param quarters: The quarters of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :type: list[NbaPlayByPlayQuarter]
        """

        self._quarters = quarters

    @property
    def plays(self):
        """Gets the plays of this NbaPlayByPlayPlayByPlay.  # noqa: E501


        :return: The plays of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: list[NbaPlayByPlayPlay]
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this NbaPlayByPlayPlayByPlay.


        :param plays: The plays of this NbaPlayByPlayPlayByPlay.  # noqa: E501
        :type: list[NbaPlayByPlayPlay]
        """

        self._plays = plays

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
        if issubclass(NbaPlayByPlayPlayByPlay, dict):
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
        if not isinstance(other, NbaPlayByPlayPlayByPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
