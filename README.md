# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatedValuesApi(swagger_client.ApiClient(configuration))
pv_system_id = 'pv_system_id_example' # str | PV system ID as Guid.
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

## Documentation for API Endpoints

All URIs are relative to *https://api.solarweb.com/thirdparty*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AggregatedValuesApi* | [**aggregated_values_get_month_values**](docs/AggregatedValuesApi.md#aggregated_values_get_month_values) | **GET** /aggvalues/month | Gets dayly aggregated values for given pv system, year and month  (only available with expert package).
*AggregatedValuesApi* | [**aggregated_values_get_total_values**](docs/AggregatedValuesApi.md#aggregated_values_get_total_values) | **GET** /aggvalues/total | Gets yearly aggregated values for given pv system (only available with expert package).
*AggregatedValuesApi* | [**aggregated_values_get_year_values**](docs/AggregatedValuesApi.md#aggregated_values_get_year_values) | **GET** /aggvalues/year | Gets monthly aggregated values for given pv system and year  (only available with expert package).
*AuthenticationApi* | [**authentication_login**](docs/AuthenticationApi.md#authentication_login) | **POST** /auth/login | User login to get AccessToken to query API data.
*AuthenticationApi* | [**authentication_refresh**](docs/AuthenticationApi.md#authentication_refresh) | **POST** /auth/refresh | Refresh AccessToken, i.e. get a new AccessToken without loging in.
*DetailValuesApi* | [**detail_values_get_detail_values**](docs/DetailValuesApi.md#detail_values_get_detail_values) | **GET** /detailvalues/{pvSystemId} | Gets a list of values for the given pv system, date range and channel type, whereby the date range is restricted to 24 hours   (some channels are only available with expert package).
*EnergyFlowValuesApi* | [**energy_flow_values_get_for_pv_system**](docs/EnergyFlowValuesApi.md#energy_flow_values_get_for_pv_system) | **GET** /energyflow/{pvSystemId} | Gets energy flow values for given pv system (only available with expert package).
*MetadataApi* | [**metadata_get**](docs/MetadataApi.md#metadata_get) | **GET** /metadata | Gets metadata of all PV systems for the user, identified by the access token.
*MetadataApi* | [**metadata_get_0**](docs/MetadataApi.md#metadata_get_0) | **GET** /metadata/{pvSystemId} | Gets metadata of the PV systems with the given ID.
*RealtimeApi* | [**realtime_get**](docs/RealtimeApi.md#realtime_get) | **GET** /realtime/{pvSystemId} | Gets realtime values for given pv system for user.
*ServiceMessagesApi* | [**service_messages_get_service_messages**](docs/ServiceMessagesApi.md#service_messages_get_service_messages) | **GET** /servicemessages/{pvSystemId} | Gets a list of errors and events for a given PV system and date range with texts in given language.


## Documentation For Models

 - [AddressModel](docs/AddressModel.md)
 - [AggValuesModel](docs/AggValuesModel.md)
 - [AuthenticationModel](docs/AuthenticationModel.md)
 - [BatteryInfoModel](docs/BatteryInfoModel.md)
 - [DetailValueModel](docs/DetailValueModel.md)
 - [DeviceInfoModel](docs/DeviceInfoModel.md)
 - [EnergyFlowModel](docs/EnergyFlowModel.md)
 - [InverterInfoModel](docs/InverterInfoModel.md)
 - [LoginModel](docs/LoginModel.md)
 - [PvSystemMetadataExpertModel](docs/PvSystemMetadataExpertModel.md)
 - [RealtimeInverterExpertModel](docs/RealtimeInverterExpertModel.md)
 - [RefreshModel](docs/RefreshModel.md)
 - [ServiceMessageModel](docs/ServiceMessageModel.md)
 - [ValueUnit](docs/ValueUnit.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



