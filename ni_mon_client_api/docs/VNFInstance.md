# VNFInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_container** | **bool** | whether the vnf is a container or a virtual machine | [optional] 
**status** | **str** | state of VNF . (ACTIVE, SHUTOFF, ERROR, Running, etc.). The string can be different between VM and container | [optional] 
**flavor_id** | **str** | the flavor id of the vnf | [optional] 
**image_id** | **str** | i the dockerhub image (if container) or glance image (if VM) used for the vnf | [optional] 
**node_id** | **str** |  | [optional] 
**ports** | [**list[NetworkPort]**](NetworkPort.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


