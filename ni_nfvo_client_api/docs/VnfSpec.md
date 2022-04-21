# VnfSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavor_id** | **str** | flavor used to deploy vnf | 
**node_name** | **str** | name of the compute node where Vnf will be deployed | [optional] 
**vnf_name** | **str** |  | [optional] 
**user_data** | **str** | [VM only] configuration to pass to the Vnf at boot (e.g., cloud-init) | [optional] 
**image_id** | **str** | if container: put the dockerhub container (e.g., ubuntu:18.04). If VM, put the OS image id. default to ubuntu image id in the config file | [optional] 
**command** | **list[str]** | [Container only] Command to run when start the container,e.g., ./script.sh | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


