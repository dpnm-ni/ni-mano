# Sfc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**sfc_name** | **str** |  | [optional] 
**sfcr_ids** | **list[str]** |  | [optional] 
**vnf_instance_ids** | **list[list[str]]** | list of list of vnf id(s). Each sub-list is a node in traffic path, where traffic are load-balanced between Vnfs in the node. Each E.g.: [[A,B], [C], [D]] : traffic go to [A, B] node (load-balanced between A and B), then go to C, then go to D. | [optional] 
**is_symmetric** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


