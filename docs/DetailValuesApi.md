# swagger_client.DetailValuesApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_values_get_detail_values**](DetailValuesApi.md#detail_values_get_detail_values) | **GET** /detailvalues/{pvSystemId} | Gets a list of values for the given pv system, date range and channel type, whereby the date range is restricted to 24 hours   (some channels are only available with expert package).

# **detail_values_get_detail_values**
> list[DetailValueModel] detail_values_get_detail_values(pv_system_id, _from, to, channel_type, access_token)

Gets a list of values for the given pv system, date range and channel type, whereby the date range is restricted to 24 hours   (some channels are only available with expert package).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DetailValuesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
_from = '2013-10-20T19:20:30+01:00' # datetime | Start date time.
to = '2013-10-20T19:20:30+01:00' # datetime | End date time.
channel_type = 'channel_type_example' # str | Channel type to get values for.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets a list of values for the given pv system, date range and channel type, whereby the date range is restricted to 24 hours   (some channels are only available with expert package).
    api_response = api_instance.detail_values_get_detail_values(pv_system_id, _from, to, channel_type, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetailValuesApi->detail_values_get_detail_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **_from** | **datetime**| Start date time. | 
 **to** | **datetime**| End date time. | 
 **channel_type** | **str**| Channel type to get values for. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**list[DetailValueModel]**](DetailValueModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

