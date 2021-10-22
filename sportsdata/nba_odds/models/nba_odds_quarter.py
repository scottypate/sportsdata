# coding: utf-8

"""
    NBA v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NbaOddsQuarter(object):
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
        'quarter_id': 'int',
        'game_id': 'int',
        'number': 'int',
        'name': 'str',
        'away_score': 'int',
        'home_score': 'int'
    }

    attribute_map = {
        'quarter_id': 'QuarterID',
        'game_id': 'GameID',
        'number': 'Number',
        'name': 'Name',
        'away_score': 'AwayScore',
        'home_score': 'HomeScore'
    }

    def __init__(self, quarter_id=None, game_id=None, number=None, name=None, away_score=None, home_score=None):  # noqa: E501
        """NbaOddsQuarter - a model defined in Swagger"""  # noqa: E501
        self._quarter_id = None
        self._game_id = None
        self._number = None
        self._name = None
        self._away_score = None
        self._home_score = None
        self.discriminator = None
        if quarter_id is not None:
            self.quarter_id = quarter_id
        if game_id is not None:
            self.game_id = game_id
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if away_score is not None:
            self.away_score = away_score
        if home_score is not None:
            self.home_score = home_score

    @property
    def quarter_id(self):
        """Gets the quarter_id of this NbaOddsQuarter.  # noqa: E501


        :return: The quarter_id of this NbaOddsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._quarter_id

    @quarter_id.setter
    def quarter_id(self, quarter_id):
        """Sets the quarter_id of this NbaOddsQuarter.


        :param quarter_id: The quarter_id of this NbaOddsQuarter.  # noqa: E501
        :type: int
        """

        self._quarter_id = quarter_id

    @property
    def game_id(self):
        """Gets the game_id of this NbaOddsQuarter.  # noqa: E501


        :return: The game_id of this NbaOddsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this NbaOddsQuarter.


        :param game_id: The game_id of this NbaOddsQuarter.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def number(self):
        """Gets the number of this NbaOddsQuarter.  # noqa: E501


        :return: The number of this NbaOddsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this NbaOddsQuarter.


        :param number: The number of this NbaOddsQuarter.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this NbaOddsQuarter.  # noqa: E501


        :return: The name of this NbaOddsQuarter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NbaOddsQuarter.


        :param name: The name of this NbaOddsQuarter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def away_score(self):
        """Gets the away_score of this NbaOddsQuarter.  # noqa: E501


        :return: The away_score of this NbaOddsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this NbaOddsQuarter.


        :param away_score: The away_score of this NbaOddsQuarter.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def home_score(self):
        """Gets the home_score of this NbaOddsQuarter.  # noqa: E501


        :return: The home_score of this NbaOddsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this NbaOddsQuarter.


        :param home_score: The home_score of this NbaOddsQuarter.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

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
        if issubclass(NbaOddsQuarter, dict):
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
        if not isinstance(other, NbaOddsQuarter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
