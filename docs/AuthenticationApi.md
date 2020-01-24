# swagger_client.AuthenticationApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_login**](AuthenticationApi.md#authentication_login) | **POST** /auth/login | User login to get AccessToken to query API data.
[**authentication_refresh**](AuthenticationApi.md#authentication_refresh) | **POST** /auth/refresh | Refresh AccessToken, i.e. get a new AccessToken without loging in.

# **authentication_login**
> AuthenticationModel authentication_login(body)

User login to get AccessToken to query API data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.LoginModel() # LoginModel | Login data (username, password, etc.).

try:
    # User login to get AccessToken to query API data.
    api_response = api_instance.authentication_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginModel**](LoginModel.md)| Login data (username, password, etc.). | 

### Return type

[**AuthenticationModel**](AuthenticationModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_refresh**
> AuthenticationModel authentication_refresh(body)

Refresh AccessToken, i.e. get a new AccessToken without loging in.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.RefreshModel() # RefreshModel | Refresh data (current AccessToken, RefreshToken, etc.).

try:
    # Refresh AccessToken, i.e. get a new AccessToken without loging in.
    api_response = api_instance.authentication_refresh(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshModel**](RefreshModel.md)| Refresh data (current AccessToken, RefreshToken, etc.). | 

### Return type

[**AuthenticationModel**](AuthenticationModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

