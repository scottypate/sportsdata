# coding: utf-8

"""
    LoL v3 Stats

    LoL v3 Stats  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LolStatsMatchBan(object):
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
        'match_id': 'int',
        'team_id': 'int',
        'champion_id': 'int',
        'champion': 'LolStatsChampionInfo'
    }

    attribute_map = {
        'match_id': 'MatchId',
        'team_id': 'TeamId',
        'champion_id': 'ChampionId',
        'champion': 'Champion'
    }

    def __init__(self, match_id=None, team_id=None, champion_id=None, champion=None):  # noqa: E501
        """LolStatsMatchBan - a model defined in Swagger"""  # noqa: E501
        self._match_id = None
        self._team_id = None
        self._champion_id = None
        self._champion = None
        self.discriminator = None
        if match_id is not None:
            self.match_id = match_id
        if team_id is not None:
            self.team_id = team_id
        if champion_id is not None:
            self.champion_id = champion_id
        if champion is not None:
            self.champion = champion

    @property
    def match_id(self):
        """Gets the match_id of this LolStatsMatchBan.  # noqa: E501


        :return: The match_id of this LolStatsMatchBan.  # noqa: E501
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this LolStatsMatchBan.


        :param match_id: The match_id of this LolStatsMatchBan.  # noqa: E501
        :type: int
        """

        self._match_id = match_id

    @property
    def team_id(self):
        """Gets the team_id of this LolStatsMatchBan.  # noqa: E501


        :return: The team_id of this LolStatsMatchBan.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this LolStatsMatchBan.


        :param team_id: The team_id of this LolStatsMatchBan.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def champion_id(self):
        """Gets the champion_id of this LolStatsMatchBan.  # noqa: E501


        :return: The champion_id of this LolStatsMatchBan.  # noqa: E501
        :rtype: int
        """
        return self._champion_id

    @champion_id.setter
    def champion_id(self, champion_id):
        """Sets the champion_id of this LolStatsMatchBan.


        :param champion_id: The champion_id of this LolStatsMatchBan.  # noqa: E501
        :type: int
        """

        self._champion_id = champion_id

    @property
    def champion(self):
        """Gets the champion of this LolStatsMatchBan.  # noqa: E501


        :return: The champion of this LolStatsMatchBan.  # noqa: E501
        :rtype: LolStatsChampionInfo
        """
        return self._champion

    @champion.setter
    def champion(self, champion):
        """Sets the champion of this LolStatsMatchBan.


        :param champion: The champion of this LolStatsMatchBan.  # noqa: E501
        :type: LolStatsChampionInfo
        """

        self._champion = champion

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
        if issubclass(LolStatsMatchBan, dict):
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
        if not isinstance(other, LolStatsMatchBan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
