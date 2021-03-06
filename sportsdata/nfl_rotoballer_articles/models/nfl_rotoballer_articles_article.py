# coding: utf-8

"""
    NFL v3 RotoBaller Articles

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NflRotoballerArticlesArticle(object):
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
        'article_id': 'int',
        'title': 'str',
        'source': 'str',
        'updated': 'str',
        'content': 'str',
        'url': 'str',
        'terms_of_use': 'str',
        'author': 'str',
        'players': 'list[NflRotoballerArticlesPlayerInfo]'
    }

    attribute_map = {
        'article_id': 'ArticleID',
        'title': 'Title',
        'source': 'Source',
        'updated': 'Updated',
        'content': 'Content',
        'url': 'Url',
        'terms_of_use': 'TermsOfUse',
        'author': 'Author',
        'players': 'Players'
    }

    def __init__(self, article_id=None, title=None, source=None, updated=None, content=None, url=None, terms_of_use=None, author=None, players=None):  # noqa: E501
        """NflRotoballerArticlesArticle - a model defined in Swagger"""  # noqa: E501
        self._article_id = None
        self._title = None
        self._source = None
        self._updated = None
        self._content = None
        self._url = None
        self._terms_of_use = None
        self._author = None
        self._players = None
        self.discriminator = None
        if article_id is not None:
            self.article_id = article_id
        if title is not None:
            self.title = title
        if source is not None:
            self.source = source
        if updated is not None:
            self.updated = updated
        if content is not None:
            self.content = content
        if url is not None:
            self.url = url
        if terms_of_use is not None:
            self.terms_of_use = terms_of_use
        if author is not None:
            self.author = author
        if players is not None:
            self.players = players

    @property
    def article_id(self):
        """Gets the article_id of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The article_id of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: int
        """
        return self._article_id

    @article_id.setter
    def article_id(self, article_id):
        """Sets the article_id of this NflRotoballerArticlesArticle.


        :param article_id: The article_id of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: int
        """

        self._article_id = article_id

    @property
    def title(self):
        """Gets the title of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The title of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NflRotoballerArticlesArticle.


        :param title: The title of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def source(self):
        """Gets the source of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The source of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NflRotoballerArticlesArticle.


        :param source: The source of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def updated(self):
        """Gets the updated of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The updated of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NflRotoballerArticlesArticle.


        :param updated: The updated of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def content(self):
        """Gets the content of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The content of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NflRotoballerArticlesArticle.


        :param content: The content of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def url(self):
        """Gets the url of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The url of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NflRotoballerArticlesArticle.


        :param url: The url of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def terms_of_use(self):
        """Gets the terms_of_use of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The terms_of_use of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_use

    @terms_of_use.setter
    def terms_of_use(self, terms_of_use):
        """Sets the terms_of_use of this NflRotoballerArticlesArticle.


        :param terms_of_use: The terms_of_use of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._terms_of_use = terms_of_use

    @property
    def author(self):
        """Gets the author of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The author of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this NflRotoballerArticlesArticle.


        :param author: The author of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def players(self):
        """Gets the players of this NflRotoballerArticlesArticle.  # noqa: E501


        :return: The players of this NflRotoballerArticlesArticle.  # noqa: E501
        :rtype: list[NflRotoballerArticlesPlayerInfo]
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this NflRotoballerArticlesArticle.


        :param players: The players of this NflRotoballerArticlesArticle.  # noqa: E501
        :type: list[NflRotoballerArticlesPlayerInfo]
        """

        self._players = players

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
        if issubclass(NflRotoballerArticlesArticle, dict):
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
        if not isinstance(other, NflRotoballerArticlesArticle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
