# coding: utf-8

"""
    MMA v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MmaScoresFighterInfo(object):
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
        'fighter_id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'pre_fight_wins': 'int',
        'pre_fight_losses': 'int',
        'pre_fight_draws': 'int',
        'pre_fight_no_contests': 'int',
        'winner': 'bool',
        'moneyline': 'int',
        'active': 'bool'
    }

    attribute_map = {
        'fighter_id': 'FighterId',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'pre_fight_wins': 'PreFightWins',
        'pre_fight_losses': 'PreFightLosses',
        'pre_fight_draws': 'PreFightDraws',
        'pre_fight_no_contests': 'PreFightNoContests',
        'winner': 'Winner',
        'moneyline': 'Moneyline',
        'active': 'Active'
    }

    def __init__(self, fighter_id=None, first_name=None, last_name=None, pre_fight_wins=None, pre_fight_losses=None, pre_fight_draws=None, pre_fight_no_contests=None, winner=None, moneyline=None, active=None):  # noqa: E501
        """MmaScoresFighterInfo - a model defined in Swagger"""  # noqa: E501
        self._fighter_id = None
        self._first_name = None
        self._last_name = None
        self._pre_fight_wins = None
        self._pre_fight_losses = None
        self._pre_fight_draws = None
        self._pre_fight_no_contests = None
        self._winner = None
        self._moneyline = None
        self._active = None
        self.discriminator = None
        if fighter_id is not None:
            self.fighter_id = fighter_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if pre_fight_wins is not None:
            self.pre_fight_wins = pre_fight_wins
        if pre_fight_losses is not None:
            self.pre_fight_losses = pre_fight_losses
        if pre_fight_draws is not None:
            self.pre_fight_draws = pre_fight_draws
        if pre_fight_no_contests is not None:
            self.pre_fight_no_contests = pre_fight_no_contests
        if winner is not None:
            self.winner = winner
        if moneyline is not None:
            self.moneyline = moneyline
        if active is not None:
            self.active = active

    @property
    def fighter_id(self):
        """Gets the fighter_id of this MmaScoresFighterInfo.  # noqa: E501


        :return: The fighter_id of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._fighter_id

    @fighter_id.setter
    def fighter_id(self, fighter_id):
        """Sets the fighter_id of this MmaScoresFighterInfo.


        :param fighter_id: The fighter_id of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._fighter_id = fighter_id

    @property
    def first_name(self):
        """Gets the first_name of this MmaScoresFighterInfo.  # noqa: E501


        :return: The first_name of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MmaScoresFighterInfo.


        :param first_name: The first_name of this MmaScoresFighterInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MmaScoresFighterInfo.  # noqa: E501


        :return: The last_name of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MmaScoresFighterInfo.


        :param last_name: The last_name of this MmaScoresFighterInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def pre_fight_wins(self):
        """Gets the pre_fight_wins of this MmaScoresFighterInfo.  # noqa: E501


        :return: The pre_fight_wins of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_fight_wins

    @pre_fight_wins.setter
    def pre_fight_wins(self, pre_fight_wins):
        """Sets the pre_fight_wins of this MmaScoresFighterInfo.


        :param pre_fight_wins: The pre_fight_wins of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._pre_fight_wins = pre_fight_wins

    @property
    def pre_fight_losses(self):
        """Gets the pre_fight_losses of this MmaScoresFighterInfo.  # noqa: E501


        :return: The pre_fight_losses of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_fight_losses

    @pre_fight_losses.setter
    def pre_fight_losses(self, pre_fight_losses):
        """Sets the pre_fight_losses of this MmaScoresFighterInfo.


        :param pre_fight_losses: The pre_fight_losses of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._pre_fight_losses = pre_fight_losses

    @property
    def pre_fight_draws(self):
        """Gets the pre_fight_draws of this MmaScoresFighterInfo.  # noqa: E501


        :return: The pre_fight_draws of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_fight_draws

    @pre_fight_draws.setter
    def pre_fight_draws(self, pre_fight_draws):
        """Sets the pre_fight_draws of this MmaScoresFighterInfo.


        :param pre_fight_draws: The pre_fight_draws of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._pre_fight_draws = pre_fight_draws

    @property
    def pre_fight_no_contests(self):
        """Gets the pre_fight_no_contests of this MmaScoresFighterInfo.  # noqa: E501


        :return: The pre_fight_no_contests of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_fight_no_contests

    @pre_fight_no_contests.setter
    def pre_fight_no_contests(self, pre_fight_no_contests):
        """Sets the pre_fight_no_contests of this MmaScoresFighterInfo.


        :param pre_fight_no_contests: The pre_fight_no_contests of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._pre_fight_no_contests = pre_fight_no_contests

    @property
    def winner(self):
        """Gets the winner of this MmaScoresFighterInfo.  # noqa: E501


        :return: The winner of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this MmaScoresFighterInfo.


        :param winner: The winner of this MmaScoresFighterInfo.  # noqa: E501
        :type: bool
        """

        self._winner = winner

    @property
    def moneyline(self):
        """Gets the moneyline of this MmaScoresFighterInfo.  # noqa: E501


        :return: The moneyline of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: int
        """
        return self._moneyline

    @moneyline.setter
    def moneyline(self, moneyline):
        """Sets the moneyline of this MmaScoresFighterInfo.


        :param moneyline: The moneyline of this MmaScoresFighterInfo.  # noqa: E501
        :type: int
        """

        self._moneyline = moneyline

    @property
    def active(self):
        """Gets the active of this MmaScoresFighterInfo.  # noqa: E501


        :return: The active of this MmaScoresFighterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MmaScoresFighterInfo.


        :param active: The active of this MmaScoresFighterInfo.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(MmaScoresFighterInfo, dict):
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
        if not isinstance(other, MmaScoresFighterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
