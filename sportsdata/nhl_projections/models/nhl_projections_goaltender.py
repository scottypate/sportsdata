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

class NhlProjectionsGoaltender(object):
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
        'player_id': 'int',
        'team_id': 'int',
        'team': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'jersey': 'int',
        'confirmed': 'bool'
    }

    attribute_map = {
        'player_id': 'PlayerID',
        'team_id': 'TeamID',
        'team': 'Team',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'jersey': 'Jersey',
        'confirmed': 'Confirmed'
    }

    def __init__(self, player_id=None, team_id=None, team=None, first_name=None, last_name=None, jersey=None, confirmed=None):  # noqa: E501
        """NhlProjectionsGoaltender - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._team_id = None
        self._team = None
        self._first_name = None
        self._last_name = None
        self._jersey = None
        self._confirmed = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if jersey is not None:
            self.jersey = jersey
        if confirmed is not None:
            self.confirmed = confirmed

    @property
    def player_id(self):
        """Gets the player_id of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The player_id of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this NhlProjectionsGoaltender.


        :param player_id: The player_id of this NhlProjectionsGoaltender.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def team_id(self):
        """Gets the team_id of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The team_id of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NhlProjectionsGoaltender.


        :param team_id: The team_id of this NhlProjectionsGoaltender.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The team of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this NhlProjectionsGoaltender.


        :param team: The team of this NhlProjectionsGoaltender.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def first_name(self):
        """Gets the first_name of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The first_name of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this NhlProjectionsGoaltender.


        :param first_name: The first_name of this NhlProjectionsGoaltender.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The last_name of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this NhlProjectionsGoaltender.


        :param last_name: The last_name of this NhlProjectionsGoaltender.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def jersey(self):
        """Gets the jersey of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The jersey of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this NhlProjectionsGoaltender.


        :param jersey: The jersey of this NhlProjectionsGoaltender.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

    @property
    def confirmed(self):
        """Gets the confirmed of this NhlProjectionsGoaltender.  # noqa: E501


        :return: The confirmed of this NhlProjectionsGoaltender.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this NhlProjectionsGoaltender.


        :param confirmed: The confirmed of this NhlProjectionsGoaltender.  # noqa: E501
        :type: bool
        """

        self._confirmed = confirmed

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
        if issubclass(NhlProjectionsGoaltender, dict):
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
        if not isinstance(other, NhlProjectionsGoaltender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
