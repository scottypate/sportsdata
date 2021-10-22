# coding: utf-8

"""
    Golf v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GolfV2PlayerHole(object):
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
        'player_round_id': 'int',
        'number': 'int',
        'par': 'int',
        'score': 'int',
        'to_par': 'int',
        'hole_in_one': 'bool',
        'double_eagle': 'bool',
        'eagle': 'bool',
        'birdie': 'bool',
        'is_par': 'bool',
        'bogey': 'bool',
        'double_bogey': 'bool',
        'worse_than_double_bogey': 'bool'
    }

    attribute_map = {
        'player_round_id': 'PlayerRoundID',
        'number': 'Number',
        'par': 'Par',
        'score': 'Score',
        'to_par': 'ToPar',
        'hole_in_one': 'HoleInOne',
        'double_eagle': 'DoubleEagle',
        'eagle': 'Eagle',
        'birdie': 'Birdie',
        'is_par': 'IsPar',
        'bogey': 'Bogey',
        'double_bogey': 'DoubleBogey',
        'worse_than_double_bogey': 'WorseThanDoubleBogey'
    }

    def __init__(self, player_round_id=None, number=None, par=None, score=None, to_par=None, hole_in_one=None, double_eagle=None, eagle=None, birdie=None, is_par=None, bogey=None, double_bogey=None, worse_than_double_bogey=None):  # noqa: E501
        """GolfV2PlayerHole - a model defined in Swagger"""  # noqa: E501
        self._player_round_id = None
        self._number = None
        self._par = None
        self._score = None
        self._to_par = None
        self._hole_in_one = None
        self._double_eagle = None
        self._eagle = None
        self._birdie = None
        self._is_par = None
        self._bogey = None
        self._double_bogey = None
        self._worse_than_double_bogey = None
        self.discriminator = None
        if player_round_id is not None:
            self.player_round_id = player_round_id
        if number is not None:
            self.number = number
        if par is not None:
            self.par = par
        if score is not None:
            self.score = score
        if to_par is not None:
            self.to_par = to_par
        if hole_in_one is not None:
            self.hole_in_one = hole_in_one
        if double_eagle is not None:
            self.double_eagle = double_eagle
        if eagle is not None:
            self.eagle = eagle
        if birdie is not None:
            self.birdie = birdie
        if is_par is not None:
            self.is_par = is_par
        if bogey is not None:
            self.bogey = bogey
        if double_bogey is not None:
            self.double_bogey = double_bogey
        if worse_than_double_bogey is not None:
            self.worse_than_double_bogey = worse_than_double_bogey

    @property
    def player_round_id(self):
        """Gets the player_round_id of this GolfV2PlayerHole.  # noqa: E501


        :return: The player_round_id of this GolfV2PlayerHole.  # noqa: E501
        :rtype: int
        """
        return self._player_round_id

    @player_round_id.setter
    def player_round_id(self, player_round_id):
        """Sets the player_round_id of this GolfV2PlayerHole.


        :param player_round_id: The player_round_id of this GolfV2PlayerHole.  # noqa: E501
        :type: int
        """

        self._player_round_id = player_round_id

    @property
    def number(self):
        """Gets the number of this GolfV2PlayerHole.  # noqa: E501


        :return: The number of this GolfV2PlayerHole.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GolfV2PlayerHole.


        :param number: The number of this GolfV2PlayerHole.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def par(self):
        """Gets the par of this GolfV2PlayerHole.  # noqa: E501


        :return: The par of this GolfV2PlayerHole.  # noqa: E501
        :rtype: int
        """
        return self._par

    @par.setter
    def par(self, par):
        """Sets the par of this GolfV2PlayerHole.


        :param par: The par of this GolfV2PlayerHole.  # noqa: E501
        :type: int
        """

        self._par = par

    @property
    def score(self):
        """Gets the score of this GolfV2PlayerHole.  # noqa: E501


        :return: The score of this GolfV2PlayerHole.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this GolfV2PlayerHole.


        :param score: The score of this GolfV2PlayerHole.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def to_par(self):
        """Gets the to_par of this GolfV2PlayerHole.  # noqa: E501


        :return: The to_par of this GolfV2PlayerHole.  # noqa: E501
        :rtype: int
        """
        return self._to_par

    @to_par.setter
    def to_par(self, to_par):
        """Sets the to_par of this GolfV2PlayerHole.


        :param to_par: The to_par of this GolfV2PlayerHole.  # noqa: E501
        :type: int
        """

        self._to_par = to_par

    @property
    def hole_in_one(self):
        """Gets the hole_in_one of this GolfV2PlayerHole.  # noqa: E501


        :return: The hole_in_one of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._hole_in_one

    @hole_in_one.setter
    def hole_in_one(self, hole_in_one):
        """Sets the hole_in_one of this GolfV2PlayerHole.


        :param hole_in_one: The hole_in_one of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._hole_in_one = hole_in_one

    @property
    def double_eagle(self):
        """Gets the double_eagle of this GolfV2PlayerHole.  # noqa: E501


        :return: The double_eagle of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._double_eagle

    @double_eagle.setter
    def double_eagle(self, double_eagle):
        """Sets the double_eagle of this GolfV2PlayerHole.


        :param double_eagle: The double_eagle of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._double_eagle = double_eagle

    @property
    def eagle(self):
        """Gets the eagle of this GolfV2PlayerHole.  # noqa: E501


        :return: The eagle of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._eagle

    @eagle.setter
    def eagle(self, eagle):
        """Sets the eagle of this GolfV2PlayerHole.


        :param eagle: The eagle of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._eagle = eagle

    @property
    def birdie(self):
        """Gets the birdie of this GolfV2PlayerHole.  # noqa: E501


        :return: The birdie of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._birdie

    @birdie.setter
    def birdie(self, birdie):
        """Sets the birdie of this GolfV2PlayerHole.


        :param birdie: The birdie of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._birdie = birdie

    @property
    def is_par(self):
        """Gets the is_par of this GolfV2PlayerHole.  # noqa: E501


        :return: The is_par of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._is_par

    @is_par.setter
    def is_par(self, is_par):
        """Sets the is_par of this GolfV2PlayerHole.


        :param is_par: The is_par of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._is_par = is_par

    @property
    def bogey(self):
        """Gets the bogey of this GolfV2PlayerHole.  # noqa: E501


        :return: The bogey of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._bogey

    @bogey.setter
    def bogey(self, bogey):
        """Sets the bogey of this GolfV2PlayerHole.


        :param bogey: The bogey of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._bogey = bogey

    @property
    def double_bogey(self):
        """Gets the double_bogey of this GolfV2PlayerHole.  # noqa: E501


        :return: The double_bogey of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._double_bogey

    @double_bogey.setter
    def double_bogey(self, double_bogey):
        """Sets the double_bogey of this GolfV2PlayerHole.


        :param double_bogey: The double_bogey of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._double_bogey = double_bogey

    @property
    def worse_than_double_bogey(self):
        """Gets the worse_than_double_bogey of this GolfV2PlayerHole.  # noqa: E501


        :return: The worse_than_double_bogey of this GolfV2PlayerHole.  # noqa: E501
        :rtype: bool
        """
        return self._worse_than_double_bogey

    @worse_than_double_bogey.setter
    def worse_than_double_bogey(self, worse_than_double_bogey):
        """Sets the worse_than_double_bogey of this GolfV2PlayerHole.


        :param worse_than_double_bogey: The worse_than_double_bogey of this GolfV2PlayerHole.  # noqa: E501
        :type: bool
        """

        self._worse_than_double_bogey = worse_than_double_bogey

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
        if issubclass(GolfV2PlayerHole, dict):
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
        if not isinstance(other, GolfV2PlayerHole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other