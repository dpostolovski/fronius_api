# swagger_client.AggregatedValuesApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregated_values_get_month_values**](AggregatedValuesApi.md#aggregated_values_get_month_values) | **GET** /aggvalues/month | Gets dayly aggregated values for given pv system, year and month  (only available with expert package).
[**aggregated_values_get_total_values**](AggregatedValuesApi.md#aggregated_values_get_total_values) | **GET** /aggvalues/total | Gets yearly aggregated values for given pv system (only available with expert package).
[**aggregated_values_get_year_values**](AggregatedValuesApi.md#aggregated_values_get_year_values) | **GET** /aggvalues/year | Gets monthly aggregated values for given pv system and year  (only available with expert package).

# **aggregated_values_get_month_values**
> AggValuesModel aggregated_values_get_month_values(pv_system_id, year, month, access_token)

Gets dayly aggregated values for given pv system, year and month  (only available with expert package).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatedValuesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
year = 56 # int | The year to get aggregated days for.
month = 56 # int | The month to get aggregated days for.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets dayly aggregated values for given pv system, year and month  (only available with expert package).
    api_response = api_instance.aggregated_values_get_month_values(pv_system_id, year, month, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedValuesApi->aggregated_values_get_month_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **year** | **int**| The year to get aggregated days for. | 
 **month** | **int**| The month to get aggregated days for. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**AggValuesModel**](AggValuesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregated_values_get_total_values**
> AggValuesModel aggregated_values_get_total_values(pv_system_id, access_token)

Gets yearly aggregated values for given pv system (only available with expert package).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatedValuesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets yearly aggregated values for given pv system (only available with expert package).
    api_response = api_instance.aggregated_values_get_total_values(pv_system_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedValuesApi->aggregated_values_get_total_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**AggValuesModel**](AggValuesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregated_values_get_year_values**
> AggValuesModel aggregated_values_get_year_values(pv_system_id, year, access_token)

Gets monthly aggregated values for given pv system and year  (only available with expert package).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatedValuesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
year = 56 # int | The year to get aggregated months for.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets monthly aggregated values for given pv system and year  (only available with expert package).
    api_response = api_instance.aggregated_values_get_year_values(pv_system_id, year, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedValuesApi->aggregated_values_get_year_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **year** | **int**| The year to get aggregated months for. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**AggValuesModel**](AggValuesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

