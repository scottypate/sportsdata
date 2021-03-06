# coding: utf-8

"""
    NASCAR v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NascarV2DriverRace(object):
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
        'stat_id': 'int',
        'driver_id': 'int',
        'season': 'int',
        'name': 'str',
        'number': 'int',
        'number_display': 'str',
        'manufacturer': 'str',
        'draft_kings_salary': 'int',
        'race_id': 'int',
        'day': 'str',
        'date_time': 'str',
        'updated': 'str',
        'created': 'str',
        'fantasy_points': 'float',
        'fantasy_points_draft_kings': 'float',
        'qualifying_speed': 'float',
        'pole_final_position': 'float',
        'start_position': 'float',
        'final_position': 'float',
        'position_differential': 'float',
        'laps': 'float',
        'laps_led': 'float',
        'fastest_laps': 'float',
        'points': 'float',
        'bonus': 'float',
        'penalty': 'float',
        'wins': 'float',
        'poles': 'float'
    }

    attribute_map = {
        'stat_id': 'StatID',
        'driver_id': 'DriverID',
        'season': 'Season',
        'name': 'Name',
        'number': 'Number',
        'number_display': 'NumberDisplay',
        'manufacturer': 'Manufacturer',
        'draft_kings_salary': 'DraftKingsSalary',
        'race_id': 'RaceID',
        'day': 'Day',
        'date_time': 'DateTime',
        'updated': 'Updated',
        'created': 'Created',
        'fantasy_points': 'FantasyPoints',
        'fantasy_points_draft_kings': 'FantasyPointsDraftKings',
        'qualifying_speed': 'QualifyingSpeed',
        'pole_final_position': 'PoleFinalPosition',
        'start_position': 'StartPosition',
        'final_position': 'FinalPosition',
        'position_differential': 'PositionDifferential',
        'laps': 'Laps',
        'laps_led': 'LapsLed',
        'fastest_laps': 'FastestLaps',
        'points': 'Points',
        'bonus': 'Bonus',
        'penalty': 'Penalty',
        'wins': 'Wins',
        'poles': 'Poles'
    }

    def __init__(self, stat_id=None, driver_id=None, season=None, name=None, number=None, number_display=None, manufacturer=None, draft_kings_salary=None, race_id=None, day=None, date_time=None, updated=None, created=None, fantasy_points=None, fantasy_points_draft_kings=None, qualifying_speed=None, pole_final_position=None, start_position=None, final_position=None, position_differential=None, laps=None, laps_led=None, fastest_laps=None, points=None, bonus=None, penalty=None, wins=None, poles=None):  # noqa: E501
        """NascarV2DriverRace - a model defined in Swagger"""  # noqa: E501
        self._stat_id = None
        self._driver_id = None
        self._season = None
        self._name = None
        self._number = None
        self._number_display = None
        self._manufacturer = None
        self._draft_kings_salary = None
        self._race_id = None
        self._day = None
        self._date_time = None
        self._updated = None
        self._created = None
        self._fantasy_points = None
        self._fantasy_points_draft_kings = None
        self._qualifying_speed = None
        self._pole_final_position = None
        self._start_position = None
        self._final_position = None
        self._position_differential = None
        self._laps = None
        self._laps_led = None
        self._fastest_laps = None
        self._points = None
        self._bonus = None
        self._penalty = None
        self._wins = None
        self._poles = None
        self.discriminator = None
        if stat_id is not None:
            self.stat_id = stat_id
        if driver_id is not None:
            self.driver_id = driver_id
        if season is not None:
            self.season = season
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if number_display is not None:
            self.number_display = number_display
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if draft_kings_salary is not None:
            self.draft_kings_salary = draft_kings_salary
        if race_id is not None:
            self.race_id = race_id
        if day is not None:
            self.day = day
        if date_time is not None:
            self.date_time = date_time
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if fantasy_points is not None:
            self.fantasy_points = fantasy_points
        if fantasy_points_draft_kings is not None:
            self.fantasy_points_draft_kings = fantasy_points_draft_kings
        if qualifying_speed is not None:
            self.qualifying_speed = qualifying_speed
        if pole_final_position is not None:
            self.pole_final_position = pole_final_position
        if start_position is not None:
            self.start_position = start_position
        if final_position is not None:
            self.final_position = final_position
        if position_differential is not None:
            self.position_differential = position_differential
        if laps is not None:
            self.laps = laps
        if laps_led is not None:
            self.laps_led = laps_led
        if fastest_laps is not None:
            self.fastest_laps = fastest_laps
        if points is not None:
            self.points = points
        if bonus is not None:
            self.bonus = bonus
        if penalty is not None:
            self.penalty = penalty
        if wins is not None:
            self.wins = wins
        if poles is not None:
            self.poles = poles

    @property
    def stat_id(self):
        """Gets the stat_id of this NascarV2DriverRace.  # noqa: E501


        :return: The stat_id of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._stat_id

    @stat_id.setter
    def stat_id(self, stat_id):
        """Sets the stat_id of this NascarV2DriverRace.


        :param stat_id: The stat_id of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._stat_id = stat_id

    @property
    def driver_id(self):
        """Gets the driver_id of this NascarV2DriverRace.  # noqa: E501


        :return: The driver_id of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this NascarV2DriverRace.


        :param driver_id: The driver_id of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def season(self):
        """Gets the season of this NascarV2DriverRace.  # noqa: E501


        :return: The season of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this NascarV2DriverRace.


        :param season: The season of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def name(self):
        """Gets the name of this NascarV2DriverRace.  # noqa: E501


        :return: The name of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NascarV2DriverRace.


        :param name: The name of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this NascarV2DriverRace.  # noqa: E501


        :return: The number of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this NascarV2DriverRace.


        :param number: The number of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def number_display(self):
        """Gets the number_display of this NascarV2DriverRace.  # noqa: E501


        :return: The number_display of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._number_display

    @number_display.setter
    def number_display(self, number_display):
        """Sets the number_display of this NascarV2DriverRace.


        :param number_display: The number_display of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._number_display = number_display

    @property
    def manufacturer(self):
        """Gets the manufacturer of this NascarV2DriverRace.  # noqa: E501


        :return: The manufacturer of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this NascarV2DriverRace.


        :param manufacturer: The manufacturer of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def draft_kings_salary(self):
        """Gets the draft_kings_salary of this NascarV2DriverRace.  # noqa: E501


        :return: The draft_kings_salary of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._draft_kings_salary

    @draft_kings_salary.setter
    def draft_kings_salary(self, draft_kings_salary):
        """Sets the draft_kings_salary of this NascarV2DriverRace.


        :param draft_kings_salary: The draft_kings_salary of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._draft_kings_salary = draft_kings_salary

    @property
    def race_id(self):
        """Gets the race_id of this NascarV2DriverRace.  # noqa: E501


        :return: The race_id of this NascarV2DriverRace.  # noqa: E501
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """Sets the race_id of this NascarV2DriverRace.


        :param race_id: The race_id of this NascarV2DriverRace.  # noqa: E501
        :type: int
        """

        self._race_id = race_id

    @property
    def day(self):
        """Gets the day of this NascarV2DriverRace.  # noqa: E501


        :return: The day of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this NascarV2DriverRace.


        :param day: The day of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def date_time(self):
        """Gets the date_time of this NascarV2DriverRace.  # noqa: E501


        :return: The date_time of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this NascarV2DriverRace.


        :param date_time: The date_time of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def updated(self):
        """Gets the updated of this NascarV2DriverRace.  # noqa: E501


        :return: The updated of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NascarV2DriverRace.


        :param updated: The updated of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this NascarV2DriverRace.  # noqa: E501


        :return: The created of this NascarV2DriverRace.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NascarV2DriverRace.


        :param created: The created of this NascarV2DriverRace.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this NascarV2DriverRace.  # noqa: E501


        :return: The fantasy_points of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this NascarV2DriverRace.


        :param fantasy_points: The fantasy_points of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._fantasy_points = fantasy_points

    @property
    def fantasy_points_draft_kings(self):
        """Gets the fantasy_points_draft_kings of this NascarV2DriverRace.  # noqa: E501


        :return: The fantasy_points_draft_kings of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_draft_kings

    @fantasy_points_draft_kings.setter
    def fantasy_points_draft_kings(self, fantasy_points_draft_kings):
        """Sets the fantasy_points_draft_kings of this NascarV2DriverRace.


        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._fantasy_points_draft_kings = fantasy_points_draft_kings

    @property
    def qualifying_speed(self):
        """Gets the qualifying_speed of this NascarV2DriverRace.  # noqa: E501


        :return: The qualifying_speed of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._qualifying_speed

    @qualifying_speed.setter
    def qualifying_speed(self, qualifying_speed):
        """Sets the qualifying_speed of this NascarV2DriverRace.


        :param qualifying_speed: The qualifying_speed of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._qualifying_speed = qualifying_speed

    @property
    def pole_final_position(self):
        """Gets the pole_final_position of this NascarV2DriverRace.  # noqa: E501


        :return: The pole_final_position of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._pole_final_position

    @pole_final_position.setter
    def pole_final_position(self, pole_final_position):
        """Sets the pole_final_position of this NascarV2DriverRace.


        :param pole_final_position: The pole_final_position of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._pole_final_position = pole_final_position

    @property
    def start_position(self):
        """Gets the start_position of this NascarV2DriverRace.  # noqa: E501


        :return: The start_position of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this NascarV2DriverRace.


        :param start_position: The start_position of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._start_position = start_position

    @property
    def final_position(self):
        """Gets the final_position of this NascarV2DriverRace.  # noqa: E501


        :return: The final_position of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._final_position

    @final_position.setter
    def final_position(self, final_position):
        """Sets the final_position of this NascarV2DriverRace.


        :param final_position: The final_position of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._final_position = final_position

    @property
    def position_differential(self):
        """Gets the position_differential of this NascarV2DriverRace.  # noqa: E501


        :return: The position_differential of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._position_differential

    @position_differential.setter
    def position_differential(self, position_differential):
        """Sets the position_differential of this NascarV2DriverRace.


        :param position_differential: The position_differential of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._position_differential = position_differential

    @property
    def laps(self):
        """Gets the laps of this NascarV2DriverRace.  # noqa: E501


        :return: The laps of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._laps

    @laps.setter
    def laps(self, laps):
        """Sets the laps of this NascarV2DriverRace.


        :param laps: The laps of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._laps = laps

    @property
    def laps_led(self):
        """Gets the laps_led of this NascarV2DriverRace.  # noqa: E501


        :return: The laps_led of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._laps_led

    @laps_led.setter
    def laps_led(self, laps_led):
        """Sets the laps_led of this NascarV2DriverRace.


        :param laps_led: The laps_led of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._laps_led = laps_led

    @property
    def fastest_laps(self):
        """Gets the fastest_laps of this NascarV2DriverRace.  # noqa: E501


        :return: The fastest_laps of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._fastest_laps

    @fastest_laps.setter
    def fastest_laps(self, fastest_laps):
        """Sets the fastest_laps of this NascarV2DriverRace.


        :param fastest_laps: The fastest_laps of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._fastest_laps = fastest_laps

    @property
    def points(self):
        """Gets the points of this NascarV2DriverRace.  # noqa: E501


        :return: The points of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this NascarV2DriverRace.


        :param points: The points of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._points = points

    @property
    def bonus(self):
        """Gets the bonus of this NascarV2DriverRace.  # noqa: E501


        :return: The bonus of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        """Sets the bonus of this NascarV2DriverRace.


        :param bonus: The bonus of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._bonus = bonus

    @property
    def penalty(self):
        """Gets the penalty of this NascarV2DriverRace.  # noqa: E501


        :return: The penalty of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this NascarV2DriverRace.


        :param penalty: The penalty of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._penalty = penalty

    @property
    def wins(self):
        """Gets the wins of this NascarV2DriverRace.  # noqa: E501


        :return: The wins of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this NascarV2DriverRace.


        :param wins: The wins of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._wins = wins

    @property
    def poles(self):
        """Gets the poles of this NascarV2DriverRace.  # noqa: E501


        :return: The poles of this NascarV2DriverRace.  # noqa: E501
        :rtype: float
        """
        return self._poles

    @poles.setter
    def poles(self, poles):
        """Sets the poles of this NascarV2DriverRace.


        :param poles: The poles of this NascarV2DriverRace.  # noqa: E501
        :type: float
        """

        self._poles = poles

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
        if issubclass(NascarV2DriverRace, dict):
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
        if not isinstance(other, NascarV2DriverRace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
