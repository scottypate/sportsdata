# coding: utf-8

"""
    Golf v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GolfV2DfsSlateTournament(object):
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
        'slate_tournament_id': 'int',
        'slate_id': 'int',
        'tournament_id': 'int',
        'tournament': 'GolfV2Tournament',
        'operator_tournament_id': 'int',
        'removed_by_operator': 'bool'
    }

    attribute_map = {
        'slate_tournament_id': 'SlateTournamentID',
        'slate_id': 'SlateID',
        'tournament_id': 'TournamentID',
        'tournament': 'Tournament',
        'operator_tournament_id': 'OperatorTournamentID',
        'removed_by_operator': 'RemovedByOperator'
    }

    def __init__(self, slate_tournament_id=None, slate_id=None, tournament_id=None, tournament=None, operator_tournament_id=None, removed_by_operator=None):  # noqa: E501
        """GolfV2DfsSlateTournament - a model defined in Swagger"""  # noqa: E501
        self._slate_tournament_id = None
        self._slate_id = None
        self._tournament_id = None
        self._tournament = None
        self._operator_tournament_id = None
        self._removed_by_operator = None
        self.discriminator = None
        if slate_tournament_id is not None:
            self.slate_tournament_id = slate_tournament_id
        if slate_id is not None:
            self.slate_id = slate_id
        if tournament_id is not None:
            self.tournament_id = tournament_id
        if tournament is not None:
            self.tournament = tournament
        if operator_tournament_id is not None:
            self.operator_tournament_id = operator_tournament_id
        if removed_by_operator is not None:
            self.removed_by_operator = removed_by_operator

    @property
    def slate_tournament_id(self):
        """Gets the slate_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The slate_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: int
        """
        return self._slate_tournament_id

    @slate_tournament_id.setter
    def slate_tournament_id(self, slate_tournament_id):
        """Sets the slate_tournament_id of this GolfV2DfsSlateTournament.


        :param slate_tournament_id: The slate_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: int
        """

        self._slate_tournament_id = slate_tournament_id

    @property
    def slate_id(self):
        """Gets the slate_id of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The slate_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: int
        """
        return self._slate_id

    @slate_id.setter
    def slate_id(self, slate_id):
        """Sets the slate_id of this GolfV2DfsSlateTournament.


        :param slate_id: The slate_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: int
        """

        self._slate_id = slate_id

    @property
    def tournament_id(self):
        """Gets the tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this GolfV2DfsSlateTournament.


        :param tournament_id: The tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: int
        """

        self._tournament_id = tournament_id

    @property
    def tournament(self):
        """Gets the tournament of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The tournament of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: GolfV2Tournament
        """
        return self._tournament

    @tournament.setter
    def tournament(self, tournament):
        """Sets the tournament of this GolfV2DfsSlateTournament.


        :param tournament: The tournament of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: GolfV2Tournament
        """

        self._tournament = tournament

    @property
    def operator_tournament_id(self):
        """Gets the operator_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The operator_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: int
        """
        return self._operator_tournament_id

    @operator_tournament_id.setter
    def operator_tournament_id(self, operator_tournament_id):
        """Sets the operator_tournament_id of this GolfV2DfsSlateTournament.


        :param operator_tournament_id: The operator_tournament_id of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: int
        """

        self._operator_tournament_id = operator_tournament_id

    @property
    def removed_by_operator(self):
        """Gets the removed_by_operator of this GolfV2DfsSlateTournament.  # noqa: E501


        :return: The removed_by_operator of this GolfV2DfsSlateTournament.  # noqa: E501
        :rtype: bool
        """
        return self._removed_by_operator

    @removed_by_operator.setter
    def removed_by_operator(self, removed_by_operator):
        """Sets the removed_by_operator of this GolfV2DfsSlateTournament.


        :param removed_by_operator: The removed_by_operator of this GolfV2DfsSlateTournament.  # noqa: E501
        :type: bool
        """

        self._removed_by_operator = removed_by_operator

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
        if issubclass(GolfV2DfsSlateTournament, dict):
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
        if not isinstance(other, GolfV2DfsSlateTournament):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
