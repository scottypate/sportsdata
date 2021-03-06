# coding: utf-8

"""
    CWBB v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CwbbScoresTeam(object):
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
        'team_id': 'int',
        'key': 'str',
        'active': 'bool',
        'school': 'str',
        'name': 'str',
        'ap_rank': 'int',
        'wins': 'int',
        'losses': 'int',
        'conference_wins': 'int',
        'conference_losses': 'int',
        'global_team_id': 'int',
        'conference_id': 'int',
        'conference': 'str',
        'team_logo_url': 'str',
        'short_display_name': 'str'
    }

    attribute_map = {
        'team_id': 'TeamID',
        'key': 'Key',
        'active': 'Active',
        'school': 'School',
        'name': 'Name',
        'ap_rank': 'ApRank',
        'wins': 'Wins',
        'losses': 'Losses',
        'conference_wins': 'ConferenceWins',
        'conference_losses': 'ConferenceLosses',
        'global_team_id': 'GlobalTeamID',
        'conference_id': 'ConferenceID',
        'conference': 'Conference',
        'team_logo_url': 'TeamLogoUrl',
        'short_display_name': 'ShortDisplayName'
    }

    def __init__(self, team_id=None, key=None, active=None, school=None, name=None, ap_rank=None, wins=None, losses=None, conference_wins=None, conference_losses=None, global_team_id=None, conference_id=None, conference=None, team_logo_url=None, short_display_name=None):  # noqa: E501
        """CwbbScoresTeam - a model defined in Swagger"""  # noqa: E501
        self._team_id = None
        self._key = None
        self._active = None
        self._school = None
        self._name = None
        self._ap_rank = None
        self._wins = None
        self._losses = None
        self._conference_wins = None
        self._conference_losses = None
        self._global_team_id = None
        self._conference_id = None
        self._conference = None
        self._team_logo_url = None
        self._short_display_name = None
        self.discriminator = None
        if team_id is not None:
            self.team_id = team_id
        if key is not None:
            self.key = key
        if active is not None:
            self.active = active
        if school is not None:
            self.school = school
        if name is not None:
            self.name = name
        if ap_rank is not None:
            self.ap_rank = ap_rank
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if conference_wins is not None:
            self.conference_wins = conference_wins
        if conference_losses is not None:
            self.conference_losses = conference_losses
        if global_team_id is not None:
            self.global_team_id = global_team_id
        if conference_id is not None:
            self.conference_id = conference_id
        if conference is not None:
            self.conference = conference
        if team_logo_url is not None:
            self.team_logo_url = team_logo_url
        if short_display_name is not None:
            self.short_display_name = short_display_name

    @property
    def team_id(self):
        """Gets the team_id of this CwbbScoresTeam.  # noqa: E501


        :return: The team_id of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this CwbbScoresTeam.


        :param team_id: The team_id of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def key(self):
        """Gets the key of this CwbbScoresTeam.  # noqa: E501


        :return: The key of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CwbbScoresTeam.


        :param key: The key of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def active(self):
        """Gets the active of this CwbbScoresTeam.  # noqa: E501


        :return: The active of this CwbbScoresTeam.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this CwbbScoresTeam.


        :param active: The active of this CwbbScoresTeam.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def school(self):
        """Gets the school of this CwbbScoresTeam.  # noqa: E501


        :return: The school of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this CwbbScoresTeam.


        :param school: The school of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def name(self):
        """Gets the name of this CwbbScoresTeam.  # noqa: E501


        :return: The name of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CwbbScoresTeam.


        :param name: The name of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ap_rank(self):
        """Gets the ap_rank of this CwbbScoresTeam.  # noqa: E501


        :return: The ap_rank of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._ap_rank

    @ap_rank.setter
    def ap_rank(self, ap_rank):
        """Sets the ap_rank of this CwbbScoresTeam.


        :param ap_rank: The ap_rank of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._ap_rank = ap_rank

    @property
    def wins(self):
        """Gets the wins of this CwbbScoresTeam.  # noqa: E501


        :return: The wins of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this CwbbScoresTeam.


        :param wins: The wins of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this CwbbScoresTeam.  # noqa: E501


        :return: The losses of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this CwbbScoresTeam.


        :param losses: The losses of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def conference_wins(self):
        """Gets the conference_wins of this CwbbScoresTeam.  # noqa: E501


        :return: The conference_wins of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._conference_wins

    @conference_wins.setter
    def conference_wins(self, conference_wins):
        """Sets the conference_wins of this CwbbScoresTeam.


        :param conference_wins: The conference_wins of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._conference_wins = conference_wins

    @property
    def conference_losses(self):
        """Gets the conference_losses of this CwbbScoresTeam.  # noqa: E501


        :return: The conference_losses of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._conference_losses

    @conference_losses.setter
    def conference_losses(self, conference_losses):
        """Sets the conference_losses of this CwbbScoresTeam.


        :param conference_losses: The conference_losses of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._conference_losses = conference_losses

    @property
    def global_team_id(self):
        """Gets the global_team_id of this CwbbScoresTeam.  # noqa: E501


        :return: The global_team_id of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this CwbbScoresTeam.


        :param global_team_id: The global_team_id of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

    @property
    def conference_id(self):
        """Gets the conference_id of this CwbbScoresTeam.  # noqa: E501


        :return: The conference_id of this CwbbScoresTeam.  # noqa: E501
        :rtype: int
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this CwbbScoresTeam.


        :param conference_id: The conference_id of this CwbbScoresTeam.  # noqa: E501
        :type: int
        """

        self._conference_id = conference_id

    @property
    def conference(self):
        """Gets the conference of this CwbbScoresTeam.  # noqa: E501


        :return: The conference of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this CwbbScoresTeam.


        :param conference: The conference of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def team_logo_url(self):
        """Gets the team_logo_url of this CwbbScoresTeam.  # noqa: E501


        :return: The team_logo_url of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._team_logo_url

    @team_logo_url.setter
    def team_logo_url(self, team_logo_url):
        """Sets the team_logo_url of this CwbbScoresTeam.


        :param team_logo_url: The team_logo_url of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._team_logo_url = team_logo_url

    @property
    def short_display_name(self):
        """Gets the short_display_name of this CwbbScoresTeam.  # noqa: E501


        :return: The short_display_name of this CwbbScoresTeam.  # noqa: E501
        :rtype: str
        """
        return self._short_display_name

    @short_display_name.setter
    def short_display_name(self, short_display_name):
        """Sets the short_display_name of this CwbbScoresTeam.


        :param short_display_name: The short_display_name of this CwbbScoresTeam.  # noqa: E501
        :type: str
        """

        self._short_display_name = short_display_name

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
        if issubclass(CwbbScoresTeam, dict):
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
        if not isinstance(other, CwbbScoresTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
