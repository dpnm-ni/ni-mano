# Sfcr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**arrivaltime** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**source_client** | **str** | the id of the source VM/container (not Vnf) | [optional] 
**destination_client** | **str** | the id of the destination VM/container (not Vnf) | [optional] 
**src_ip_prefix** | **str** |  | [optional] 
**dst_ip_prefix** | **str** |  | [optional] 
**src_port_min** | **int** |  | [optional] 
**src_port_max** | **int** |  | [optional] 
**dst_port_min** | **int** |  | [optional] 
**dst_port_max** | **int** |  | [optional] 
**proto** | **str** |  | [optional] 
**bw** | **int** | bandwidth requirement of the sfcr | [optional] 
**delay** | **int** | delay requirement of the sfcr | [optional] 
**duration** | **int** | sfcr running duration | [optional] 
**nf_chain** | **list[str]** | the type of Vnfs in the path (e.g.: fw, ids, nat, etc.). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


