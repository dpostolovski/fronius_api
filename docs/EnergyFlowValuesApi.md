# swagger_client.EnergyFlowValuesApi

All URIs are relative to *https://api.solarweb.com/thirdparty*

Method | HTTP request | Description
------------- | ------------- | -------------
[**energy_flow_values_get_for_pv_system**](EnergyFlowValuesApi.md#energy_flow_values_get_for_pv_system) | **GET** /energyflow/{pvSystemId} | Gets energy flow values for given pv system (only available with expert package).

# **energy_flow_values_get_for_pv_system**
> EnergyFlowModel energy_flow_values_get_for_pv_system(pv_system_id, access_token)

Gets energy flow values for given pv system (only available with expert package).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnergyFlowValuesApi()
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | PV system ID as Guid.
access_token = 'access_token_example' # str | access token obtained from the service method /auth/login

try:
    # Gets energy flow values for given pv system (only available with expert package).
    api_response = api_instance.energy_flow_values_get_for_pv_system(pv_system_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnergyFlowValuesApi->energy_flow_values_get_for_pv_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| PV system ID as Guid. | 
 **access_token** | **str**| access token obtained from the service method /auth/login | 

### Return type

[**EnergyFlowModel**](EnergyFlowModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

