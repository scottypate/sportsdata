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

class GolfV2Season(object):
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
        'season_id': 'int',
        'description': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'season_id': 'SeasonID',
        'description': 'Description',
        'start_date': 'StartDate',
        'end_date': 'EndDate'
    }

    def __init__(self, season_id=None, description=None, start_date=None, end_date=None):  # noqa: E501
        """GolfV2Season - a model defined in Swagger"""  # noqa: E501
        self._season_id = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None
        if season_id is not None:
            self.season_id = season_id
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def season_id(self):
        """Gets the season_id of this GolfV2Season.  # noqa: E501


        :return: The season_id of this GolfV2Season.  # noqa: E501
        :rtype: int
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id):
        """Sets the season_id of this GolfV2Season.


        :param season_id: The season_id of this GolfV2Season.  # noqa: E501
        :type: int
        """

        self._season_id = season_id

    @property
    def description(self):
        """Gets the description of this GolfV2Season.  # noqa: E501


        :return: The description of this GolfV2Season.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GolfV2Season.


        :param description: The description of this GolfV2Season.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def start_date(self):
        """Gets the start_date of this GolfV2Season.  # noqa: E501


        :return: The start_date of this GolfV2Season.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GolfV2Season.


        :param start_date: The start_date of this GolfV2Season.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this GolfV2Season.  # noqa: E501


        :return: The end_date of this GolfV2Season.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GolfV2Season.


        :param end_date: The end_date of this GolfV2Season.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

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
        if issubclass(GolfV2Season, dict):
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
        if not isinstance(other, GolfV2Season):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
