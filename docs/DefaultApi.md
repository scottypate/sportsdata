# sportsdata.wnba_scores.DefaultApi

All URIs are relative to *https://api.sportsdata.io/v3/wnba/scores*

Method | HTTP request | Description
------------- | ------------- | -------------
[**are_games_in_progress**](DefaultApi.md#are_games_in_progress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
[**current_season**](DefaultApi.md#current_season) | **GET** /{format}/CurrentSeason | Current Season
[**games_by_date**](DefaultApi.md#games_by_date) | **GET** /{format}/GamesByDate/{date} | Games by Date
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Games/{Season} | Schedule
[**stadiums**](DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
[**teams**](DefaultApi.md#teams) | **GET** /{format}/Teams | Teams

# **are_games_in_progress**
> bool are_games_in_progress(format)

Are Games In Progress

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Are Games In Progress
    api_response = api_instance.are_games_in_progress(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->are_games_in_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**bool**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_season**
> WnbaScoresSeason current_season(format)

Current Season

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Current Season
    api_response = api_instance.current_season(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->current_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**WnbaScoresSeason**](WnbaScoresSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_by_date**
> list[WnbaScoresGame] games_by_date(format, _date)

Games by Date

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str | The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.

try:
    # Games by Date
    api_response = api_instance.games_by_date(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->games_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**| The date of the game(s).&lt;br&gt;Examples: &lt;code&gt;2019-MAY-16&lt;/code&gt;, &lt;code&gt;2019-MAY-25&lt;/code&gt;, etc. | 

### Return type

[**list[WnbaScoresGame]**](WnbaScoresGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule**
> list[WnbaScoresGame] schedule(format, season)

Schedule

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season (with optional season type).<br>Examples: <code>2019</code>, <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.

try:
    # Schedule
    api_response = api_instance.schedule(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2019&lt;/code&gt;, &lt;code&gt;2019PRE&lt;/code&gt;, &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2019REG&lt;/code&gt;, etc. | 

### Return type

[**list[WnbaScoresGame]**](WnbaScoresGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stadiums**
> list[WnbaScoresStadium] stadiums(format)

Stadiums

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Stadiums
    api_response = api_instance.stadiums(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stadiums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[WnbaScoresStadium]**](WnbaScoresStadium.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams**
> list[WnbaScoresTeam] teams(format)

Teams

### Example
```python
from __future__ import print_function
import time
import sportsdata.wnba_scores
from sportsdata.wnba_scores.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = sportsdata.wnba_scores.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = sportsdata.wnba_scores.DefaultApi(sportsdata.wnba_scores.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Teams
    api_response = api_instance.teams(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[WnbaScoresTeam]**](WnbaScoresTeam.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

