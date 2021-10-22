# coding: utf-8

"""
    CFB v3 Odds

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CfbOddsBettingOutcome(object):
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
        'betting_outcome_id': 'int',
        'betting_market_id': 'int',
        'sports_book': 'CfbOddsSportsbook',
        'betting_outcome_type_id': 'int',
        'betting_outcome_type': 'str',
        'payout_american': 'int',
        'payout_decimal': 'float',
        'value': 'float',
        'participant': 'str',
        'is_available': 'bool',
        'is_alternate': 'bool',
        'created': 'str',
        'updated': 'str',
        'unlisted': 'str',
        'team_id': 'int',
        'player_id': 'int',
        'global_team_id': 'int',
        'sportsbook_url': 'str'
    }

    attribute_map = {
        'betting_outcome_id': 'BettingOutcomeID',
        'betting_market_id': 'BettingMarketID',
        'sports_book': 'SportsBook',
        'betting_outcome_type_id': 'BettingOutcomeTypeID',
        'betting_outcome_type': 'BettingOutcomeType',
        'payout_american': 'PayoutAmerican',
        'payout_decimal': 'PayoutDecimal',
        'value': 'Value',
        'participant': 'Participant',
        'is_available': 'IsAvailable',
        'is_alternate': 'IsAlternate',
        'created': 'Created',
        'updated': 'Updated',
        'unlisted': 'Unlisted',
        'team_id': 'TeamID',
        'player_id': 'PlayerID',
        'global_team_id': 'GlobalTeamID',
        'sportsbook_url': 'SportsbookUrl'
    }

    def __init__(self, betting_outcome_id=None, betting_market_id=None, sports_book=None, betting_outcome_type_id=None, betting_outcome_type=None, payout_american=None, payout_decimal=None, value=None, participant=None, is_available=None, is_alternate=None, created=None, updated=None, unlisted=None, team_id=None, player_id=None, global_team_id=None, sportsbook_url=None):  # noqa: E501
        """CfbOddsBettingOutcome - a model defined in Swagger"""  # noqa: E501
        self._betting_outcome_id = None
        self._betting_market_id = None
        self._sports_book = None
        self._betting_outcome_type_id = None
        self._betting_outcome_type = None
        self._payout_american = None
        self._payout_decimal = None
        self._value = None
        self._participant = None
        self._is_available = None
        self._is_alternate = None
        self._created = None
        self._updated = None
        self._unlisted = None
        self._team_id = None
        self._player_id = None
        self._global_team_id = None
        self._sportsbook_url = None
        self.discriminator = None
        if betting_outcome_id is not None:
            self.betting_outcome_id = betting_outcome_id
        if betting_market_id is not None:
            self.betting_market_id = betting_market_id
        if sports_book is not None:
            self.sports_book = sports_book
        if betting_outcome_type_id is not None:
            self.betting_outcome_type_id = betting_outcome_type_id
        if betting_outcome_type is not None:
            self.betting_outcome_type = betting_outcome_type
        if payout_american is not None:
            self.payout_american = payout_american
        if payout_decimal is not None:
            self.payout_decimal = payout_decimal
        if value is not None:
            self.value = value
        if participant is not None:
            self.participant = participant
        if is_available is not None:
            self.is_available = is_available
        if is_alternate is not None:
            self.is_alternate = is_alternate
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if unlisted is not None:
            self.unlisted = unlisted
        if team_id is not None:
            self.team_id = team_id
        if player_id is not None:
            self.player_id = player_id
        if global_team_id is not None:
            self.global_team_id = global_team_id
        if sportsbook_url is not None:
            self.sportsbook_url = sportsbook_url

    @property
    def betting_outcome_id(self):
        """Gets the betting_outcome_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The betting_outcome_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._betting_outcome_id

    @betting_outcome_id.setter
    def betting_outcome_id(self, betting_outcome_id):
        """Sets the betting_outcome_id of this CfbOddsBettingOutcome.


        :param betting_outcome_id: The betting_outcome_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._betting_outcome_id = betting_outcome_id

    @property
    def betting_market_id(self):
        """Gets the betting_market_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The betting_market_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._betting_market_id

    @betting_market_id.setter
    def betting_market_id(self, betting_market_id):
        """Sets the betting_market_id of this CfbOddsBettingOutcome.


        :param betting_market_id: The betting_market_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._betting_market_id = betting_market_id

    @property
    def sports_book(self):
        """Gets the sports_book of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The sports_book of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: CfbOddsSportsbook
        """
        return self._sports_book

    @sports_book.setter
    def sports_book(self, sports_book):
        """Sets the sports_book of this CfbOddsBettingOutcome.


        :param sports_book: The sports_book of this CfbOddsBettingOutcome.  # noqa: E501
        :type: CfbOddsSportsbook
        """

        self._sports_book = sports_book

    @property
    def betting_outcome_type_id(self):
        """Gets the betting_outcome_type_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The betting_outcome_type_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._betting_outcome_type_id

    @betting_outcome_type_id.setter
    def betting_outcome_type_id(self, betting_outcome_type_id):
        """Sets the betting_outcome_type_id of this CfbOddsBettingOutcome.


        :param betting_outcome_type_id: The betting_outcome_type_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._betting_outcome_type_id = betting_outcome_type_id

    @property
    def betting_outcome_type(self):
        """Gets the betting_outcome_type of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The betting_outcome_type of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._betting_outcome_type

    @betting_outcome_type.setter
    def betting_outcome_type(self, betting_outcome_type):
        """Sets the betting_outcome_type of this CfbOddsBettingOutcome.


        :param betting_outcome_type: The betting_outcome_type of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._betting_outcome_type = betting_outcome_type

    @property
    def payout_american(self):
        """Gets the payout_american of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The payout_american of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._payout_american

    @payout_american.setter
    def payout_american(self, payout_american):
        """Sets the payout_american of this CfbOddsBettingOutcome.


        :param payout_american: The payout_american of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._payout_american = payout_american

    @property
    def payout_decimal(self):
        """Gets the payout_decimal of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The payout_decimal of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: float
        """
        return self._payout_decimal

    @payout_decimal.setter
    def payout_decimal(self, payout_decimal):
        """Sets the payout_decimal of this CfbOddsBettingOutcome.


        :param payout_decimal: The payout_decimal of this CfbOddsBettingOutcome.  # noqa: E501
        :type: float
        """

        self._payout_decimal = payout_decimal

    @property
    def value(self):
        """Gets the value of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The value of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CfbOddsBettingOutcome.


        :param value: The value of this CfbOddsBettingOutcome.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def participant(self):
        """Gets the participant of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The participant of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this CfbOddsBettingOutcome.


        :param participant: The participant of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._participant = participant

    @property
    def is_available(self):
        """Gets the is_available of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The is_available of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this CfbOddsBettingOutcome.


        :param is_available: The is_available of this CfbOddsBettingOutcome.  # noqa: E501
        :type: bool
        """

        self._is_available = is_available

    @property
    def is_alternate(self):
        """Gets the is_alternate of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The is_alternate of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: bool
        """
        return self._is_alternate

    @is_alternate.setter
    def is_alternate(self, is_alternate):
        """Sets the is_alternate of this CfbOddsBettingOutcome.


        :param is_alternate: The is_alternate of this CfbOddsBettingOutcome.  # noqa: E501
        :type: bool
        """

        self._is_alternate = is_alternate

    @property
    def created(self):
        """Gets the created of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The created of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CfbOddsBettingOutcome.


        :param created: The created of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The updated of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CfbOddsBettingOutcome.


        :param updated: The updated of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def unlisted(self):
        """Gets the unlisted of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The unlisted of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._unlisted

    @unlisted.setter
    def unlisted(self, unlisted):
        """Sets the unlisted of this CfbOddsBettingOutcome.


        :param unlisted: The unlisted of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._unlisted = unlisted

    @property
    def team_id(self):
        """Gets the team_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The team_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this CfbOddsBettingOutcome.


        :param team_id: The team_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def player_id(self):
        """Gets the player_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The player_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this CfbOddsBettingOutcome.


        :param player_id: The player_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def global_team_id(self):
        """Gets the global_team_id of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The global_team_id of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this CfbOddsBettingOutcome.


        :param global_team_id: The global_team_id of this CfbOddsBettingOutcome.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

    @property
    def sportsbook_url(self):
        """Gets the sportsbook_url of this CfbOddsBettingOutcome.  # noqa: E501


        :return: The sportsbook_url of this CfbOddsBettingOutcome.  # noqa: E501
        :rtype: str
        """
        return self._sportsbook_url

    @sportsbook_url.setter
    def sportsbook_url(self, sportsbook_url):
        """Sets the sportsbook_url of this CfbOddsBettingOutcome.


        :param sportsbook_url: The sportsbook_url of this CfbOddsBettingOutcome.  # noqa: E501
        :type: str
        """

        self._sportsbook_url = sportsbook_url

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
        if issubclass(CfbOddsBettingOutcome, dict):
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
        if not isinstance(other, CfbOddsBettingOutcome):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
