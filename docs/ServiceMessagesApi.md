# swagger_client.ServiceMessagesApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_messages_get_service_messages**](ServiceMessagesApi.md#service_messages_get_service_messages) | **GET** /servicemessages/{pvSystemId} | Gets a list of errors and events for a given PV system and date range with texts in given language.

# **service_messages_get_service_messages**
> list[ServiceMessageModel] service_messages_get_service_messages(pv_system_id, access_token, start_date=start_date, end_date=end_date, language_code=language_code)

Gets a list of errors and events for a given PV system and date range with texts in given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceMessagesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date, default today (UTC). (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date, default today (UTC). (optional)
language_code = 'language_code_example' # str | Two letter ISO language code. (optional)

try:
    # Gets a list of errors and events for a given PV system and date range with texts in given language.
    api_response = api_instance.service_messages_get_service_messages(pv_system_id, access_token, start_date=start_date, end_date=end_date, language_code=language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceMessagesApi->service_messages_get_service_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 
 **start_date** | **datetime**| Start date, default today (UTC). | [optional] 
 **end_date** | **datetime**| End date, default today (UTC). | [optional] 
 **language_code** | **str**| Two letter ISO language code. | [optional] 

### Return type

[**list[ServiceMessageModel]**](ServiceMessageModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

