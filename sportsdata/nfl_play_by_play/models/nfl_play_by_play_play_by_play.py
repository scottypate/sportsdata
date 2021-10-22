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

class NflPlayByPlayPlayByPlay(object):
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
        'score': 'NflPlayByPlayScore',
        'quarters': 'list[NflPlayByPlayQuarter]',
        'plays': 'list[NflPlayByPlayPlay]'
    }

    attribute_map = {
        'score': 'Score',
        'quarters': 'Quarters',
        'plays': 'Plays'
    }

    def __init__(self, score=None, quarters=None, plays=None):  # noqa: E501
        """NflPlayByPlayPlayByPlay - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._quarters = None
        self._plays = None
        self.discriminator = None
        if score is not None:
            self.score = score
        if quarters is not None:
            self.quarters = quarters
        if plays is not None:
            self.plays = plays

    @property
    def score(self):
        """Gets the score of this NflPlayByPlayPlayByPlay.  # noqa: E501


        :return: The score of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: NflPlayByPlayScore
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this NflPlayByPlayPlayByPlay.


        :param score: The score of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :type: NflPlayByPlayScore
        """

        self._score = score

    @property
    def quarters(self):
        """Gets the quarters of this NflPlayByPlayPlayByPlay.  # noqa: E501


        :return: The quarters of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: list[NflPlayByPlayQuarter]
        """
        return self._quarters

    @quarters.setter
    def quarters(self, quarters):
        """Sets the quarters of this NflPlayByPlayPlayByPlay.


        :param quarters: The quarters of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :type: list[NflPlayByPlayQuarter]
        """

        self._quarters = quarters

    @property
    def plays(self):
        """Gets the plays of this NflPlayByPlayPlayByPlay.  # noqa: E501


        :return: The plays of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :rtype: list[NflPlayByPlayPlay]
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this NflPlayByPlayPlayByPlay.


        :param plays: The plays of this NflPlayByPlayPlayByPlay.  # noqa: E501
        :type: list[NflPlayByPlayPlay]
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
        if issubclass(NflPlayByPlayPlayByPlay, dict):
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
        if not isinstance(other, NflPlayByPlayPlayByPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other