# coding: utf-8

"""
    NBA v3 Projections

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sportsdata.nba_projections.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dfs_slates_by_date(self, format, _date, **kwargs):  # noqa: E501
        """DFS Slates by Date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dfs_slates_by_date(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>. (required)
        :return: list[NbaProjectionsDfsSlate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dfs_slates_by_date_with_http_info(format, _date, **kwargs)  # noqa: E501
        else:
            (data) = self.dfs_slates_by_date_with_http_info(format, _date, **kwargs)  # noqa: E501
            return data

    def dfs_slates_by_date_with_http_info(self, format, _date, **kwargs):  # noqa: E501
        """DFS Slates by Date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dfs_slates_by_date_with_http_info(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>. (required)
        :return: list[NbaProjectionsDfsSlate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', '_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dfs_slates_by_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `dfs_slates_by_date`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `dfs_slates_by_date`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501

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
            '/{format}/DfsSlatesByDate/{date}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NbaProjectionsDfsSlate]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projected_player_game_stats_by_date_w_injuries_dfs_salaries(self, format, _date, **kwargs):  # noqa: E501
        """Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_game_stats_by_date_w_injuries_dfs_salaries(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>. (required)
        :return: list[NbaProjectionsPlayerGameProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projected_player_game_stats_by_date_w_injuries_dfs_salaries_with_http_info(format, _date, **kwargs)  # noqa: E501
        else:
            (data) = self.projected_player_game_stats_by_date_w_injuries_dfs_salaries_with_http_info(format, _date, **kwargs)  # noqa: E501
            return data

    def projected_player_game_stats_by_date_w_injuries_dfs_salaries_with_http_info(self, format, _date, **kwargs):  # noqa: E501
        """Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_game_stats_by_date_w_injuries_dfs_salaries_with_http_info(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>. (required)
        :return: list[NbaProjectionsPlayerGameProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', '_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projected_player_game_stats_by_date_w_injuries_dfs_salaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `projected_player_game_stats_by_date_w_injuries_dfs_salaries`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `projected_player_game_stats_by_date_w_injuries_dfs_salaries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501

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
            '/{format}/PlayerGameProjectionStatsByDate/{date}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NbaProjectionsPlayerGameProjection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projected_player_game_stats_by_player_w_injuries_dfs_salaries(self, format, _date, playerid, **kwargs):  # noqa: E501
        """Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_game_stats_by_player_w_injuries_dfs_salaries(format, _date, playerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s).<br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>. (required)
        :param str playerid: Unique FantasyData Player ID. Example:<code>20000571</code>. (required)
        :return: NbaProjectionsPlayerGameProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projected_player_game_stats_by_player_w_injuries_dfs_salaries_with_http_info(format, _date, playerid, **kwargs)  # noqa: E501
        else:
            (data) = self.projected_player_game_stats_by_player_w_injuries_dfs_salaries_with_http_info(format, _date, playerid, **kwargs)  # noqa: E501
            return data

    def projected_player_game_stats_by_player_w_injuries_dfs_salaries_with_http_info(self, format, _date, playerid, **kwargs):  # noqa: E501
        """Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_game_stats_by_player_w_injuries_dfs_salaries_with_http_info(format, _date, playerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s).<br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>. (required)
        :param str playerid: Unique FantasyData Player ID. Example:<code>20000571</code>. (required)
        :return: NbaProjectionsPlayerGameProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', '_date', 'playerid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projected_player_game_stats_by_player_w_injuries_dfs_salaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `projected_player_game_stats_by_player_w_injuries_dfs_salaries`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `projected_player_game_stats_by_player_w_injuries_dfs_salaries`")  # noqa: E501
        # verify the required parameter 'playerid' is set
        if ('playerid' not in params or
                params['playerid'] is None):
            raise ValueError("Missing the required parameter `playerid` when calling `projected_player_game_stats_by_player_w_injuries_dfs_salaries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501
        if 'playerid' in params:
            path_params['playerid'] = params['playerid']  # noqa: E501

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
            '/{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NbaProjectionsPlayerGameProjection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projected_player_season_stats(self, format, season, **kwargs):  # noqa: E501
        """Projected Player Season Stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats(format, season, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :return: list[NbaProjectionsPlayerSeasonProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projected_player_season_stats_with_http_info(format, season, **kwargs)  # noqa: E501
        else:
            (data) = self.projected_player_season_stats_with_http_info(format, season, **kwargs)  # noqa: E501
            return data

    def projected_player_season_stats_with_http_info(self, format, season, **kwargs):  # noqa: E501
        """Projected Player Season Stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats_with_http_info(format, season, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :return: list[NbaProjectionsPlayerSeasonProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'season']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projected_player_season_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `projected_player_season_stats`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `projected_player_season_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'season' in params:
            path_params['season'] = params['season']  # noqa: E501

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
            '/{format}/PlayerSeasonProjectionStats/{season}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NbaProjectionsPlayerSeasonProjection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projected_player_season_stats_by_player(self, format, season, playerid, **kwargs):  # noqa: E501
        """Projected Player Season Stats by Player  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats_by_player(format, season, playerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :param str playerid: Unique FantasyData Player ID. Example:<code>20000571</code>. (required)
        :return: NbaProjectionsPlayerSeasonProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projected_player_season_stats_by_player_with_http_info(format, season, playerid, **kwargs)  # noqa: E501
        else:
            (data) = self.projected_player_season_stats_by_player_with_http_info(format, season, playerid, **kwargs)  # noqa: E501
            return data

    def projected_player_season_stats_by_player_with_http_info(self, format, season, playerid, **kwargs):  # noqa: E501
        """Projected Player Season Stats by Player  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats_by_player_with_http_info(format, season, playerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :param str playerid: Unique FantasyData Player ID. Example:<code>20000571</code>. (required)
        :return: NbaProjectionsPlayerSeasonProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'season', 'playerid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projected_player_season_stats_by_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `projected_player_season_stats_by_player`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `projected_player_season_stats_by_player`")  # noqa: E501
        # verify the required parameter 'playerid' is set
        if ('playerid' not in params or
                params['playerid'] is None):
            raise ValueError("Missing the required parameter `playerid` when calling `projected_player_season_stats_by_player`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'season' in params:
            path_params['season'] = params['season']  # noqa: E501
        if 'playerid' in params:
            path_params['playerid'] = params['playerid']  # noqa: E501

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
            '/{format}/PlayerSeasonProjectionStatsByPlayer/{season}/{playerid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NbaProjectionsPlayerSeasonProjection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projected_player_season_stats_by_team(self, format, season, team, **kwargs):  # noqa: E501
        """Projected Player Season Stats by Team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats_by_team(format, season, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :param str team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>. (required)
        :return: list[NbaProjectionsPlayerSeasonProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projected_player_season_stats_by_team_with_http_info(format, season, team, **kwargs)  # noqa: E501
        else:
            (data) = self.projected_player_season_stats_by_team_with_http_info(format, season, team, **kwargs)  # noqa: E501
            return data

    def projected_player_season_stats_by_team_with_http_info(self, format, season, team, **kwargs):  # noqa: E501
        """Projected Player Season Stats by Team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projected_player_season_stats_by_team_with_http_info(format, season, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc. (required)
        :param str team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>. (required)
        :return: list[NbaProjectionsPlayerSeasonProjection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'season', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projected_player_season_stats_by_team" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `projected_player_season_stats_by_team`")  # noqa: E501
        # verify the required parameter 'season' is set
        if ('season' not in params or
                params['season'] is None):
            raise ValueError("Missing the required parameter `season` when calling `projected_player_season_stats_by_team`")  # noqa: E501
        # verify the required parameter 'team' is set
        if ('team' not in params or
                params['team'] is None):
            raise ValueError("Missing the required parameter `team` when calling `projected_player_season_stats_by_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'season' in params:
            path_params['season'] = params['season']  # noqa: E501
        if 'team' in params:
            path_params['team'] = params['team']  # noqa: E501

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
            '/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NbaProjectionsPlayerSeasonProjection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def starting_lineups_by_date(self, format, _date, **kwargs):  # noqa: E501
        """Starting Lineups by Date  # noqa: E501

        This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.starting_lineups_by_date(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>. (required)
        :return: list[NbaProjectionsStartingLineups]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.starting_lineups_by_date_with_http_info(format, _date, **kwargs)  # noqa: E501
        else:
            (data) = self.starting_lineups_by_date_with_http_info(format, _date, **kwargs)  # noqa: E501
            return data

    def starting_lineups_by_date_with_http_info(self, format, _date, **kwargs):  # noqa: E501
        """Starting Lineups by Date  # noqa: E501

        This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.starting_lineups_by_date_with_http_info(format, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str format: Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>. (required)
        :param str _date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>. (required)
        :return: list[NbaProjectionsStartingLineups]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', '_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method starting_lineups_by_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `starting_lineups_by_date`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `starting_lineups_by_date`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501

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
            '/{format}/StartingLineupsByDate/{date}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NbaProjectionsStartingLineups]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
