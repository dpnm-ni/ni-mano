# ni_nfvo_client.SfcrApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sfcr**](SfcrApi.md#add_sfcr) | **POST** /sfcrs | Add new SFC request. return sfcr ID if success
[**del_sfcr**](SfcrApi.md#del_sfcr) | **DELETE** /sfcrs/{id} | Delete a sfcr.
[**get_sfcrs**](SfcrApi.md#get_sfcrs) | **GET** /sfcrs | Get currently active SFC requests.


# **add_sfcr**
> str add_sfcr(sfcr_spec)

Add new SFC request. return sfcr ID if success

### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcrApi()
sfcr_spec = ni_nfvo_client.SFCRSpec() # SFCRSpec | SFC request object to be added.

try:
    # Add new SFC request. return sfcr ID if success
    api_response = api_instance.add_sfcr(sfcr_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfcrApi->add_sfcr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sfcr_spec** | [**SFCRSpec**](SFCRSpec.md)| SFC request object to be added. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_sfcr**
> del_sfcr(id)

Delete a sfcr.



### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcrApi()
id = 'id_example' # str | route id

try:
    # Delete a sfcr.
    api_instance.del_sfcr(id)
except ApiException as e:
    print("Exception when calling SfcrApi->del_sfcr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| route id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfcrs**
> list[SFCR] get_sfcrs()

Get currently active SFC requests.

### Example
```python
from __future__ import print_function
import time
import ni_nfvo_client
from ni_nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_nfvo_client.SfcrApi()

try:
    # Get currently active SFC requests.
    api_response = api_instance.get_sfcrs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfcrApi->get_sfcrs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SFCR]**](SFCR.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

