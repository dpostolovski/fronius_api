# swagger_client.RealtimeApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realtime_get**](RealtimeApi.md#realtime_get) | **GET** /realtime/{pvSystemId} | Gets realtime values for given pv system for user.

# **realtime_get**
> RealtimeInverterExpertModel realtime_get(pv_system_id, access_token)

Gets realtime values for given pv system for user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RealtimeApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system Id as Guid.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets realtime values for given pv system for user.
    api_response = api_instance.realtime_get(pv_system_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RealtimeApi->realtime_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system Id as Guid. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**RealtimeInverterExpertModel**](RealtimeInverterExpertModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

