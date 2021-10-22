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

class SoccerStatsPlayoffAggregateScore(object):
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
        'team_a_id': 'int',
        'team_a_aggregate_score': 'int',
        'team_b_id': 'int',
        'team_b_aggregate_score': 'int',
        'winning_team_id': 'int',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'team_a_id': 'TeamA_Id',
        'team_a_aggregate_score': 'TeamA_AggregateScore',
        'team_b_id': 'TeamB_Id',
        'team_b_aggregate_score': 'TeamB_AggregateScore',
        'winning_team_id': 'WinningTeamId',
        'created': 'Created',
        'updated': 'Updated'
    }

    def __init__(self, team_a_id=None, team_a_aggregate_score=None, team_b_id=None, team_b_aggregate_score=None, winning_team_id=None, created=None, updated=None):  # noqa: E501
        """SoccerStatsPlayoffAggregateScore - a model defined in Swagger"""  # noqa: E501
        self._team_a_id = None
        self._team_a_aggregate_score = None
        self._team_b_id = None
        self._team_b_aggregate_score = None
        self._winning_team_id = None
        self._created = None
        self._updated = None
        self.discriminator = None
        if team_a_id is not None:
            self.team_a_id = team_a_id
        if team_a_aggregate_score is not None:
            self.team_a_aggregate_score = team_a_aggregate_score
        if team_b_id is not None:
            self.team_b_id = team_b_id
        if team_b_aggregate_score is not None:
            self.team_b_aggregate_score = team_b_aggregate_score
        if winning_team_id is not None:
            self.winning_team_id = winning_team_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def team_a_id(self):
        """Gets the team_a_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The team_a_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: int
        """
        return self._team_a_id

    @team_a_id.setter
    def team_a_id(self, team_a_id):
        """Sets the team_a_id of this SoccerStatsPlayoffAggregateScore.


        :param team_a_id: The team_a_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: int
        """

        self._team_a_id = team_a_id

    @property
    def team_a_aggregate_score(self):
        """Gets the team_a_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The team_a_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: int
        """
        return self._team_a_aggregate_score

    @team_a_aggregate_score.setter
    def team_a_aggregate_score(self, team_a_aggregate_score):
        """Sets the team_a_aggregate_score of this SoccerStatsPlayoffAggregateScore.


        :param team_a_aggregate_score: The team_a_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: int
        """

        self._team_a_aggregate_score = team_a_aggregate_score

    @property
    def team_b_id(self):
        """Gets the team_b_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The team_b_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: int
        """
        return self._team_b_id

    @team_b_id.setter
    def team_b_id(self, team_b_id):
        """Sets the team_b_id of this SoccerStatsPlayoffAggregateScore.


        :param team_b_id: The team_b_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: int
        """

        self._team_b_id = team_b_id

    @property
    def team_b_aggregate_score(self):
        """Gets the team_b_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The team_b_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: int
        """
        return self._team_b_aggregate_score

    @team_b_aggregate_score.setter
    def team_b_aggregate_score(self, team_b_aggregate_score):
        """Sets the team_b_aggregate_score of this SoccerStatsPlayoffAggregateScore.


        :param team_b_aggregate_score: The team_b_aggregate_score of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: int
        """

        self._team_b_aggregate_score = team_b_aggregate_score

    @property
    def winning_team_id(self):
        """Gets the winning_team_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The winning_team_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: int
        """
        return self._winning_team_id

    @winning_team_id.setter
    def winning_team_id(self, winning_team_id):
        """Sets the winning_team_id of this SoccerStatsPlayoffAggregateScore.


        :param winning_team_id: The winning_team_id of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: int
        """

        self._winning_team_id = winning_team_id

    @property
    def created(self):
        """Gets the created of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The created of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SoccerStatsPlayoffAggregateScore.


        :param created: The created of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this SoccerStatsPlayoffAggregateScore.  # noqa: E501


        :return: The updated of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SoccerStatsPlayoffAggregateScore.


        :param updated: The updated of this SoccerStatsPlayoffAggregateScore.  # noqa: E501
        :type: str
        """

        self._updated = updated

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
        if issubclass(SoccerStatsPlayoffAggregateScore, dict):
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
        if not isinstance(other, SoccerStatsPlayoffAggregateScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other