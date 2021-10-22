# coding: utf-8

"""
    Soccer v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoccerStatsMembership(object):
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
        'membership_id': 'int',
        'team_id': 'int',
        'player_id': 'int',
        'player_name': 'str',
        'team_name': 'str',
        'team_area': 'str',
        'active': 'bool',
        'start_date': 'str',
        'end_date': 'str',
        'updated': 'str',
        'jersey': 'int'
    }

    attribute_map = {
        'membership_id': 'MembershipId',
        'team_id': 'TeamId',
        'player_id': 'PlayerId',
        'player_name': 'PlayerName',
        'team_name': 'TeamName',
        'team_area': 'TeamArea',
        'active': 'Active',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'updated': 'Updated',
        'jersey': 'Jersey'
    }

    def __init__(self, membership_id=None, team_id=None, player_id=None, player_name=None, team_name=None, team_area=None, active=None, start_date=None, end_date=None, updated=None, jersey=None):  # noqa: E501
        """SoccerStatsMembership - a model defined in Swagger"""  # noqa: E501
        self._membership_id = None
        self._team_id = None
        self._player_id = None
        self._player_name = None
        self._team_name = None
        self._team_area = None
        self._active = None
        self._start_date = None
        self._end_date = None
        self._updated = None
        self._jersey = None
        self.discriminator = None
        if membership_id is not None:
            self.membership_id = membership_id
        if team_id is not None:
            self.team_id = team_id
        if player_id is not None:
            self.player_id = player_id
        if player_name is not None:
            self.player_name = player_name
        if team_name is not None:
            self.team_name = team_name
        if team_area is not None:
            self.team_area = team_area
        if active is not None:
            self.active = active
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if updated is not None:
            self.updated = updated
        if jersey is not None:
            self.jersey = jersey

    @property
    def membership_id(self):
        """Gets the membership_id of this SoccerStatsMembership.  # noqa: E501


        :return: The membership_id of this SoccerStatsMembership.  # noqa: E501
        :rtype: int
        """
        return self._membership_id

    @membership_id.setter
    def membership_id(self, membership_id):
        """Sets the membership_id of this SoccerStatsMembership.


        :param membership_id: The membership_id of this SoccerStatsMembership.  # noqa: E501
        :type: int
        """

        self._membership_id = membership_id

    @property
    def team_id(self):
        """Gets the team_id of this SoccerStatsMembership.  # noqa: E501


        :return: The team_id of this SoccerStatsMembership.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this SoccerStatsMembership.


        :param team_id: The team_id of this SoccerStatsMembership.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def player_id(self):
        """Gets the player_id of this SoccerStatsMembership.  # noqa: E501


        :return: The player_id of this SoccerStatsMembership.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this SoccerStatsMembership.


        :param player_id: The player_id of this SoccerStatsMembership.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def player_name(self):
        """Gets the player_name of this SoccerStatsMembership.  # noqa: E501


        :return: The player_name of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._player_name

    @player_name.setter
    def player_name(self, player_name):
        """Sets the player_name of this SoccerStatsMembership.


        :param player_name: The player_name of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._player_name = player_name

    @property
    def team_name(self):
        """Gets the team_name of this SoccerStatsMembership.  # noqa: E501


        :return: The team_name of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this SoccerStatsMembership.


        :param team_name: The team_name of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

    @property
    def team_area(self):
        """Gets the team_area of this SoccerStatsMembership.  # noqa: E501


        :return: The team_area of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._team_area

    @team_area.setter
    def team_area(self, team_area):
        """Sets the team_area of this SoccerStatsMembership.


        :param team_area: The team_area of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._team_area = team_area

    @property
    def active(self):
        """Gets the active of this SoccerStatsMembership.  # noqa: E501


        :return: The active of this SoccerStatsMembership.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SoccerStatsMembership.


        :param active: The active of this SoccerStatsMembership.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def start_date(self):
        """Gets the start_date of this SoccerStatsMembership.  # noqa: E501


        :return: The start_date of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SoccerStatsMembership.


        :param start_date: The start_date of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SoccerStatsMembership.  # noqa: E501


        :return: The end_date of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SoccerStatsMembership.


        :param end_date: The end_date of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def updated(self):
        """Gets the updated of this SoccerStatsMembership.  # noqa: E501


        :return: The updated of this SoccerStatsMembership.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SoccerStatsMembership.


        :param updated: The updated of this SoccerStatsMembership.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def jersey(self):
        """Gets the jersey of this SoccerStatsMembership.  # noqa: E501


        :return: The jersey of this SoccerStatsMembership.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this SoccerStatsMembership.


        :param jersey: The jersey of this SoccerStatsMembership.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

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
        if issubclass(SoccerStatsMembership, dict):
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
        if not isinstance(other, SoccerStatsMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
