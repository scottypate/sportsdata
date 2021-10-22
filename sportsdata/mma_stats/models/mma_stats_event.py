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

class MmaStatsEvent(object):
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
        'event_id': 'int',
        'league_id': 'int',
        'name': 'str',
        'short_name': 'str',
        'season': 'int',
        'day': 'str',
        'date_time': 'str',
        'status': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'event_id': 'EventId',
        'league_id': 'LeagueId',
        'name': 'Name',
        'short_name': 'ShortName',
        'season': 'Season',
        'day': 'Day',
        'date_time': 'DateTime',
        'status': 'Status',
        'active': 'Active'
    }

    def __init__(self, event_id=None, league_id=None, name=None, short_name=None, season=None, day=None, date_time=None, status=None, active=None):  # noqa: E501
        """MmaStatsEvent - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._league_id = None
        self._name = None
        self._short_name = None
        self._season = None
        self._day = None
        self._date_time = None
        self._status = None
        self._active = None
        self.discriminator = None
        if event_id is not None:
            self.event_id = event_id
        if league_id is not None:
            self.league_id = league_id
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if season is not None:
            self.season = season
        if day is not None:
            self.day = day
        if date_time is not None:
            self.date_time = date_time
        if status is not None:
            self.status = status
        if active is not None:
            self.active = active

    @property
    def event_id(self):
        """Gets the event_id of this MmaStatsEvent.  # noqa: E501


        :return: The event_id of this MmaStatsEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this MmaStatsEvent.


        :param event_id: The event_id of this MmaStatsEvent.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def league_id(self):
        """Gets the league_id of this MmaStatsEvent.  # noqa: E501


        :return: The league_id of this MmaStatsEvent.  # noqa: E501
        :rtype: int
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this MmaStatsEvent.


        :param league_id: The league_id of this MmaStatsEvent.  # noqa: E501
        :type: int
        """

        self._league_id = league_id

    @property
    def name(self):
        """Gets the name of this MmaStatsEvent.  # noqa: E501


        :return: The name of this MmaStatsEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MmaStatsEvent.


        :param name: The name of this MmaStatsEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this MmaStatsEvent.  # noqa: E501


        :return: The short_name of this MmaStatsEvent.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this MmaStatsEvent.


        :param short_name: The short_name of this MmaStatsEvent.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def season(self):
        """Gets the season of this MmaStatsEvent.  # noqa: E501


        :return: The season of this MmaStatsEvent.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this MmaStatsEvent.


        :param season: The season of this MmaStatsEvent.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def day(self):
        """Gets the day of this MmaStatsEvent.  # noqa: E501


        :return: The day of this MmaStatsEvent.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this MmaStatsEvent.


        :param day: The day of this MmaStatsEvent.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def date_time(self):
        """Gets the date_time of this MmaStatsEvent.  # noqa: E501


        :return: The date_time of this MmaStatsEvent.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this MmaStatsEvent.


        :param date_time: The date_time of this MmaStatsEvent.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def status(self):
        """Gets the status of this MmaStatsEvent.  # noqa: E501


        :return: The status of this MmaStatsEvent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MmaStatsEvent.


        :param status: The status of this MmaStatsEvent.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def active(self):
        """Gets the active of this MmaStatsEvent.  # noqa: E501


        :return: The active of this MmaStatsEvent.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MmaStatsEvent.


        :param active: The active of this MmaStatsEvent.  # noqa: E501
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
        if issubclass(MmaStatsEvent, dict):
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
        if not isinstance(other, MmaStatsEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
