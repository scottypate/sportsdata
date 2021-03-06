# coding: utf-8

"""
    Soccer v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoccerScoresPlayer(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'common_name': 'str',
        'short_name': 'str',
        'position': 'str',
        'position_category': 'str',
        'jersey': 'int',
        'foot': 'str',
        'height': 'int',
        'weight': 'int',
        'gender': 'str',
        'birth_date': 'str',
        'birth_city': 'str',
        'birth_country': 'str',
        'nationality': 'str',
        'injury_status': 'str',
        'injury_body_part': 'str',
        'injury_notes': 'str',
        'injury_start_date': 'str',
        'updated': 'str',
        'photo_url': 'str',
        'roto_wire_player_id': 'int',
        'draft_kings_position': 'str',
        'usa_today_player_id': 'int',
        'usa_today_headshot_url': 'str',
        'usa_today_headshot_no_background_url': 'str',
        'usa_today_headshot_updated': 'str',
        'usa_today_headshot_no_background_updated': 'str'
    }

    attribute_map = {
        'player_id': 'PlayerId',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'common_name': 'CommonName',
        'short_name': 'ShortName',
        'position': 'Position',
        'position_category': 'PositionCategory',
        'jersey': 'Jersey',
        'foot': 'Foot',
        'height': 'Height',
        'weight': 'Weight',
        'gender': 'Gender',
        'birth_date': 'BirthDate',
        'birth_city': 'BirthCity',
        'birth_country': 'BirthCountry',
        'nationality': 'Nationality',
        'injury_status': 'InjuryStatus',
        'injury_body_part': 'InjuryBodyPart',
        'injury_notes': 'InjuryNotes',
        'injury_start_date': 'InjuryStartDate',
        'updated': 'Updated',
        'photo_url': 'PhotoUrl',
        'roto_wire_player_id': 'RotoWirePlayerID',
        'draft_kings_position': 'DraftKingsPosition',
        'usa_today_player_id': 'UsaTodayPlayerID',
        'usa_today_headshot_url': 'UsaTodayHeadshotUrl',
        'usa_today_headshot_no_background_url': 'UsaTodayHeadshotNoBackgroundUrl',
        'usa_today_headshot_updated': 'UsaTodayHeadshotUpdated',
        'usa_today_headshot_no_background_updated': 'UsaTodayHeadshotNoBackgroundUpdated'
    }

    def __init__(self, player_id=None, first_name=None, last_name=None, common_name=None, short_name=None, position=None, position_category=None, jersey=None, foot=None, height=None, weight=None, gender=None, birth_date=None, birth_city=None, birth_country=None, nationality=None, injury_status=None, injury_body_part=None, injury_notes=None, injury_start_date=None, updated=None, photo_url=None, roto_wire_player_id=None, draft_kings_position=None, usa_today_player_id=None, usa_today_headshot_url=None, usa_today_headshot_no_background_url=None, usa_today_headshot_updated=None, usa_today_headshot_no_background_updated=None):  # noqa: E501
        """SoccerScoresPlayer - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._first_name = None
        self._last_name = None
        self._common_name = None
        self._short_name = None
        self._position = None
        self._position_category = None
        self._jersey = None
        self._foot = None
        self._height = None
        self._weight = None
        self._gender = None
        self._birth_date = None
        self._birth_city = None
        self._birth_country = None
        self._nationality = None
        self._injury_status = None
        self._injury_body_part = None
        self._injury_notes = None
        self._injury_start_date = None
        self._updated = None
        self._photo_url = None
        self._roto_wire_player_id = None
        self._draft_kings_position = None
        self._usa_today_player_id = None
        self._usa_today_headshot_url = None
        self._usa_today_headshot_no_background_url = None
        self._usa_today_headshot_updated = None
        self._usa_today_headshot_no_background_updated = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if common_name is not None:
            self.common_name = common_name
        if short_name is not None:
            self.short_name = short_name
        if position is not None:
            self.position = position
        if position_category is not None:
            self.position_category = position_category
        if jersey is not None:
            self.jersey = jersey
        if foot is not None:
            self.foot = foot
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if gender is not None:
            self.gender = gender
        if birth_date is not None:
            self.birth_date = birth_date
        if birth_city is not None:
            self.birth_city = birth_city
        if birth_country is not None:
            self.birth_country = birth_country
        if nationality is not None:
            self.nationality = nationality
        if injury_status is not None:
            self.injury_status = injury_status
        if injury_body_part is not None:
            self.injury_body_part = injury_body_part
        if injury_notes is not None:
            self.injury_notes = injury_notes
        if injury_start_date is not None:
            self.injury_start_date = injury_start_date
        if updated is not None:
            self.updated = updated
        if photo_url is not None:
            self.photo_url = photo_url
        if roto_wire_player_id is not None:
            self.roto_wire_player_id = roto_wire_player_id
        if draft_kings_position is not None:
            self.draft_kings_position = draft_kings_position
        if usa_today_player_id is not None:
            self.usa_today_player_id = usa_today_player_id
        if usa_today_headshot_url is not None:
            self.usa_today_headshot_url = usa_today_headshot_url
        if usa_today_headshot_no_background_url is not None:
            self.usa_today_headshot_no_background_url = usa_today_headshot_no_background_url
        if usa_today_headshot_updated is not None:
            self.usa_today_headshot_updated = usa_today_headshot_updated
        if usa_today_headshot_no_background_updated is not None:
            self.usa_today_headshot_no_background_updated = usa_today_headshot_no_background_updated

    @property
    def player_id(self):
        """Gets the player_id of this SoccerScoresPlayer.  # noqa: E501


        :return: The player_id of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this SoccerScoresPlayer.


        :param player_id: The player_id of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def first_name(self):
        """Gets the first_name of this SoccerScoresPlayer.  # noqa: E501


        :return: The first_name of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SoccerScoresPlayer.


        :param first_name: The first_name of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SoccerScoresPlayer.  # noqa: E501


        :return: The last_name of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SoccerScoresPlayer.


        :param last_name: The last_name of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def common_name(self):
        """Gets the common_name of this SoccerScoresPlayer.  # noqa: E501


        :return: The common_name of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this SoccerScoresPlayer.


        :param common_name: The common_name of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def short_name(self):
        """Gets the short_name of this SoccerScoresPlayer.  # noqa: E501


        :return: The short_name of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this SoccerScoresPlayer.


        :param short_name: The short_name of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def position(self):
        """Gets the position of this SoccerScoresPlayer.  # noqa: E501


        :return: The position of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SoccerScoresPlayer.


        :param position: The position of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def position_category(self):
        """Gets the position_category of this SoccerScoresPlayer.  # noqa: E501


        :return: The position_category of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._position_category

    @position_category.setter
    def position_category(self, position_category):
        """Sets the position_category of this SoccerScoresPlayer.


        :param position_category: The position_category of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._position_category = position_category

    @property
    def jersey(self):
        """Gets the jersey of this SoccerScoresPlayer.  # noqa: E501


        :return: The jersey of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this SoccerScoresPlayer.


        :param jersey: The jersey of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

    @property
    def foot(self):
        """Gets the foot of this SoccerScoresPlayer.  # noqa: E501


        :return: The foot of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._foot

    @foot.setter
    def foot(self, foot):
        """Sets the foot of this SoccerScoresPlayer.


        :param foot: The foot of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._foot = foot

    @property
    def height(self):
        """Gets the height of this SoccerScoresPlayer.  # noqa: E501


        :return: The height of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SoccerScoresPlayer.


        :param height: The height of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this SoccerScoresPlayer.  # noqa: E501


        :return: The weight of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SoccerScoresPlayer.


        :param weight: The weight of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def gender(self):
        """Gets the gender of this SoccerScoresPlayer.  # noqa: E501


        :return: The gender of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SoccerScoresPlayer.


        :param gender: The gender of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def birth_date(self):
        """Gets the birth_date of this SoccerScoresPlayer.  # noqa: E501


        :return: The birth_date of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this SoccerScoresPlayer.


        :param birth_date: The birth_date of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._birth_date = birth_date

    @property
    def birth_city(self):
        """Gets the birth_city of this SoccerScoresPlayer.  # noqa: E501


        :return: The birth_city of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._birth_city

    @birth_city.setter
    def birth_city(self, birth_city):
        """Sets the birth_city of this SoccerScoresPlayer.


        :param birth_city: The birth_city of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._birth_city = birth_city

    @property
    def birth_country(self):
        """Gets the birth_country of this SoccerScoresPlayer.  # noqa: E501


        :return: The birth_country of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._birth_country

    @birth_country.setter
    def birth_country(self, birth_country):
        """Sets the birth_country of this SoccerScoresPlayer.


        :param birth_country: The birth_country of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._birth_country = birth_country

    @property
    def nationality(self):
        """Gets the nationality of this SoccerScoresPlayer.  # noqa: E501


        :return: The nationality of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this SoccerScoresPlayer.


        :param nationality: The nationality of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._nationality = nationality

    @property
    def injury_status(self):
        """Gets the injury_status of this SoccerScoresPlayer.  # noqa: E501


        :return: The injury_status of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._injury_status

    @injury_status.setter
    def injury_status(self, injury_status):
        """Sets the injury_status of this SoccerScoresPlayer.


        :param injury_status: The injury_status of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._injury_status = injury_status

    @property
    def injury_body_part(self):
        """Gets the injury_body_part of this SoccerScoresPlayer.  # noqa: E501


        :return: The injury_body_part of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._injury_body_part

    @injury_body_part.setter
    def injury_body_part(self, injury_body_part):
        """Sets the injury_body_part of this SoccerScoresPlayer.


        :param injury_body_part: The injury_body_part of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._injury_body_part = injury_body_part

    @property
    def injury_notes(self):
        """Gets the injury_notes of this SoccerScoresPlayer.  # noqa: E501


        :return: The injury_notes of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._injury_notes

    @injury_notes.setter
    def injury_notes(self, injury_notes):
        """Sets the injury_notes of this SoccerScoresPlayer.


        :param injury_notes: The injury_notes of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._injury_notes = injury_notes

    @property
    def injury_start_date(self):
        """Gets the injury_start_date of this SoccerScoresPlayer.  # noqa: E501


        :return: The injury_start_date of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._injury_start_date

    @injury_start_date.setter
    def injury_start_date(self, injury_start_date):
        """Sets the injury_start_date of this SoccerScoresPlayer.


        :param injury_start_date: The injury_start_date of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._injury_start_date = injury_start_date

    @property
    def updated(self):
        """Gets the updated of this SoccerScoresPlayer.  # noqa: E501


        :return: The updated of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SoccerScoresPlayer.


        :param updated: The updated of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def photo_url(self):
        """Gets the photo_url of this SoccerScoresPlayer.  # noqa: E501


        :return: The photo_url of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this SoccerScoresPlayer.


        :param photo_url: The photo_url of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def roto_wire_player_id(self):
        """Gets the roto_wire_player_id of this SoccerScoresPlayer.  # noqa: E501


        :return: The roto_wire_player_id of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._roto_wire_player_id

    @roto_wire_player_id.setter
    def roto_wire_player_id(self, roto_wire_player_id):
        """Sets the roto_wire_player_id of this SoccerScoresPlayer.


        :param roto_wire_player_id: The roto_wire_player_id of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._roto_wire_player_id = roto_wire_player_id

    @property
    def draft_kings_position(self):
        """Gets the draft_kings_position of this SoccerScoresPlayer.  # noqa: E501


        :return: The draft_kings_position of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._draft_kings_position

    @draft_kings_position.setter
    def draft_kings_position(self, draft_kings_position):
        """Sets the draft_kings_position of this SoccerScoresPlayer.


        :param draft_kings_position: The draft_kings_position of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._draft_kings_position = draft_kings_position

    @property
    def usa_today_player_id(self):
        """Gets the usa_today_player_id of this SoccerScoresPlayer.  # noqa: E501


        :return: The usa_today_player_id of this SoccerScoresPlayer.  # noqa: E501
        :rtype: int
        """
        return self._usa_today_player_id

    @usa_today_player_id.setter
    def usa_today_player_id(self, usa_today_player_id):
        """Sets the usa_today_player_id of this SoccerScoresPlayer.


        :param usa_today_player_id: The usa_today_player_id of this SoccerScoresPlayer.  # noqa: E501
        :type: int
        """

        self._usa_today_player_id = usa_today_player_id

    @property
    def usa_today_headshot_url(self):
        """Gets the usa_today_headshot_url of this SoccerScoresPlayer.  # noqa: E501


        :return: The usa_today_headshot_url of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._usa_today_headshot_url

    @usa_today_headshot_url.setter
    def usa_today_headshot_url(self, usa_today_headshot_url):
        """Sets the usa_today_headshot_url of this SoccerScoresPlayer.


        :param usa_today_headshot_url: The usa_today_headshot_url of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._usa_today_headshot_url = usa_today_headshot_url

    @property
    def usa_today_headshot_no_background_url(self):
        """Gets the usa_today_headshot_no_background_url of this SoccerScoresPlayer.  # noqa: E501


        :return: The usa_today_headshot_no_background_url of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._usa_today_headshot_no_background_url

    @usa_today_headshot_no_background_url.setter
    def usa_today_headshot_no_background_url(self, usa_today_headshot_no_background_url):
        """Sets the usa_today_headshot_no_background_url of this SoccerScoresPlayer.


        :param usa_today_headshot_no_background_url: The usa_today_headshot_no_background_url of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._usa_today_headshot_no_background_url = usa_today_headshot_no_background_url

    @property
    def usa_today_headshot_updated(self):
        """Gets the usa_today_headshot_updated of this SoccerScoresPlayer.  # noqa: E501


        :return: The usa_today_headshot_updated of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._usa_today_headshot_updated

    @usa_today_headshot_updated.setter
    def usa_today_headshot_updated(self, usa_today_headshot_updated):
        """Sets the usa_today_headshot_updated of this SoccerScoresPlayer.


        :param usa_today_headshot_updated: The usa_today_headshot_updated of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._usa_today_headshot_updated = usa_today_headshot_updated

    @property
    def usa_today_headshot_no_background_updated(self):
        """Gets the usa_today_headshot_no_background_updated of this SoccerScoresPlayer.  # noqa: E501


        :return: The usa_today_headshot_no_background_updated of this SoccerScoresPlayer.  # noqa: E501
        :rtype: str
        """
        return self._usa_today_headshot_no_background_updated

    @usa_today_headshot_no_background_updated.setter
    def usa_today_headshot_no_background_updated(self, usa_today_headshot_no_background_updated):
        """Sets the usa_today_headshot_no_background_updated of this SoccerScoresPlayer.


        :param usa_today_headshot_no_background_updated: The usa_today_headshot_no_background_updated of this SoccerScoresPlayer.  # noqa: E501
        :type: str
        """

        self._usa_today_headshot_no_background_updated = usa_today_headshot_no_background_updated

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
        if issubclass(SoccerScoresPlayer, dict):
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
        if not isinstance(other, SoccerScoresPlayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
