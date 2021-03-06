# coding: utf-8

"""
    CBB v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CbbStatsPlayer(object):
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
        'team_id': 'int',
        'team': 'str',
        'jersey': 'int',
        'position': 'str',
        '_class': 'str',
        'height': 'int',
        'weight': 'int',
        'birth_city': 'str',
        'birth_state': 'str',
        'high_school': 'str',
        'sport_radar_player_id': 'str',
        'rotoworld_player_id': 'int',
        'roto_wire_player_id': 'int',
        'fantasy_alarm_player_id': 'int',
        'global_team_id': 'int'
    }

    attribute_map = {
        'player_id': 'PlayerID',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'team_id': 'TeamID',
        'team': 'Team',
        'jersey': 'Jersey',
        'position': 'Position',
        '_class': 'Class',
        'height': 'Height',
        'weight': 'Weight',
        'birth_city': 'BirthCity',
        'birth_state': 'BirthState',
        'high_school': 'HighSchool',
        'sport_radar_player_id': 'SportRadarPlayerID',
        'rotoworld_player_id': 'RotoworldPlayerID',
        'roto_wire_player_id': 'RotoWirePlayerID',
        'fantasy_alarm_player_id': 'FantasyAlarmPlayerID',
        'global_team_id': 'GlobalTeamID'
    }

    def __init__(self, player_id=None, first_name=None, last_name=None, team_id=None, team=None, jersey=None, position=None, _class=None, height=None, weight=None, birth_city=None, birth_state=None, high_school=None, sport_radar_player_id=None, rotoworld_player_id=None, roto_wire_player_id=None, fantasy_alarm_player_id=None, global_team_id=None):  # noqa: E501
        """CbbStatsPlayer - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._first_name = None
        self._last_name = None
        self._team_id = None
        self._team = None
        self._jersey = None
        self._position = None
        self.__class = None
        self._height = None
        self._weight = None
        self._birth_city = None
        self._birth_state = None
        self._high_school = None
        self._sport_radar_player_id = None
        self._rotoworld_player_id = None
        self._roto_wire_player_id = None
        self._fantasy_alarm_player_id = None
        self._global_team_id = None
        self.discriminator = None
        if player_id is not None:
            self.player_id = player_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if jersey is not None:
            self.jersey = jersey
        if position is not None:
            self.position = position
        if _class is not None:
            self._class = _class
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if birth_city is not None:
            self.birth_city = birth_city
        if birth_state is not None:
            self.birth_state = birth_state
        if high_school is not None:
            self.high_school = high_school
        if sport_radar_player_id is not None:
            self.sport_radar_player_id = sport_radar_player_id
        if rotoworld_player_id is not None:
            self.rotoworld_player_id = rotoworld_player_id
        if roto_wire_player_id is not None:
            self.roto_wire_player_id = roto_wire_player_id
        if fantasy_alarm_player_id is not None:
            self.fantasy_alarm_player_id = fantasy_alarm_player_id
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def player_id(self):
        """Gets the player_id of this CbbStatsPlayer.  # noqa: E501


        :return: The player_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this CbbStatsPlayer.


        :param player_id: The player_id of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def first_name(self):
        """Gets the first_name of this CbbStatsPlayer.  # noqa: E501


        :return: The first_name of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CbbStatsPlayer.


        :param first_name: The first_name of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CbbStatsPlayer.  # noqa: E501


        :return: The last_name of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CbbStatsPlayer.


        :param last_name: The last_name of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def team_id(self):
        """Gets the team_id of this CbbStatsPlayer.  # noqa: E501


        :return: The team_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this CbbStatsPlayer.


        :param team_id: The team_id of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this CbbStatsPlayer.  # noqa: E501


        :return: The team of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this CbbStatsPlayer.


        :param team: The team of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def jersey(self):
        """Gets the jersey of this CbbStatsPlayer.  # noqa: E501


        :return: The jersey of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this CbbStatsPlayer.


        :param jersey: The jersey of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

    @property
    def position(self):
        """Gets the position of this CbbStatsPlayer.  # noqa: E501


        :return: The position of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CbbStatsPlayer.


        :param position: The position of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def _class(self):
        """Gets the _class of this CbbStatsPlayer.  # noqa: E501


        :return: The _class of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this CbbStatsPlayer.


        :param _class: The _class of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def height(self):
        """Gets the height of this CbbStatsPlayer.  # noqa: E501


        :return: The height of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CbbStatsPlayer.


        :param height: The height of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this CbbStatsPlayer.  # noqa: E501


        :return: The weight of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CbbStatsPlayer.


        :param weight: The weight of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def birth_city(self):
        """Gets the birth_city of this CbbStatsPlayer.  # noqa: E501


        :return: The birth_city of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._birth_city

    @birth_city.setter
    def birth_city(self, birth_city):
        """Sets the birth_city of this CbbStatsPlayer.


        :param birth_city: The birth_city of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._birth_city = birth_city

    @property
    def birth_state(self):
        """Gets the birth_state of this CbbStatsPlayer.  # noqa: E501


        :return: The birth_state of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._birth_state

    @birth_state.setter
    def birth_state(self, birth_state):
        """Sets the birth_state of this CbbStatsPlayer.


        :param birth_state: The birth_state of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._birth_state = birth_state

    @property
    def high_school(self):
        """Gets the high_school of this CbbStatsPlayer.  # noqa: E501


        :return: The high_school of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._high_school

    @high_school.setter
    def high_school(self, high_school):
        """Sets the high_school of this CbbStatsPlayer.


        :param high_school: The high_school of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._high_school = high_school

    @property
    def sport_radar_player_id(self):
        """Gets the sport_radar_player_id of this CbbStatsPlayer.  # noqa: E501


        :return: The sport_radar_player_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: str
        """
        return self._sport_radar_player_id

    @sport_radar_player_id.setter
    def sport_radar_player_id(self, sport_radar_player_id):
        """Sets the sport_radar_player_id of this CbbStatsPlayer.


        :param sport_radar_player_id: The sport_radar_player_id of this CbbStatsPlayer.  # noqa: E501
        :type: str
        """

        self._sport_radar_player_id = sport_radar_player_id

    @property
    def rotoworld_player_id(self):
        """Gets the rotoworld_player_id of this CbbStatsPlayer.  # noqa: E501


        :return: The rotoworld_player_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._rotoworld_player_id

    @rotoworld_player_id.setter
    def rotoworld_player_id(self, rotoworld_player_id):
        """Sets the rotoworld_player_id of this CbbStatsPlayer.


        :param rotoworld_player_id: The rotoworld_player_id of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._rotoworld_player_id = rotoworld_player_id

    @property
    def roto_wire_player_id(self):
        """Gets the roto_wire_player_id of this CbbStatsPlayer.  # noqa: E501


        :return: The roto_wire_player_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._roto_wire_player_id

    @roto_wire_player_id.setter
    def roto_wire_player_id(self, roto_wire_player_id):
        """Sets the roto_wire_player_id of this CbbStatsPlayer.


        :param roto_wire_player_id: The roto_wire_player_id of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._roto_wire_player_id = roto_wire_player_id

    @property
    def fantasy_alarm_player_id(self):
        """Gets the fantasy_alarm_player_id of this CbbStatsPlayer.  # noqa: E501


        :return: The fantasy_alarm_player_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._fantasy_alarm_player_id

    @fantasy_alarm_player_id.setter
    def fantasy_alarm_player_id(self, fantasy_alarm_player_id):
        """Sets the fantasy_alarm_player_id of this CbbStatsPlayer.


        :param fantasy_alarm_player_id: The fantasy_alarm_player_id of this CbbStatsPlayer.  # noqa: E501
        :type: int
        """

        self._fantasy_alarm_player_id = fantasy_alarm_player_id

    @property
    def global_team_id(self):
        """Gets the global_team_id of this CbbStatsPlayer.  # noqa: E501


        :return: The global_team_id of this CbbStatsPlayer.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this CbbStatsPlayer.


        :param global_team_id: The global_team_id of this CbbStatsPlayer.  # noqa: E501
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
        if issubclass(CbbStatsPlayer, dict):
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
        if not isinstance(other, CbbStatsPlayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
