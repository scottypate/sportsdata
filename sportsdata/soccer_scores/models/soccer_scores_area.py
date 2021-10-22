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

class SoccerScoresArea(object):
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
        'area_id': 'int',
        'country_code': 'str',
        'name': 'str',
        'competitions': 'list[SoccerScoresCompetition]'
    }

    attribute_map = {
        'area_id': 'AreaId',
        'country_code': 'CountryCode',
        'name': 'Name',
        'competitions': 'Competitions'
    }

    def __init__(self, area_id=None, country_code=None, name=None, competitions=None):  # noqa: E501
        """SoccerScoresArea - a model defined in Swagger"""  # noqa: E501
        self._area_id = None
        self._country_code = None
        self._name = None
        self._competitions = None
        self.discriminator = None
        if area_id is not None:
            self.area_id = area_id
        if country_code is not None:
            self.country_code = country_code
        if name is not None:
            self.name = name
        if competitions is not None:
            self.competitions = competitions

    @property
    def area_id(self):
        """Gets the area_id of this SoccerScoresArea.  # noqa: E501


        :return: The area_id of this SoccerScoresArea.  # noqa: E501
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this SoccerScoresArea.


        :param area_id: The area_id of this SoccerScoresArea.  # noqa: E501
        :type: int
        """

        self._area_id = area_id

    @property
    def country_code(self):
        """Gets the country_code of this SoccerScoresArea.  # noqa: E501


        :return: The country_code of this SoccerScoresArea.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SoccerScoresArea.


        :param country_code: The country_code of this SoccerScoresArea.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def name(self):
        """Gets the name of this SoccerScoresArea.  # noqa: E501


        :return: The name of this SoccerScoresArea.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoccerScoresArea.


        :param name: The name of this SoccerScoresArea.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def competitions(self):
        """Gets the competitions of this SoccerScoresArea.  # noqa: E501


        :return: The competitions of this SoccerScoresArea.  # noqa: E501
        :rtype: list[SoccerScoresCompetition]
        """
        return self._competitions

    @competitions.setter
    def competitions(self, competitions):
        """Sets the competitions of this SoccerScoresArea.


        :param competitions: The competitions of this SoccerScoresArea.  # noqa: E501
        :type: list[SoccerScoresCompetition]
        """

        self._competitions = competitions

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
        if issubclass(SoccerScoresArea, dict):
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
        if not isinstance(other, SoccerScoresArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
