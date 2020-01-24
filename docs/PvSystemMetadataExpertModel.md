# PvSystemMetadataExpertModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_import** | **datetime** | Last data import for pv system (only available with expert package). | [optional] 
**id** | **str** | PV system ID as Guid. | [optional] 
**name** | **str** | PV system name. | [optional] 
**peak_power** | **float** | Total peak power of PV system. | [optional] 
**address** | [**AddressModel**](AddressModel.md) |  | [optional] 
**installation_date** | **datetime** | Installation date of PV system. | [optional] 
**dalo_device_info** | [**dict(str, DeviceInfoModel)**](DeviceInfoModel.md) | Dictionary of device infos for dalo ids. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

