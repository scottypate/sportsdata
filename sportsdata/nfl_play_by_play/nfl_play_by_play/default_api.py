# coding: utf-8

"""
    NFL v3 Play-by-Play

    NFL play-by-play API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sportsdata.nfl_play_by_play.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def play_by_play(self, format, season, week, hometeam, **kwargs):  # noqa: E501
        """Play By Play  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play(format, season, week, hometeam, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.          (required)
        :param str week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>          (required)
        :param str hometeam: Abbreviation of the home team. Example: <code>WAS</code>. (required)
        :return: NflPlayByPlayPlayByPlay
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.play_by_play_with_http_info(format, season, week, hometeam, **kwargs)  # noqa: E501
        else:
            (data) = self.play_by_play_with_http_info(format, season, week, hometeam, **kwargs)  # noqa: E501
            return data

    def play_by_play_with_http_info(self, format, season, week, hometeam, **kwargs):  # noqa: E501
        """Play By Play  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play_with_http_info(format, season, week, hometeam, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.          (required)
        :param str week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>          (required)
        :param str hometeam: Abbreviation of the home team. Example: <code>WAS</code>. (required)
        :return: NflPlayByPlayPlayByPlay
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'season', 'week', 'hometeam']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method play_by_play" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `play_by_play`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `play_by_play`")  # noqa: E501
        # verify the required parameter 'week' is set
        if ('week' not in params or
                params['week'] is None):
            raise ValueError("Missing the required parameter `week` when calling `play_by_play`")  # noqa: E501
        # verify the required parameter 'hometeam' is set
        if ('hometeam' not in params or
                params['hometeam'] is None):
            raise ValueError("Missing the required parameter `hometeam` when calling `play_by_play`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'season' in params:
            path_params['season'] = params['season']  # noqa: E501
        if 'week' in params:
            path_params['week'] = params['week']  # noqa: E501
        if 'hometeam' in params:
            path_params['hometeam'] = params['hometeam']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/{format}/PlayByPlay/{season}/{week}/{hometeam}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NflPlayByPlayPlayByPlay',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def play_by_play_delta(self, format, season, week, minutes, **kwargs):  # noqa: E501
        """Play By Play Delta  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play_delta(format, season, week, minutes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.          (required)
        :param str week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>          (required)
        :param str minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.          (required)
        :return: list[NflPlayByPlayPlayByPlay]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.play_by_play_delta_with_http_info(format, season, week, minutes, **kwargs)  # noqa: E501
        else:
            (data) = self.play_by_play_delta_with_http_info(format, season, week, minutes, **kwargs)  # noqa: E501
            return data

    def play_by_play_delta_with_http_info(self, format, season, week, minutes, **kwargs):  # noqa: E501
        """Play By Play Delta  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play_delta_with_http_info(format, season, week, minutes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.          (required)
        :param str week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>          (required)
        :param str minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.          (required)
        :return: list[NflPlayByPlayPlayByPlay]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'season', 'week', 'minutes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method play_by_play_delta" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `play_by_play_delta`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `play_by_play_delta`")  # noqa: E501
        # verify the required parameter 'week' is set
        if ('week' not in params or
                params['week'] is None):
            raise ValueError("Missing the required parameter `week` when calling `play_by_play_delta`")  # noqa: E501
        # verify the required parameter 'minutes' is set
        if ('minutes' not in params or
                params['minutes'] is None):
            raise ValueError("Missing the required parameter `minutes` when calling `play_by_play_delta`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'season' in params:
            path_params['season'] = params['season']  # noqa: E501
        if 'week' in params:
            path_params['week'] = params['week']  # noqa: E501
        if 'minutes' in params:
            path_params['minutes'] = params['minutes']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/{format}/PlayByPlayDelta/{season}/{week}/{minutes}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NflPlayByPlayPlayByPlay]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def play_by_play_simulation(self, format, numberofplays, **kwargs):  # noqa: E501
        """Play By Play Simulation  # noqa: E501

        Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play_simulation(format, numberofplays, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc. (required)
        :return: list[NflPlayByPlayPlayByPlay]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.play_by_play_simulation_with_http_info(format, numberofplays, **kwargs)  # noqa: E501
        else:
            (data) = self.play_by_play_simulation_with_http_info(format, numberofplays, **kwargs)  # noqa: E501
            return data

    def play_by_play_simulation_with_http_info(self, format, numberofplays, **kwargs):  # noqa: E501
        """Play By Play Simulation  # noqa: E501

        Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.play_by_play_simulation_with_http_info(format, numberofplays, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc. (required)
        :return: list[NflPlayByPlayPlayByPlay]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'numberofplays']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method play_by_play_simulation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `play_by_play_simulation`")  # noqa: E501
        # verify the required parameter 'numberofplays' is set
        if ('numberofplays' not in params or
                params['numberofplays'] is None):
            raise ValueError("Missing the required parameter `numberofplays` when calling `play_by_play_simulation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'numberofplays' in params:
            path_params['numberofplays'] = params['numberofplays']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/{format}/SimulatedPlayByPlay/{numberofplays}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NflPlayByPlayPlayByPlay]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
