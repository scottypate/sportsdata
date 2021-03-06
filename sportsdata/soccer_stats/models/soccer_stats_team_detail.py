# coding: utf-8

"""
    Soccer v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoccerStatsTeamDetail(object):
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
        'players': 'list[SoccerStatsPlayer]',
        'team_id': 'int',
        'area_id': 'int',
        'venue_id': 'int',
        'key': 'str',
        'name': 'str',
        'full_name': 'str',
        'active': 'bool',
        'area_name': 'str',
        'venue_name': 'str',
        'gender': 'str',
        'type': 'str',
        'address': 'str',
        'city': 'str',
        'zip': 'str',
        'phone': 'str',
        'fax': 'str',
        'website': 'str',
        'email': 'str',
        'founded': 'int',
        'club_color1': 'str',
        'club_color2': 'str',
        'club_color3': 'str',
        'nickname1': 'str',
        'nickname2': 'str',
        'nickname3': 'str',
        'wikipedia_logo_url': 'str',
        'wikipedia_word_mark_url': 'str',
        'global_team_id': 'int'
    }

    attribute_map = {
        'players': 'Players',
        'team_id': 'TeamId',
        'area_id': 'AreaId',
        'venue_id': 'VenueId',
        'key': 'Key',
        'name': 'Name',
        'full_name': 'FullName',
        'active': 'Active',
        'area_name': 'AreaName',
        'venue_name': 'VenueName',
        'gender': 'Gender',
        'type': 'Type',
        'address': 'Address',
        'city': 'City',
        'zip': 'Zip',
        'phone': 'Phone',
        'fax': 'Fax',
        'website': 'Website',
        'email': 'Email',
        'founded': 'Founded',
        'club_color1': 'ClubColor1',
        'club_color2': 'ClubColor2',
        'club_color3': 'ClubColor3',
        'nickname1': 'Nickname1',
        'nickname2': 'Nickname2',
        'nickname3': 'Nickname3',
        'wikipedia_logo_url': 'WikipediaLogoUrl',
        'wikipedia_word_mark_url': 'WikipediaWordMarkUrl',
        'global_team_id': 'GlobalTeamId'
    }

    def __init__(self, players=None, team_id=None, area_id=None, venue_id=None, key=None, name=None, full_name=None, active=None, area_name=None, venue_name=None, gender=None, type=None, address=None, city=None, zip=None, phone=None, fax=None, website=None, email=None, founded=None, club_color1=None, club_color2=None, club_color3=None, nickname1=None, nickname2=None, nickname3=None, wikipedia_logo_url=None, wikipedia_word_mark_url=None, global_team_id=None):  # noqa: E501
        """SoccerStatsTeamDetail - a model defined in Swagger"""  # noqa: E501
        self._players = None
        self._team_id = None
        self._area_id = None
        self._venue_id = None
        self._key = None
        self._name = None
        self._full_name = None
        self._active = None
        self._area_name = None
        self._venue_name = None
        self._gender = None
        self._type = None
        self._address = None
        self._city = None
        self._zip = None
        self._phone = None
        self._fax = None
        self._website = None
        self._email = None
        self._founded = None
        self._club_color1 = None
        self._club_color2 = None
        self._club_color3 = None
        self._nickname1 = None
        self._nickname2 = None
        self._nickname3 = None
        self._wikipedia_logo_url = None
        self._wikipedia_word_mark_url = None
        self._global_team_id = None
        self.discriminator = None
        if players is not None:
            self.players = players
        if team_id is not None:
            self.team_id = team_id
        if area_id is not None:
            self.area_id = area_id
        if venue_id is not None:
            self.venue_id = venue_id
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if full_name is not None:
            self.full_name = full_name
        if active is not None:
            self.active = active
        if area_name is not None:
            self.area_name = area_name
        if venue_name is not None:
            self.venue_name = venue_name
        if gender is not None:
            self.gender = gender
        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if zip is not None:
            self.zip = zip
        if phone is not None:
            self.phone = phone
        if fax is not None:
            self.fax = fax
        if website is not None:
            self.website = website
        if email is not None:
            self.email = email
        if founded is not None:
            self.founded = founded
        if club_color1 is not None:
            self.club_color1 = club_color1
        if club_color2 is not None:
            self.club_color2 = club_color2
        if club_color3 is not None:
            self.club_color3 = club_color3
        if nickname1 is not None:
            self.nickname1 = nickname1
        if nickname2 is not None:
            self.nickname2 = nickname2
        if nickname3 is not None:
            self.nickname3 = nickname3
        if wikipedia_logo_url is not None:
            self.wikipedia_logo_url = wikipedia_logo_url
        if wikipedia_word_mark_url is not None:
            self.wikipedia_word_mark_url = wikipedia_word_mark_url
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def players(self):
        """Gets the players of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The players of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: list[SoccerStatsPlayer]
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this SoccerStatsTeamDetail.


        :param players: The players of this SoccerStatsTeamDetail.  # noqa: E501
        :type: list[SoccerStatsPlayer]
        """

        self._players = players

    @property
    def team_id(self):
        """Gets the team_id of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The team_id of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this SoccerStatsTeamDetail.


        :param team_id: The team_id of this SoccerStatsTeamDetail.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def area_id(self):
        """Gets the area_id of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The area_id of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this SoccerStatsTeamDetail.


        :param area_id: The area_id of this SoccerStatsTeamDetail.  # noqa: E501
        :type: int
        """

        self._area_id = area_id

    @property
    def venue_id(self):
        """Gets the venue_id of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The venue_id of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: int
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this SoccerStatsTeamDetail.


        :param venue_id: The venue_id of this SoccerStatsTeamDetail.  # noqa: E501
        :type: int
        """

        self._venue_id = venue_id

    @property
    def key(self):
        """Gets the key of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The key of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SoccerStatsTeamDetail.


        :param key: The key of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The name of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoccerStatsTeamDetail.


        :param name: The name of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The full_name of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SoccerStatsTeamDetail.


        :param full_name: The full_name of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def active(self):
        """Gets the active of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The active of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SoccerStatsTeamDetail.


        :param active: The active of this SoccerStatsTeamDetail.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def area_name(self):
        """Gets the area_name of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The area_name of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this SoccerStatsTeamDetail.


        :param area_name: The area_name of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._area_name = area_name

    @property
    def venue_name(self):
        """Gets the venue_name of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The venue_name of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._venue_name

    @venue_name.setter
    def venue_name(self, venue_name):
        """Sets the venue_name of this SoccerStatsTeamDetail.


        :param venue_name: The venue_name of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._venue_name = venue_name

    @property
    def gender(self):
        """Gets the gender of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The gender of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SoccerStatsTeamDetail.


        :param gender: The gender of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def type(self):
        """Gets the type of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The type of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoccerStatsTeamDetail.


        :param type: The type of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """Gets the address of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The address of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SoccerStatsTeamDetail.


        :param address: The address of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The city of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SoccerStatsTeamDetail.


        :param city: The city of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def zip(self):
        """Gets the zip of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The zip of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this SoccerStatsTeamDetail.


        :param zip: The zip of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The phone of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SoccerStatsTeamDetail.


        :param phone: The phone of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The fax of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this SoccerStatsTeamDetail.


        :param fax: The fax of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def website(self):
        """Gets the website of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The website of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this SoccerStatsTeamDetail.


        :param website: The website of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """Gets the email of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The email of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SoccerStatsTeamDetail.


        :param email: The email of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def founded(self):
        """Gets the founded of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The founded of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: int
        """
        return self._founded

    @founded.setter
    def founded(self, founded):
        """Sets the founded of this SoccerStatsTeamDetail.


        :param founded: The founded of this SoccerStatsTeamDetail.  # noqa: E501
        :type: int
        """

        self._founded = founded

    @property
    def club_color1(self):
        """Gets the club_color1 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The club_color1 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._club_color1

    @club_color1.setter
    def club_color1(self, club_color1):
        """Sets the club_color1 of this SoccerStatsTeamDetail.


        :param club_color1: The club_color1 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._club_color1 = club_color1

    @property
    def club_color2(self):
        """Gets the club_color2 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The club_color2 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._club_color2

    @club_color2.setter
    def club_color2(self, club_color2):
        """Sets the club_color2 of this SoccerStatsTeamDetail.


        :param club_color2: The club_color2 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._club_color2 = club_color2

    @property
    def club_color3(self):
        """Gets the club_color3 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The club_color3 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._club_color3

    @club_color3.setter
    def club_color3(self, club_color3):
        """Sets the club_color3 of this SoccerStatsTeamDetail.


        :param club_color3: The club_color3 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._club_color3 = club_color3

    @property
    def nickname1(self):
        """Gets the nickname1 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The nickname1 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._nickname1

    @nickname1.setter
    def nickname1(self, nickname1):
        """Sets the nickname1 of this SoccerStatsTeamDetail.


        :param nickname1: The nickname1 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._nickname1 = nickname1

    @property
    def nickname2(self):
        """Gets the nickname2 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The nickname2 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._nickname2

    @nickname2.setter
    def nickname2(self, nickname2):
        """Sets the nickname2 of this SoccerStatsTeamDetail.


        :param nickname2: The nickname2 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._nickname2 = nickname2

    @property
    def nickname3(self):
        """Gets the nickname3 of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The nickname3 of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._nickname3

    @nickname3.setter
    def nickname3(self, nickname3):
        """Sets the nickname3 of this SoccerStatsTeamDetail.


        :param nickname3: The nickname3 of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._nickname3 = nickname3

    @property
    def wikipedia_logo_url(self):
        """Gets the wikipedia_logo_url of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The wikipedia_logo_url of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia_logo_url

    @wikipedia_logo_url.setter
    def wikipedia_logo_url(self, wikipedia_logo_url):
        """Sets the wikipedia_logo_url of this SoccerStatsTeamDetail.


        :param wikipedia_logo_url: The wikipedia_logo_url of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._wikipedia_logo_url = wikipedia_logo_url

    @property
    def wikipedia_word_mark_url(self):
        """Gets the wikipedia_word_mark_url of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The wikipedia_word_mark_url of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia_word_mark_url

    @wikipedia_word_mark_url.setter
    def wikipedia_word_mark_url(self, wikipedia_word_mark_url):
        """Sets the wikipedia_word_mark_url of this SoccerStatsTeamDetail.


        :param wikipedia_word_mark_url: The wikipedia_word_mark_url of this SoccerStatsTeamDetail.  # noqa: E501
        :type: str
        """

        self._wikipedia_word_mark_url = wikipedia_word_mark_url

    @property
    def global_team_id(self):
        """Gets the global_team_id of this SoccerStatsTeamDetail.  # noqa: E501


        :return: The global_team_id of this SoccerStatsTeamDetail.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this SoccerStatsTeamDetail.


        :param global_team_id: The global_team_id of this SoccerStatsTeamDetail.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

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
        if issubclass(SoccerStatsTeamDetail, dict):
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
        if not isinstance(other, SoccerStatsTeamDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
