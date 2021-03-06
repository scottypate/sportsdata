# coding: utf-8

"""
    MLB v3 Projections

    MLB projections API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbProjectionsDfsSlateGame(object):
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
        'slate_game_id': 'int',
        'slate_id': 'int',
        'game_id': 'int',
        'game': 'MlbProjectionsGame',
        'operator_game_id': 'int',
        'removed_by_operator': 'bool'
    }

    attribute_map = {
        'slate_game_id': 'SlateGameID',
        'slate_id': 'SlateID',
        'game_id': 'GameID',
        'game': 'Game',
        'operator_game_id': 'OperatorGameID',
        'removed_by_operator': 'RemovedByOperator'
    }

    def __init__(self, slate_game_id=None, slate_id=None, game_id=None, game=None, operator_game_id=None, removed_by_operator=None):  # noqa: E501
        """MlbProjectionsDfsSlateGame - a model defined in Swagger"""  # noqa: E501
        self._slate_game_id = None
        self._slate_id = None
        self._game_id = None
        self._game = None
        self._operator_game_id = None
        self._removed_by_operator = None
        self.discriminator = None
        if slate_game_id is not None:
            self.slate_game_id = slate_game_id
        if slate_id is not None:
            self.slate_id = slate_id
        if game_id is not None:
            self.game_id = game_id
        if game is not None:
            self.game = game
        if operator_game_id is not None:
            self.operator_game_id = operator_game_id
        if removed_by_operator is not None:
            self.removed_by_operator = removed_by_operator

    @property
    def slate_game_id(self):
        """Gets the slate_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The slate_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: int
        """
        return self._slate_game_id

    @slate_game_id.setter
    def slate_game_id(self, slate_game_id):
        """Sets the slate_game_id of this MlbProjectionsDfsSlateGame.


        :param slate_game_id: The slate_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: int
        """

        self._slate_game_id = slate_game_id

    @property
    def slate_id(self):
        """Gets the slate_id of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The slate_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: int
        """
        return self._slate_id

    @slate_id.setter
    def slate_id(self, slate_id):
        """Sets the slate_id of this MlbProjectionsDfsSlateGame.


        :param slate_id: The slate_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: int
        """

        self._slate_id = slate_id

    @property
    def game_id(self):
        """Gets the game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this MlbProjectionsDfsSlateGame.


        :param game_id: The game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def game(self):
        """Gets the game of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The game of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: MlbProjectionsGame
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this MlbProjectionsDfsSlateGame.


        :param game: The game of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: MlbProjectionsGame
        """

        self._game = game

    @property
    def operator_game_id(self):
        """Gets the operator_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The operator_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: int
        """
        return self._operator_game_id

    @operator_game_id.setter
    def operator_game_id(self, operator_game_id):
        """Sets the operator_game_id of this MlbProjectionsDfsSlateGame.


        :param operator_game_id: The operator_game_id of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: int
        """

        self._operator_game_id = operator_game_id

    @property
    def removed_by_operator(self):
        """Gets the removed_by_operator of this MlbProjectionsDfsSlateGame.  # noqa: E501


        :return: The removed_by_operator of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :rtype: bool
        """
        return self._removed_by_operator

    @removed_by_operator.setter
    def removed_by_operator(self, removed_by_operator):
        """Sets the removed_by_operator of this MlbProjectionsDfsSlateGame.


        :param removed_by_operator: The removed_by_operator of this MlbProjectionsDfsSlateGame.  # noqa: E501
        :type: bool
        """

        self._removed_by_operator = removed_by_operator

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
        if issubclass(MlbProjectionsDfsSlateGame, dict):
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
        if not isinstance(other, MlbProjectionsDfsSlateGame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
