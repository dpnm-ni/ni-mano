# nfvo_client.VnfApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_vnf**](VnfApi.md#deploy_vnf) | **POST** /vnfs | Instantiate an instance of a VNF flavor on a given node.
[**destroy_vnf**](VnfApi.md#destroy_vnf) | **DELETE** /vnfs/{id} | Destroy a VNF instance.
[**shutdown_vnf**](VnfApi.md#shutdown_vnf) | **POST** /vnfs/{id}/shutdown | Shut down a VNF instance.


# **deploy_vnf**
> str deploy_vnf(body)

Instantiate an instance of a VNF flavor on a given node.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.VnfApi()
body = nfvo_client.Body() # Body | Flavor of VNF instance to be deployed as well as the target node. vnf_name is optional

try:
    # Instantiate an instance of a VNF flavor on a given node.
    api_response = api_instance.deploy_vnf(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfApi->deploy_vnf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Flavor of VNF instance to be deployed as well as the target node. vnf_name is optional | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vnf**
> destroy_vnf(id)

Destroy a VNF instance.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.VnfApi()
id = 'id_example' # str | vnf id

try:
    # Destroy a VNF instance.
    api_instance.destroy_vnf(id)
except ApiException as e:
    print("Exception when calling VnfApi->destroy_vnf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| vnf id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_vnf**
> shutdown_vnf(id)

Shut down a VNF instance.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.VnfApi()
id = 'id_example' # str | ID of VNF instance to be shut down.

try:
    # Shut down a VNF instance.
    api_instance.shutdown_vnf(id)
except ApiException as e:
    print("Exception when calling VnfApi->shutdown_vnf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VNF instance to be shut down. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

