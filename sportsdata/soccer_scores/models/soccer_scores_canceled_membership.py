# coding: utf-8

"""
    Soccer v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoccerScoresCanceledMembership(object):
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
        'canceled_membership_id': 'int',
        'membership_id': 'int',
        'team_id': 'int',
        'player_id': 'int',
        'created': 'str'
    }

    attribute_map = {
        'canceled_membership_id': 'CanceledMembershipId',
        'membership_id': 'MembershipId',
        'team_id': 'TeamId',
        'player_id': 'PlayerID',
        'created': 'Created'
    }

    def __init__(self, canceled_membership_id=None, membership_id=None, team_id=None, player_id=None, created=None):  # noqa: E501
        """SoccerScoresCanceledMembership - a model defined in Swagger"""  # noqa: E501
        self._canceled_membership_id = None
        self._membership_id = None
        self._team_id = None
        self._player_id = None
        self._created = None
        self.discriminator = None
        if canceled_membership_id is not None:
            self.canceled_membership_id = canceled_membership_id
        if membership_id is not None:
            self.membership_id = membership_id
        if team_id is not None:
            self.team_id = team_id
        if player_id is not None:
            self.player_id = player_id
        if created is not None:
            self.created = created

    @property
    def canceled_membership_id(self):
        """Gets the canceled_membership_id of this SoccerScoresCanceledMembership.  # noqa: E501


        :return: The canceled_membership_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :rtype: int
        """
        return self._canceled_membership_id

    @canceled_membership_id.setter
    def canceled_membership_id(self, canceled_membership_id):
        """Sets the canceled_membership_id of this SoccerScoresCanceledMembership.


        :param canceled_membership_id: The canceled_membership_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :type: int
        """

        self._canceled_membership_id = canceled_membership_id

    @property
    def membership_id(self):
        """Gets the membership_id of this SoccerScoresCanceledMembership.  # noqa: E501


        :return: The membership_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :rtype: int
        """
        return self._membership_id

    @membership_id.setter
    def membership_id(self, membership_id):
        """Sets the membership_id of this SoccerScoresCanceledMembership.


        :param membership_id: The membership_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :type: int
        """

        self._membership_id = membership_id

    @property
    def team_id(self):
        """Gets the team_id of this SoccerScoresCanceledMembership.  # noqa: E501


        :return: The team_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this SoccerScoresCanceledMembership.


        :param team_id: The team_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def player_id(self):
        """Gets the player_id of this SoccerScoresCanceledMembership.  # noqa: E501


        :return: The player_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this SoccerScoresCanceledMembership.


        :param player_id: The player_id of this SoccerScoresCanceledMembership.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def created(self):
        """Gets the created of this SoccerScoresCanceledMembership.  # noqa: E501


        :return: The created of this SoccerScoresCanceledMembership.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SoccerScoresCanceledMembership.


        :param created: The created of this SoccerScoresCanceledMembership.  # noqa: E501
        :type: str
        """

        self._created = created

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
        if issubclass(SoccerScoresCanceledMembership, dict):
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
        if not isinstance(other, SoccerScoresCanceledMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other