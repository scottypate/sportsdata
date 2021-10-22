# coding: utf-8

"""
    Golf v3 Headshots

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GolfHeadshotsHeadshot(object):
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
        'player_id': 'int',
        'name': 'str',
        'preferred_hosted_headshot_url': 'str',
        'preferred_hosted_headshot_updated': 'str',
        'hosted_headshot_with_background_url': 'str',
        'hosted_headshot_with_background_updated': 'str',
        'hosted_headshot_no_background_url': 'str',
        'hosted_headshot_no_background_updated': 'str'
    }

    attribute_map = {
        'player_id': 'PlayerID',
        'name': 'Name',
        'preferred_hosted_headshot_url': 'PreferredHostedHeadshotUrl',
        'preferred_hosted_headshot_updated': 'PreferredHostedHeadshotUpdated',
        'hosted_headshot_with_background_url': 'HostedHeadshotWithBackgroundUrl',
        'hosted_headshot_with_background_updated': 'HostedHeadshotWithBackgroundUpdated',
        'hosted_headshot_no_background_url': 'HostedHeadshotNoBackgroundUrl',
        'hosted_headshot_no_background_updated': 'HostedHeadshotNoBackgroundUpdated'
    }

    def __init__(self, player_id=None, name=None, preferred_hosted_headshot_url=None, preferred_hosted_headshot_updated=None, hosted_headshot_with_background_url=None, hosted_headshot_with_background_updated=None, hosted_headshot_no_background_url=None, hosted_headshot_no_background_updated=None):  # noqa: E501
        """GolfHeadshotsHeadshot - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._name = None
        self._preferred_hosted_headshot_url = None
        self._preferred_hosted_headshot_updated = None
        self._hosted_headshot_with_background_url = None
        self._hosted_headshot_with_background_updated = None
        self._hosted_headshot_no_background_url = None
        self._hosted_headshot_no_background_updated = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if name is not None:
            self.name = name
        if preferred_hosted_headshot_url is not None:
            self.preferred_hosted_headshot_url = preferred_hosted_headshot_url
        if preferred_hosted_headshot_updated is not None:
            self.preferred_hosted_headshot_updated = preferred_hosted_headshot_updated
        if hosted_headshot_with_background_url is not None:
            self.hosted_headshot_with_background_url = hosted_headshot_with_background_url
        if hosted_headshot_with_background_updated is not None:
            self.hosted_headshot_with_background_updated = hosted_headshot_with_background_updated
        if hosted_headshot_no_background_url is not None:
            self.hosted_headshot_no_background_url = hosted_headshot_no_background_url
        if hosted_headshot_no_background_updated is not None:
            self.hosted_headshot_no_background_updated = hosted_headshot_no_background_updated

    @property
    def player_id(self):
        """Gets the player_id of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The player_id of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this GolfHeadshotsHeadshot.


        :param player_id: The player_id of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def name(self):
        """Gets the name of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The name of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GolfHeadshotsHeadshot.


        :param name: The name of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preferred_hosted_headshot_url(self):
        """Gets the preferred_hosted_headshot_url of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The preferred_hosted_headshot_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._preferred_hosted_headshot_url

    @preferred_hosted_headshot_url.setter
    def preferred_hosted_headshot_url(self, preferred_hosted_headshot_url):
        """Sets the preferred_hosted_headshot_url of this GolfHeadshotsHeadshot.


        :param preferred_hosted_headshot_url: The preferred_hosted_headshot_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._preferred_hosted_headshot_url = preferred_hosted_headshot_url

    @property
    def preferred_hosted_headshot_updated(self):
        """Gets the preferred_hosted_headshot_updated of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The preferred_hosted_headshot_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._preferred_hosted_headshot_updated

    @preferred_hosted_headshot_updated.setter
    def preferred_hosted_headshot_updated(self, preferred_hosted_headshot_updated):
        """Sets the preferred_hosted_headshot_updated of this GolfHeadshotsHeadshot.


        :param preferred_hosted_headshot_updated: The preferred_hosted_headshot_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._preferred_hosted_headshot_updated = preferred_hosted_headshot_updated

    @property
    def hosted_headshot_with_background_url(self):
        """Gets the hosted_headshot_with_background_url of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The hosted_headshot_with_background_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._hosted_headshot_with_background_url

    @hosted_headshot_with_background_url.setter
    def hosted_headshot_with_background_url(self, hosted_headshot_with_background_url):
        """Sets the hosted_headshot_with_background_url of this GolfHeadshotsHeadshot.


        :param hosted_headshot_with_background_url: The hosted_headshot_with_background_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._hosted_headshot_with_background_url = hosted_headshot_with_background_url

    @property
    def hosted_headshot_with_background_updated(self):
        """Gets the hosted_headshot_with_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The hosted_headshot_with_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._hosted_headshot_with_background_updated

    @hosted_headshot_with_background_updated.setter
    def hosted_headshot_with_background_updated(self, hosted_headshot_with_background_updated):
        """Sets the hosted_headshot_with_background_updated of this GolfHeadshotsHeadshot.


        :param hosted_headshot_with_background_updated: The hosted_headshot_with_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._hosted_headshot_with_background_updated = hosted_headshot_with_background_updated

    @property
    def hosted_headshot_no_background_url(self):
        """Gets the hosted_headshot_no_background_url of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The hosted_headshot_no_background_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._hosted_headshot_no_background_url

    @hosted_headshot_no_background_url.setter
    def hosted_headshot_no_background_url(self, hosted_headshot_no_background_url):
        """Sets the hosted_headshot_no_background_url of this GolfHeadshotsHeadshot.


        :param hosted_headshot_no_background_url: The hosted_headshot_no_background_url of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._hosted_headshot_no_background_url = hosted_headshot_no_background_url

    @property
    def hosted_headshot_no_background_updated(self):
        """Gets the hosted_headshot_no_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501


        :return: The hosted_headshot_no_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :rtype: str
        """
        return self._hosted_headshot_no_background_updated

    @hosted_headshot_no_background_updated.setter
    def hosted_headshot_no_background_updated(self, hosted_headshot_no_background_updated):
        """Sets the hosted_headshot_no_background_updated of this GolfHeadshotsHeadshot.


        :param hosted_headshot_no_background_updated: The hosted_headshot_no_background_updated of this GolfHeadshotsHeadshot.  # noqa: E501
        :type: str
        """

        self._hosted_headshot_no_background_updated = hosted_headshot_no_background_updated

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
        if issubclass(GolfHeadshotsHeadshot, dict):
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
        if not isinstance(other, GolfHeadshotsHeadshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
