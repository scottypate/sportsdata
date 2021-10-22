# coding: utf-8

"""
    MLB v3 Stats

    MLB scores, stats, and news API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbStatsInning(object):
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
        'inning_id': 'int',
        'game_id': 'int',
        'inning_number': 'int',
        'away_team_runs': 'int',
        'home_team_runs': 'int'
    }

    attribute_map = {
        'inning_id': 'InningID',
        'game_id': 'GameID',
        'inning_number': 'InningNumber',
        'away_team_runs': 'AwayTeamRuns',
        'home_team_runs': 'HomeTeamRuns'
    }

    def __init__(self, inning_id=None, game_id=None, inning_number=None, away_team_runs=None, home_team_runs=None):  # noqa: E501
        """MlbStatsInning - a model defined in Swagger"""  # noqa: E501
        self._inning_id = None
        self._game_id = None
        self._inning_number = None
        self._away_team_runs = None
        self._home_team_runs = None
        self.discriminator = None
        if inning_id is not None:
            self.inning_id = inning_id
        if game_id is not None:
            self.game_id = game_id
        if inning_number is not None:
            self.inning_number = inning_number
        if away_team_runs is not None:
            self.away_team_runs = away_team_runs
        if home_team_runs is not None:
            self.home_team_runs = home_team_runs

    @property
    def inning_id(self):
        """Gets the inning_id of this MlbStatsInning.  # noqa: E501


        :return: The inning_id of this MlbStatsInning.  # noqa: E501
        :rtype: int
        """
        return self._inning_id

    @inning_id.setter
    def inning_id(self, inning_id):
        """Sets the inning_id of this MlbStatsInning.


        :param inning_id: The inning_id of this MlbStatsInning.  # noqa: E501
        :type: int
        """

        self._inning_id = inning_id

    @property
    def game_id(self):
        """Gets the game_id of this MlbStatsInning.  # noqa: E501


        :return: The game_id of this MlbStatsInning.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this MlbStatsInning.


        :param game_id: The game_id of this MlbStatsInning.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def inning_number(self):
        """Gets the inning_number of this MlbStatsInning.  # noqa: E501


        :return: The inning_number of this MlbStatsInning.  # noqa: E501
        :rtype: int
        """
        return self._inning_number

    @inning_number.setter
    def inning_number(self, inning_number):
        """Sets the inning_number of this MlbStatsInning.


        :param inning_number: The inning_number of this MlbStatsInning.  # noqa: E501
        :type: int
        """

        self._inning_number = inning_number

    @property
    def away_team_runs(self):
        """Gets the away_team_runs of this MlbStatsInning.  # noqa: E501


        :return: The away_team_runs of this MlbStatsInning.  # noqa: E501
        :rtype: int
        """
        return self._away_team_runs

    @away_team_runs.setter
    def away_team_runs(self, away_team_runs):
        """Sets the away_team_runs of this MlbStatsInning.


        :param away_team_runs: The away_team_runs of this MlbStatsInning.  # noqa: E501
        :type: int
        """

        self._away_team_runs = away_team_runs

    @property
    def home_team_runs(self):
        """Gets the home_team_runs of this MlbStatsInning.  # noqa: E501


        :return: The home_team_runs of this MlbStatsInning.  # noqa: E501
        :rtype: int
        """
        return self._home_team_runs

    @home_team_runs.setter
    def home_team_runs(self, home_team_runs):
        """Sets the home_team_runs of this MlbStatsInning.


        :param home_team_runs: The home_team_runs of this MlbStatsInning.  # noqa: E501
        :type: int
        """

        self._home_team_runs = home_team_runs

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
        if issubclass(MlbStatsInning, dict):
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
        if not isinstance(other, MlbStatsInning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
