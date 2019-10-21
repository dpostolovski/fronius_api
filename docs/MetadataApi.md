# swagger_client.MetadataApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_get**](MetadataApi.md#metadata_get) | **GET** /metadata | Gets metadata of all PV systems for the user, identified by the access token.
[**metadata_get_0**](MetadataApi.md#metadata_get_0) | **GET** /metadata/{pvSystemId} | Gets metadata of the PV systems with the given ID.


# **metadata_get**
> list[PvSystemMetadataExpertModel] metadata_get(access_token)

Gets metadata of all PV systems for the user, identified by the access token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets metadata of all PV systems for the user, identified by the access token.
    api_response = api_instance.metadata_get(access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**list[PvSystemMetadataExpertModel]**](PvSystemMetadataExpertModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get_0**
> PvSystemMetadataExpertModel metadata_get_0(pv_system_id, access_token)

Gets metadata of the PV systems with the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
pv_system_id = 'pv_system_id_example' # str | PV system ID as Guid.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets metadata of the PV systems with the given ID.
    api_response = api_instance.metadata_get_0(pv_system_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**PvSystemMetadataExpertModel**](PvSystemMetadataExpertModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

