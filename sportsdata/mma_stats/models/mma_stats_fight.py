# coding: utf-8

"""
    MMA v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MmaStatsFight(object):
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
        'fight_id': 'int',
        'order': 'int',
        'status': 'str',
        'weight_class': 'str',
        'card_segment': 'str',
        'referee': 'str',
        'rounds': 'int',
        'result_clock': 'int',
        'result_round': 'int',
        'result_type': 'str',
        'winner_id': 'int',
        'fighters': 'list[MmaStatsFighterInfo]',
        'active': 'bool'
    }

    attribute_map = {
        'fight_id': 'FightId',
        'order': 'Order',
        'status': 'Status',
        'weight_class': 'WeightClass',
        'card_segment': 'CardSegment',
        'referee': 'Referee',
        'rounds': 'Rounds',
        'result_clock': 'ResultClock',
        'result_round': 'ResultRound',
        'result_type': 'ResultType',
        'winner_id': 'WinnerId',
        'fighters': 'Fighters',
        'active': 'Active'
    }

    def __init__(self, fight_id=None, order=None, status=None, weight_class=None, card_segment=None, referee=None, rounds=None, result_clock=None, result_round=None, result_type=None, winner_id=None, fighters=None, active=None):  # noqa: E501
        """MmaStatsFight - a model defined in Swagger"""  # noqa: E501
        self._fight_id = None
        self._order = None
        self._status = None
        self._weight_class = None
        self._card_segment = None
        self._referee = None
        self._rounds = None
        self._result_clock = None
        self._result_round = None
        self._result_type = None
        self._winner_id = None
        self._fighters = None
        self._active = None
        self.discriminator = None
        if fight_id is not None:
            self.fight_id = fight_id
        if order is not None:
            self.order = order
        if status is not None:
            self.status = status
        if weight_class is not None:
            self.weight_class = weight_class
        if card_segment is not None:
            self.card_segment = card_segment
        if referee is not None:
            self.referee = referee
        if rounds is not None:
            self.rounds = rounds
        if result_clock is not None:
            self.result_clock = result_clock
        if result_round is not None:
            self.result_round = result_round
        if result_type is not None:
            self.result_type = result_type
        if winner_id is not None:
            self.winner_id = winner_id
        if fighters is not None:
            self.fighters = fighters
        if active is not None:
            self.active = active

    @property
    def fight_id(self):
        """Gets the fight_id of this MmaStatsFight.  # noqa: E501


        :return: The fight_id of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._fight_id

    @fight_id.setter
    def fight_id(self, fight_id):
        """Sets the fight_id of this MmaStatsFight.


        :param fight_id: The fight_id of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._fight_id = fight_id

    @property
    def order(self):
        """Gets the order of this MmaStatsFight.  # noqa: E501


        :return: The order of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this MmaStatsFight.


        :param order: The order of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def status(self):
        """Gets the status of this MmaStatsFight.  # noqa: E501


        :return: The status of this MmaStatsFight.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MmaStatsFight.


        :param status: The status of this MmaStatsFight.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def weight_class(self):
        """Gets the weight_class of this MmaStatsFight.  # noqa: E501


        :return: The weight_class of this MmaStatsFight.  # noqa: E501
        :rtype: str
        """
        return self._weight_class

    @weight_class.setter
    def weight_class(self, weight_class):
        """Sets the weight_class of this MmaStatsFight.


        :param weight_class: The weight_class of this MmaStatsFight.  # noqa: E501
        :type: str
        """

        self._weight_class = weight_class

    @property
    def card_segment(self):
        """Gets the card_segment of this MmaStatsFight.  # noqa: E501


        :return: The card_segment of this MmaStatsFight.  # noqa: E501
        :rtype: str
        """
        return self._card_segment

    @card_segment.setter
    def card_segment(self, card_segment):
        """Sets the card_segment of this MmaStatsFight.


        :param card_segment: The card_segment of this MmaStatsFight.  # noqa: E501
        :type: str
        """

        self._card_segment = card_segment

    @property
    def referee(self):
        """Gets the referee of this MmaStatsFight.  # noqa: E501


        :return: The referee of this MmaStatsFight.  # noqa: E501
        :rtype: str
        """
        return self._referee

    @referee.setter
    def referee(self, referee):
        """Sets the referee of this MmaStatsFight.


        :param referee: The referee of this MmaStatsFight.  # noqa: E501
        :type: str
        """

        self._referee = referee

    @property
    def rounds(self):
        """Gets the rounds of this MmaStatsFight.  # noqa: E501


        :return: The rounds of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        """Sets the rounds of this MmaStatsFight.


        :param rounds: The rounds of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._rounds = rounds

    @property
    def result_clock(self):
        """Gets the result_clock of this MmaStatsFight.  # noqa: E501


        :return: The result_clock of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._result_clock

    @result_clock.setter
    def result_clock(self, result_clock):
        """Sets the result_clock of this MmaStatsFight.


        :param result_clock: The result_clock of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._result_clock = result_clock

    @property
    def result_round(self):
        """Gets the result_round of this MmaStatsFight.  # noqa: E501


        :return: The result_round of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._result_round

    @result_round.setter
    def result_round(self, result_round):
        """Sets the result_round of this MmaStatsFight.


        :param result_round: The result_round of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._result_round = result_round

    @property
    def result_type(self):
        """Gets the result_type of this MmaStatsFight.  # noqa: E501


        :return: The result_type of this MmaStatsFight.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this MmaStatsFight.


        :param result_type: The result_type of this MmaStatsFight.  # noqa: E501
        :type: str
        """

        self._result_type = result_type

    @property
    def winner_id(self):
        """Gets the winner_id of this MmaStatsFight.  # noqa: E501


        :return: The winner_id of this MmaStatsFight.  # noqa: E501
        :rtype: int
        """
        return self._winner_id

    @winner_id.setter
    def winner_id(self, winner_id):
        """Sets the winner_id of this MmaStatsFight.


        :param winner_id: The winner_id of this MmaStatsFight.  # noqa: E501
        :type: int
        """

        self._winner_id = winner_id

    @property
    def fighters(self):
        """Gets the fighters of this MmaStatsFight.  # noqa: E501


        :return: The fighters of this MmaStatsFight.  # noqa: E501
        :rtype: list[MmaStatsFighterInfo]
        """
        return self._fighters

    @fighters.setter
    def fighters(self, fighters):
        """Sets the fighters of this MmaStatsFight.


        :param fighters: The fighters of this MmaStatsFight.  # noqa: E501
        :type: list[MmaStatsFighterInfo]
        """

        self._fighters = fighters

    @property
    def active(self):
        """Gets the active of this MmaStatsFight.  # noqa: E501


        :return: The active of this MmaStatsFight.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MmaStatsFight.


        :param active: The active of this MmaStatsFight.  # noqa: E501
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
        if issubclass(MmaStatsFight, dict):
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
        if not isinstance(other, MmaStatsFight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
