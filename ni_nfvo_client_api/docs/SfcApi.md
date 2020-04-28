# ni_nfvo_client.SfcApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_sfc**](SfcApi.md#del_sfc) | **DELETE** /sfcs/{id} | Delete a Sfc.
[**get_sfcs**](SfcApi.md#get_sfcs) | **GET** /sfcs | Get current sfc information, i.e., list of all active Sfcrs including their paths.
[**set_sfc**](SfcApi.md#set_sfc) | **POST** /sfcs | Create a Sfc. Return sfc ID if success.
[**update_sfc**](SfcApi.md#update_sfc) | **PUT** /sfcs/{id} | Update a new sfc path or new sfcrs.


# **del_sfc**
> del_sfc(id)

Delete a Sfc.



### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcApi()
id = 'id_example' # str | sfc id

try:
    # Delete a Sfc.
    api_instance.del_sfc(id)
except ApiException as e:
    print("Exception when calling SfcApi->del_sfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sfc id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfcs**
> list[Sfc] get_sfcs()

Get current sfc information, i.e., list of all active Sfcrs including their paths.



### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcApi()

try:
    # Get current sfc information, i.e., list of all active Sfcrs including their paths.
    api_response = api_instance.get_sfcs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfcApi->get_sfcs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sfc]**](Sfc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sfc**
> str set_sfc(sfc_spec)

Create a Sfc. Return sfc ID if success.



### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcApi()
sfc_spec = ni_nfvo_client.SfcSpec() # SfcSpec | Sfc information including Sfcr ID and vnf instance ids.

try:
    # Create a Sfc. Return sfc ID if success.
    api_response = api_instance.set_sfc(sfc_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfcApi->set_sfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sfc_spec** | [**SfcSpec**](SfcSpec.md)| Sfc information including Sfcr ID and vnf instance ids. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfc**
> str update_sfc(id, sfc_update_spec)

Update a new sfc path or new sfcrs.



### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcApi()
id = 'id_example' # str | sfc id
sfc_update_spec = ni_nfvo_client.SfcUpdateSpec() # SfcUpdateSpec | Sfc Update info.

try:
    # Update a new sfc path or new sfcrs.
    api_response = api_instance.update_sfc(id, sfc_update_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfcApi->update_sfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sfc id | 
 **sfc_update_spec** | [**SfcUpdateSpec**](SfcUpdateSpec.md)| Sfc Update info. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

