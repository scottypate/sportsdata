# coding: utf-8

"""
    MLB v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MlbOddsBettingMarketResult(object):
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
        'betting_market_id': 'int',
        'betting_market_type_id': 'int',
        'betting_market_type': 'str',
        'betting_bet_type_id': 'int',
        'betting_bet_type': 'str',
        'betting_period_type_id': 'int',
        'betting_period_type': 'str',
        'name': 'str',
        'team_id': 'int',
        'team_key': 'str',
        'player_id': 'int',
        'player_name': 'str',
        'betting_outcome_results': 'list[MlbOddsBettingOutcomeResult]'
    }

    attribute_map = {
        'betting_market_id': 'BettingMarketID',
        'betting_market_type_id': 'BettingMarketTypeID',
        'betting_market_type': 'BettingMarketType',
        'betting_bet_type_id': 'BettingBetTypeID',
        'betting_bet_type': 'BettingBetType',
        'betting_period_type_id': 'BettingPeriodTypeID',
        'betting_period_type': 'BettingPeriodType',
        'name': 'Name',
        'team_id': 'TeamID',
        'team_key': 'TeamKey',
        'player_id': 'PlayerID',
        'player_name': 'PlayerName',
        'betting_outcome_results': 'BettingOutcomeResults'
    }

    def __init__(self, betting_market_id=None, betting_market_type_id=None, betting_market_type=None, betting_bet_type_id=None, betting_bet_type=None, betting_period_type_id=None, betting_period_type=None, name=None, team_id=None, team_key=None, player_id=None, player_name=None, betting_outcome_results=None):  # noqa: E501
        """MlbOddsBettingMarketResult - a model defined in Swagger"""  # noqa: E501
        self._betting_market_id = None
        self._betting_market_type_id = None
        self._betting_market_type = None
        self._betting_bet_type_id = None
        self._betting_bet_type = None
        self._betting_period_type_id = None
        self._betting_period_type = None
        self._name = None
        self._team_id = None
        self._team_key = None
        self._player_id = None
        self._player_name = None
        self._betting_outcome_results = None
        self.discriminator = None
        if betting_market_id is not None:
            self.betting_market_id = betting_market_id
        if betting_market_type_id is not None:
            self.betting_market_type_id = betting_market_type_id
        if betting_market_type is not None:
            self.betting_market_type = betting_market_type
        if betting_bet_type_id is not None:
            self.betting_bet_type_id = betting_bet_type_id
        if betting_bet_type is not None:
            self.betting_bet_type = betting_bet_type
        if betting_period_type_id is not None:
            self.betting_period_type_id = betting_period_type_id
        if betting_period_type is not None:
            self.betting_period_type = betting_period_type
        if name is not None:
            self.name = name
        if team_id is not None:
            self.team_id = team_id
        if team_key is not None:
            self.team_key = team_key
        if player_id is not None:
            self.player_id = player_id
        if player_name is not None:
            self.player_name = player_name
        if betting_outcome_results is not None:
            self.betting_outcome_results = betting_outcome_results

    @property
    def betting_market_id(self):
        """Gets the betting_market_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_market_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._betting_market_id

    @betting_market_id.setter
    def betting_market_id(self, betting_market_id):
        """Sets the betting_market_id of this MlbOddsBettingMarketResult.


        :param betting_market_id: The betting_market_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._betting_market_id = betting_market_id

    @property
    def betting_market_type_id(self):
        """Gets the betting_market_type_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_market_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._betting_market_type_id

    @betting_market_type_id.setter
    def betting_market_type_id(self, betting_market_type_id):
        """Sets the betting_market_type_id of this MlbOddsBettingMarketResult.


        :param betting_market_type_id: The betting_market_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._betting_market_type_id = betting_market_type_id

    @property
    def betting_market_type(self):
        """Gets the betting_market_type of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_market_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._betting_market_type

    @betting_market_type.setter
    def betting_market_type(self, betting_market_type):
        """Sets the betting_market_type of this MlbOddsBettingMarketResult.


        :param betting_market_type: The betting_market_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._betting_market_type = betting_market_type

    @property
    def betting_bet_type_id(self):
        """Gets the betting_bet_type_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_bet_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._betting_bet_type_id

    @betting_bet_type_id.setter
    def betting_bet_type_id(self, betting_bet_type_id):
        """Sets the betting_bet_type_id of this MlbOddsBettingMarketResult.


        :param betting_bet_type_id: The betting_bet_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._betting_bet_type_id = betting_bet_type_id

    @property
    def betting_bet_type(self):
        """Gets the betting_bet_type of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_bet_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._betting_bet_type

    @betting_bet_type.setter
    def betting_bet_type(self, betting_bet_type):
        """Sets the betting_bet_type of this MlbOddsBettingMarketResult.


        :param betting_bet_type: The betting_bet_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._betting_bet_type = betting_bet_type

    @property
    def betting_period_type_id(self):
        """Gets the betting_period_type_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_period_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._betting_period_type_id

    @betting_period_type_id.setter
    def betting_period_type_id(self, betting_period_type_id):
        """Sets the betting_period_type_id of this MlbOddsBettingMarketResult.


        :param betting_period_type_id: The betting_period_type_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._betting_period_type_id = betting_period_type_id

    @property
    def betting_period_type(self):
        """Gets the betting_period_type of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_period_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._betting_period_type

    @betting_period_type.setter
    def betting_period_type(self, betting_period_type):
        """Sets the betting_period_type of this MlbOddsBettingMarketResult.


        :param betting_period_type: The betting_period_type of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._betting_period_type = betting_period_type

    @property
    def name(self):
        """Gets the name of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The name of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MlbOddsBettingMarketResult.


        :param name: The name of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team_id(self):
        """Gets the team_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The team_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this MlbOddsBettingMarketResult.


        :param team_id: The team_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team_key(self):
        """Gets the team_key of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The team_key of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """Sets the team_key of this MlbOddsBettingMarketResult.


        :param team_key: The team_key of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._team_key = team_key

    @property
    def player_id(self):
        """Gets the player_id of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The player_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this MlbOddsBettingMarketResult.


        :param player_id: The player_id of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def player_name(self):
        """Gets the player_name of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The player_name of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: str
        """
        return self._player_name

    @player_name.setter
    def player_name(self, player_name):
        """Sets the player_name of this MlbOddsBettingMarketResult.


        :param player_name: The player_name of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: str
        """

        self._player_name = player_name

    @property
    def betting_outcome_results(self):
        """Gets the betting_outcome_results of this MlbOddsBettingMarketResult.  # noqa: E501


        :return: The betting_outcome_results of this MlbOddsBettingMarketResult.  # noqa: E501
        :rtype: list[MlbOddsBettingOutcomeResult]
        """
        return self._betting_outcome_results

    @betting_outcome_results.setter
    def betting_outcome_results(self, betting_outcome_results):
        """Sets the betting_outcome_results of this MlbOddsBettingMarketResult.


        :param betting_outcome_results: The betting_outcome_results of this MlbOddsBettingMarketResult.  # noqa: E501
        :type: list[MlbOddsBettingOutcomeResult]
        """

        self._betting_outcome_results = betting_outcome_results

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
        if issubclass(MlbOddsBettingMarketResult, dict):
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
        if not isinstance(other, MlbOddsBettingMarketResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
