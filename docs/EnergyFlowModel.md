# EnergyFlowModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_online** | **bool** | Is PV system online. | [optional] 
**p_grid** | **float** | Current flow from/to grid. | [optional] 
**p_load** | **float** | Current flow to consumer. | [optional] 
**p_akku** | **float** | Current flow from/to battery, if battery available. | [optional] 
**p_pv** | **float** | Current flow from PV. | [optional] 
**soc** | **float** | Battery state of charge, if battery available. | [optional] 
**batt_mode** | **str** | Battery mode, if battery available. | [optional] 
**p_ohm_pilot** | **float** | Current flow to Ohm pilot, if Ohm pilot available. | [optional] 
**t_ohm_pilot** | **float** | Current temperature of Ohm pilot, if Ohm pilot available. | [optional] 
**own_consumption** | **float** |  | [optional] 
**self_sufficiency** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

