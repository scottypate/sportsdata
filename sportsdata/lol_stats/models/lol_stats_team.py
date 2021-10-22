# coding: utf-8

"""
    LoL v3 Stats

    LoL v3 Stats  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LolStatsTeam(object):
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
        'area_id': 'int',
        'area_name': 'str',
        'key': 'str',
        'name': 'str',
        'short_name': 'str',
        'active': 'bool',
        'gender': 'str',
        'type': 'str',
        'website': 'str',
        'email': 'str',
        'founded': 'int',
        'primary_color': 'str',
        'secondary_color': 'str',
        'tertiary_color': 'str',
        'quaternary_color': 'str',
        'facebook': 'str',
        'twitter': 'str',
        'you_tube': 'str',
        'instagram': 'str'
    }

    attribute_map = {
        'team_id': 'TeamId',
        'area_id': 'AreaId',
        'area_name': 'AreaName',
        'key': 'Key',
        'name': 'Name',
        'short_name': 'ShortName',
        'active': 'Active',
        'gender': 'Gender',
        'type': 'Type',
        'website': 'Website',
        'email': 'Email',
        'founded': 'Founded',
        'primary_color': 'PrimaryColor',
        'secondary_color': 'SecondaryColor',
        'tertiary_color': 'TertiaryColor',
        'quaternary_color': 'QuaternaryColor',
        'facebook': 'Facebook',
        'twitter': 'Twitter',
        'you_tube': 'YouTube',
        'instagram': 'Instagram'
    }

    def __init__(self, team_id=None, area_id=None, area_name=None, key=None, name=None, short_name=None, active=None, gender=None, type=None, website=None, email=None, founded=None, primary_color=None, secondary_color=None, tertiary_color=None, quaternary_color=None, facebook=None, twitter=None, you_tube=None, instagram=None):  # noqa: E501
        """LolStatsTeam - a model defined in Swagger"""  # noqa: E501
        self._team_id = None
        self._area_id = None
        self._area_name = None
        self._key = None
        self._name = None
        self._short_name = None
        self._active = None
        self._gender = None
        self._type = None
        self._website = None
        self._email = None
        self._founded = None
        self._primary_color = None
        self._secondary_color = None
        self._tertiary_color = None
        self._quaternary_color = None
        self._facebook = None
        self._twitter = None
        self._you_tube = None
        self._instagram = None
        self.discriminator = None
        if team_id is not None:
            self.team_id = team_id
        if area_id is not None:
            self.area_id = area_id
        if area_name is not None:
            self.area_name = area_name
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if active is not None:
            self.active = active
        if gender is not None:
            self.gender = gender
        if type is not None:
            self.type = type
        if website is not None:
            self.website = website
        if email is not None:
            self.email = email
        if founded is not None:
            self.founded = founded
        if primary_color is not None:
            self.primary_color = primary_color
        if secondary_color is not None:
            self.secondary_color = secondary_color
        if tertiary_color is not None:
            self.tertiary_color = tertiary_color
        if quaternary_color is not None:
            self.quaternary_color = quaternary_color
        if facebook is not None:
            self.facebook = facebook
        if twitter is not None:
            self.twitter = twitter
        if you_tube is not None:
            self.you_tube = you_tube
        if instagram is not None:
            self.instagram = instagram

    @property
    def team_id(self):
        """Gets the team_id of this LolStatsTeam.  # noqa: E501


        :return: The team_id of this LolStatsTeam.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this LolStatsTeam.


        :param team_id: The team_id of this LolStatsTeam.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def area_id(self):
        """Gets the area_id of this LolStatsTeam.  # noqa: E501


        :return: The area_id of this LolStatsTeam.  # noqa: E501
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this LolStatsTeam.


        :param area_id: The area_id of this LolStatsTeam.  # noqa: E501
        :type: int
        """

        self._area_id = area_id

    @property
    def area_name(self):
        """Gets the area_name of this LolStatsTeam.  # noqa: E501


        :return: The area_name of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this LolStatsTeam.


        :param area_name: The area_name of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._area_name = area_name

    @property
    def key(self):
        """Gets the key of this LolStatsTeam.  # noqa: E501


        :return: The key of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LolStatsTeam.


        :param key: The key of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this LolStatsTeam.  # noqa: E501


        :return: The name of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LolStatsTeam.


        :param name: The name of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this LolStatsTeam.  # noqa: E501


        :return: The short_name of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this LolStatsTeam.


        :param short_name: The short_name of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def active(self):
        """Gets the active of this LolStatsTeam.  # noqa: E501


        :return: The active of this LolStatsTeam.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this LolStatsTeam.


        :param active: The active of this LolStatsTeam.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def gender(self):
        """Gets the gender of this LolStatsTeam.  # noqa: E501


        :return: The gender of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this LolStatsTeam.


        :param gender: The gender of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def type(self):
        """Gets the type of this LolStatsTeam.  # noqa: E501


        :return: The type of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LolStatsTeam.


        :param type: The type of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def website(self):
        """Gets the website of this LolStatsTeam.  # noqa: E501


        :return: The website of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this LolStatsTeam.


        :param website: The website of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """Gets the email of this LolStatsTeam.  # noqa: E501


        :return: The email of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LolStatsTeam.


        :param email: The email of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def founded(self):
        """Gets the founded of this LolStatsTeam.  # noqa: E501


        :return: The founded of this LolStatsTeam.  # noqa: E501
        :rtype: int
        """
        return self._founded

    @founded.setter
    def founded(self, founded):
        """Sets the founded of this LolStatsTeam.


        :param founded: The founded of this LolStatsTeam.  # noqa: E501
        :type: int
        """

        self._founded = founded

    @property
    def primary_color(self):
        """Gets the primary_color of this LolStatsTeam.  # noqa: E501


        :return: The primary_color of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._primary_color

    @primary_color.setter
    def primary_color(self, primary_color):
        """Sets the primary_color of this LolStatsTeam.


        :param primary_color: The primary_color of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._primary_color = primary_color

    @property
    def secondary_color(self):
        """Gets the secondary_color of this LolStatsTeam.  # noqa: E501


        :return: The secondary_color of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, secondary_color):
        """Sets the secondary_color of this LolStatsTeam.


        :param secondary_color: The secondary_color of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._secondary_color = secondary_color

    @property
    def tertiary_color(self):
        """Gets the tertiary_color of this LolStatsTeam.  # noqa: E501


        :return: The tertiary_color of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._tertiary_color

    @tertiary_color.setter
    def tertiary_color(self, tertiary_color):
        """Sets the tertiary_color of this LolStatsTeam.


        :param tertiary_color: The tertiary_color of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._tertiary_color = tertiary_color

    @property
    def quaternary_color(self):
        """Gets the quaternary_color of this LolStatsTeam.  # noqa: E501


        :return: The quaternary_color of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._quaternary_color

    @quaternary_color.setter
    def quaternary_color(self, quaternary_color):
        """Sets the quaternary_color of this LolStatsTeam.


        :param quaternary_color: The quaternary_color of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._quaternary_color = quaternary_color

    @property
    def facebook(self):
        """Gets the facebook of this LolStatsTeam.  # noqa: E501


        :return: The facebook of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this LolStatsTeam.


        :param facebook: The facebook of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """Gets the twitter of this LolStatsTeam.  # noqa: E501


        :return: The twitter of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this LolStatsTeam.


        :param twitter: The twitter of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._twitter = twitter

    @property
    def you_tube(self):
        """Gets the you_tube of this LolStatsTeam.  # noqa: E501


        :return: The you_tube of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._you_tube

    @you_tube.setter
    def you_tube(self, you_tube):
        """Sets the you_tube of this LolStatsTeam.


        :param you_tube: The you_tube of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._you_tube = you_tube

    @property
    def instagram(self):
        """Gets the instagram of this LolStatsTeam.  # noqa: E501


        :return: The instagram of this LolStatsTeam.  # noqa: E501
        :rtype: str
        """
        return self._instagram

    @instagram.setter
    def instagram(self, instagram):
        """Sets the instagram of this LolStatsTeam.


        :param instagram: The instagram of this LolStatsTeam.  # noqa: E501
        :type: str
        """

        self._instagram = instagram

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
        if issubclass(LolStatsTeam, dict):
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
        if not isinstance(other, LolStatsTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
