# coding: utf-8

"""
    CS:GO v3 Stats

    CS:GO v3 Stats  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CsgoStatsMap(object):
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
        'number': 'int',
        'name': 'str',
        'status': 'str',
        'current_round': 'int',
        'team_a_score': 'int',
        'team_b_score': 'int',
        'leaderboards': 'list[CsgoStatsLeaderboard]'
    }

    attribute_map = {
        'number': 'Number',
        'name': 'Name',
        'status': 'Status',
        'current_round': 'CurrentRound',
        'team_a_score': 'TeamAScore',
        'team_b_score': 'TeamBScore',
        'leaderboards': 'Leaderboards'
    }

    def __init__(self, number=None, name=None, status=None, current_round=None, team_a_score=None, team_b_score=None, leaderboards=None):  # noqa: E501
        """CsgoStatsMap - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._name = None
        self._status = None
        self._current_round = None
        self._team_a_score = None
        self._team_b_score = None
        self._leaderboards = None
        self.discriminator = None
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if current_round is not None:
            self.current_round = current_round
        if team_a_score is not None:
            self.team_a_score = team_a_score
        if team_b_score is not None:
            self.team_b_score = team_b_score
        if leaderboards is not None:
            self.leaderboards = leaderboards

    @property
    def number(self):
        """Gets the number of this CsgoStatsMap.  # noqa: E501


        :return: The number of this CsgoStatsMap.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CsgoStatsMap.


        :param number: The number of this CsgoStatsMap.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this CsgoStatsMap.  # noqa: E501


        :return: The name of this CsgoStatsMap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CsgoStatsMap.


        :param name: The name of this CsgoStatsMap.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this CsgoStatsMap.  # noqa: E501


        :return: The status of this CsgoStatsMap.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CsgoStatsMap.


        :param status: The status of this CsgoStatsMap.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def current_round(self):
        """Gets the current_round of this CsgoStatsMap.  # noqa: E501


        :return: The current_round of this CsgoStatsMap.  # noqa: E501
        :rtype: int
        """
        return self._current_round

    @current_round.setter
    def current_round(self, current_round):
        """Sets the current_round of this CsgoStatsMap.


        :param current_round: The current_round of this CsgoStatsMap.  # noqa: E501
        :type: int
        """

        self._current_round = current_round

    @property
    def team_a_score(self):
        """Gets the team_a_score of this CsgoStatsMap.  # noqa: E501


        :return: The team_a_score of this CsgoStatsMap.  # noqa: E501
        :rtype: int
        """
        return self._team_a_score

    @team_a_score.setter
    def team_a_score(self, team_a_score):
        """Sets the team_a_score of this CsgoStatsMap.


        :param team_a_score: The team_a_score of this CsgoStatsMap.  # noqa: E501
        :type: int
        """

        self._team_a_score = team_a_score

    @property
    def team_b_score(self):
        """Gets the team_b_score of this CsgoStatsMap.  # noqa: E501


        :return: The team_b_score of this CsgoStatsMap.  # noqa: E501
        :rtype: int
        """
        return self._team_b_score

    @team_b_score.setter
    def team_b_score(self, team_b_score):
        """Sets the team_b_score of this CsgoStatsMap.


        :param team_b_score: The team_b_score of this CsgoStatsMap.  # noqa: E501
        :type: int
        """

        self._team_b_score = team_b_score

    @property
    def leaderboards(self):
        """Gets the leaderboards of this CsgoStatsMap.  # noqa: E501


        :return: The leaderboards of this CsgoStatsMap.  # noqa: E501
        :rtype: list[CsgoStatsLeaderboard]
        """
        return self._leaderboards

    @leaderboards.setter
    def leaderboards(self, leaderboards):
        """Sets the leaderboards of this CsgoStatsMap.


        :param leaderboards: The leaderboards of this CsgoStatsMap.  # noqa: E501
        :type: list[CsgoStatsLeaderboard]
        """

        self._leaderboards = leaderboards

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
        if issubclass(CsgoStatsMap, dict):
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
        if not isinstance(other, CsgoStatsMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other