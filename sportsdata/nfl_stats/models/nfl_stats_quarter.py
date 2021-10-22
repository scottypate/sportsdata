# coding: utf-8

"""
    NFL v3 Stats

    NFL rosters, player stats, team stats, and fantasy stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflStatsQuarter(object):
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
        'quarter_id': 'int',
        'score_id': 'int',
        'number': 'int',
        'name': 'str',
        'description': 'str',
        'away_team_score': 'int',
        'home_team_score': 'int',
        'updated': 'str',
        'created': 'str'
    }

    attribute_map = {
        'quarter_id': 'QuarterID',
        'score_id': 'ScoreID',
        'number': 'Number',
        'name': 'Name',
        'description': 'Description',
        'away_team_score': 'AwayTeamScore',
        'home_team_score': 'HomeTeamScore',
        'updated': 'Updated',
        'created': 'Created'
    }

    def __init__(self, quarter_id=None, score_id=None, number=None, name=None, description=None, away_team_score=None, home_team_score=None, updated=None, created=None):  # noqa: E501
        """NflStatsQuarter - a model defined in Swagger"""  # noqa: E501
        self._quarter_id = None
        self._score_id = None
        self._number = None
        self._name = None
        self._description = None
        self._away_team_score = None
        self._home_team_score = None
        self._updated = None
        self._created = None
        self.discriminator = None
        if quarter_id is not None:
            self.quarter_id = quarter_id
        if score_id is not None:
            self.score_id = score_id
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if away_team_score is not None:
            self.away_team_score = away_team_score
        if home_team_score is not None:
            self.home_team_score = home_team_score
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created

    @property
    def quarter_id(self):
        """Gets the quarter_id of this NflStatsQuarter.  # noqa: E501


        :return: The quarter_id of this NflStatsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._quarter_id

    @quarter_id.setter
    def quarter_id(self, quarter_id):
        """Sets the quarter_id of this NflStatsQuarter.


        :param quarter_id: The quarter_id of this NflStatsQuarter.  # noqa: E501
        :type: int
        """

        self._quarter_id = quarter_id

    @property
    def score_id(self):
        """Gets the score_id of this NflStatsQuarter.  # noqa: E501


        :return: The score_id of this NflStatsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._score_id

    @score_id.setter
    def score_id(self, score_id):
        """Sets the score_id of this NflStatsQuarter.


        :param score_id: The score_id of this NflStatsQuarter.  # noqa: E501
        :type: int
        """

        self._score_id = score_id

    @property
    def number(self):
        """Gets the number of this NflStatsQuarter.  # noqa: E501


        :return: The number of this NflStatsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this NflStatsQuarter.


        :param number: The number of this NflStatsQuarter.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this NflStatsQuarter.  # noqa: E501


        :return: The name of this NflStatsQuarter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NflStatsQuarter.


        :param name: The name of this NflStatsQuarter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this NflStatsQuarter.  # noqa: E501


        :return: The description of this NflStatsQuarter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NflStatsQuarter.


        :param description: The description of this NflStatsQuarter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def away_team_score(self):
        """Gets the away_team_score of this NflStatsQuarter.  # noqa: E501


        :return: The away_team_score of this NflStatsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this NflStatsQuarter.


        :param away_team_score: The away_team_score of this NflStatsQuarter.  # noqa: E501
        :type: int
        """

        self._away_team_score = away_team_score

    @property
    def home_team_score(self):
        """Gets the home_team_score of this NflStatsQuarter.  # noqa: E501


        :return: The home_team_score of this NflStatsQuarter.  # noqa: E501
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this NflStatsQuarter.


        :param home_team_score: The home_team_score of this NflStatsQuarter.  # noqa: E501
        :type: int
        """

        self._home_team_score = home_team_score

    @property
    def updated(self):
        """Gets the updated of this NflStatsQuarter.  # noqa: E501


        :return: The updated of this NflStatsQuarter.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NflStatsQuarter.


        :param updated: The updated of this NflStatsQuarter.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this NflStatsQuarter.  # noqa: E501


        :return: The created of this NflStatsQuarter.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NflStatsQuarter.


        :param created: The created of this NflStatsQuarter.  # noqa: E501
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
        if issubclass(NflStatsQuarter, dict):
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
        if not isinstance(other, NflStatsQuarter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
