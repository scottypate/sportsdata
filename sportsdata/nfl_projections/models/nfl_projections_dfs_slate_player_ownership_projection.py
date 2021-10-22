# coding: utf-8

"""
    NFL v3 Projections

    NFL projected stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflProjectionsDfsSlatePlayerOwnershipProjection(object):
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
        'slate_id': 'int',
        'player_id': 'int',
        'fantasy_defense_player_id': 'int',
        'projected_ownership_percentage': 'float',
        'is_captain': 'bool'
    }

    attribute_map = {
        'slate_id': 'SlateID',
        'player_id': 'PlayerID',
        'fantasy_defense_player_id': 'FantasyDefensePlayerID',
        'projected_ownership_percentage': 'ProjectedOwnershipPercentage',
        'is_captain': 'IsCaptain'
    }

    def __init__(self, slate_id=None, player_id=None, fantasy_defense_player_id=None, projected_ownership_percentage=None, is_captain=None):  # noqa: E501
        """NflProjectionsDfsSlatePlayerOwnershipProjection - a model defined in Swagger"""  # noqa: E501
        self._slate_id = None
        self._player_id = None
        self._fantasy_defense_player_id = None
        self._projected_ownership_percentage = None
        self._is_captain = None
        self.discriminator = None
        if slate_id is not None:
            self.slate_id = slate_id
        if player_id is not None:
            self.player_id = player_id
        if fantasy_defense_player_id is not None:
            self.fantasy_defense_player_id = fantasy_defense_player_id
        if projected_ownership_percentage is not None:
            self.projected_ownership_percentage = projected_ownership_percentage
        if is_captain is not None:
            self.is_captain = is_captain

    @property
    def slate_id(self):
        """Gets the slate_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501


        :return: The slate_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :rtype: int
        """
        return self._slate_id

    @slate_id.setter
    def slate_id(self, slate_id):
        """Sets the slate_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.


        :param slate_id: The slate_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :type: int
        """

        self._slate_id = slate_id

    @property
    def player_id(self):
        """Gets the player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501


        :return: The player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.


        :param player_id: The player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def fantasy_defense_player_id(self):
        """Gets the fantasy_defense_player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501


        :return: The fantasy_defense_player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :rtype: int
        """
        return self._fantasy_defense_player_id

    @fantasy_defense_player_id.setter
    def fantasy_defense_player_id(self, fantasy_defense_player_id):
        """Sets the fantasy_defense_player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.


        :param fantasy_defense_player_id: The fantasy_defense_player_id of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :type: int
        """

        self._fantasy_defense_player_id = fantasy_defense_player_id

    @property
    def projected_ownership_percentage(self):
        """Gets the projected_ownership_percentage of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501


        :return: The projected_ownership_percentage of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :rtype: float
        """
        return self._projected_ownership_percentage

    @projected_ownership_percentage.setter
    def projected_ownership_percentage(self, projected_ownership_percentage):
        """Sets the projected_ownership_percentage of this NflProjectionsDfsSlatePlayerOwnershipProjection.


        :param projected_ownership_percentage: The projected_ownership_percentage of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :type: float
        """

        self._projected_ownership_percentage = projected_ownership_percentage

    @property
    def is_captain(self):
        """Gets the is_captain of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501


        :return: The is_captain of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :rtype: bool
        """
        return self._is_captain

    @is_captain.setter
    def is_captain(self, is_captain):
        """Sets the is_captain of this NflProjectionsDfsSlatePlayerOwnershipProjection.


        :param is_captain: The is_captain of this NflProjectionsDfsSlatePlayerOwnershipProjection.  # noqa: E501
        :type: bool
        """

        self._is_captain = is_captain

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
        if issubclass(NflProjectionsDfsSlatePlayerOwnershipProjection, dict):
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
        if not isinstance(other, NflProjectionsDfsSlatePlayerOwnershipProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other