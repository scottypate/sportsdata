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

class NascarV2RaceResult(object):
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
        'race': 'NascarV2Race',
        'driver_races': 'list[NascarV2DriverRace]'
    }

    attribute_map = {
        'race': 'Race',
        'driver_races': 'DriverRaces'
    }

    def __init__(self, race=None, driver_races=None):  # noqa: E501
        """NascarV2RaceResult - a model defined in Swagger"""  # noqa: E501
        self._race = None
        self._driver_races = None
        self.discriminator = None
        if race is not None:
            self.race = race
        if driver_races is not None:
            self.driver_races = driver_races

    @property
    def race(self):
        """Gets the race of this NascarV2RaceResult.  # noqa: E501


        :return: The race of this NascarV2RaceResult.  # noqa: E501
        :rtype: NascarV2Race
        """
        return self._race

    @race.setter
    def race(self, race):
        """Sets the race of this NascarV2RaceResult.


        :param race: The race of this NascarV2RaceResult.  # noqa: E501
        :type: NascarV2Race
        """

        self._race = race

    @property
    def driver_races(self):
        """Gets the driver_races of this NascarV2RaceResult.  # noqa: E501


        :return: The driver_races of this NascarV2RaceResult.  # noqa: E501
        :rtype: list[NascarV2DriverRace]
        """
        return self._driver_races

    @driver_races.setter
    def driver_races(self, driver_races):
        """Sets the driver_races of this NascarV2RaceResult.


        :param driver_races: The driver_races of this NascarV2RaceResult.  # noqa: E501
        :type: list[NascarV2DriverRace]
        """

        self._driver_races = driver_races

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
        if issubclass(NascarV2RaceResult, dict):
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
        if not isinstance(other, NascarV2RaceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
