# coding: utf-8

"""
    CWBB v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CwbbScoresConference(object):
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
        'conference_id': 'int',
        'name': 'str',
        'teams': 'list[CwbbScoresTeam]'
    }

    attribute_map = {
        'conference_id': 'ConferenceID',
        'name': 'Name',
        'teams': 'Teams'
    }

    def __init__(self, conference_id=None, name=None, teams=None):  # noqa: E501
        """CwbbScoresConference - a model defined in Swagger"""  # noqa: E501
        self._conference_id = None
        self._name = None
        self._teams = None
        self.discriminator = None
        if conference_id is not None:
            self.conference_id = conference_id
        if name is not None:
            self.name = name
        if teams is not None:
            self.teams = teams

    @property
    def conference_id(self):
        """Gets the conference_id of this CwbbScoresConference.  # noqa: E501


        :return: The conference_id of this CwbbScoresConference.  # noqa: E501
        :rtype: int
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this CwbbScoresConference.


        :param conference_id: The conference_id of this CwbbScoresConference.  # noqa: E501
        :type: int
        """

        self._conference_id = conference_id

    @property
    def name(self):
        """Gets the name of this CwbbScoresConference.  # noqa: E501


        :return: The name of this CwbbScoresConference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CwbbScoresConference.


        :param name: The name of this CwbbScoresConference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def teams(self):
        """Gets the teams of this CwbbScoresConference.  # noqa: E501


        :return: The teams of this CwbbScoresConference.  # noqa: E501
        :rtype: list[CwbbScoresTeam]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this CwbbScoresConference.


        :param teams: The teams of this CwbbScoresConference.  # noqa: E501
        :type: list[CwbbScoresTeam]
        """

        self._teams = teams

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
        if issubclass(CwbbScoresConference, dict):
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
        if not isinstance(other, CwbbScoresConference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
