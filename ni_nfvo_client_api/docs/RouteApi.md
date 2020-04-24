# nfvo_client.RouteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_route**](RouteApi.md#del_route) | **DELETE** /routes/{id} | Delete a Route.
[**get_routes**](RouteApi.md#get_routes) | **GET** /routes | Get current route information, i.e., list of all active SFCRs including their paths.
[**set_route**](RouteApi.md#set_route) | **POST** /routes | Route a request via the provided route. Return route id if success (which also means input route id is ommitted).
[**update_route**](RouteApi.md#update_route) | **PUT** /routes/{id} | Update a new route path or new sfcrs.


# **del_route**
> del_route(id)

Delete a Route.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.RouteApi()
id = 'id_example' # str | route id

try:
    # Delete a Route.
    api_instance.del_route(id)
except ApiException as e:
    print("Exception when calling RouteApi->del_route: %s\n" % e)
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

# **get_routes**
> list[Route] get_routes()

Get current route information, i.e., list of all active SFCRs including their paths.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.RouteApi()

try:
    # Get current route information, i.e., list of all active SFCRs including their paths.
    api_response = api_instance.get_routes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->get_routes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Route]**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_route**
> str set_route(body)

Route a request via the provided route. Return route id if success (which also means input route id is ommitted).



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.RouteApi()
body = nfvo_client.Route() # Route | Route information including SFCR ID and vnf instance ids.

try:
    # Route a request via the provided route. Return route id if success (which also means input route id is ommitted).
    api_response = api_instance.set_route(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->set_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Route**](Route.md)| Route information including SFCR ID and vnf instance ids. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route**
> str update_route(id, body)

Update a new route path or new sfcrs.



### Example
```python
from __future__ import print_function
import time
import nfvo_client
from nfvo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nfvo_client.RouteApi()
id = 'id_example' # str | route id
body = nfvo_client.RouteUpdate() # RouteUpdate | Route Update info.

try:
    # Update a new route path or new sfcrs.
    api_response = api_instance.update_route(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->update_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| route id | 
 **body** | [**RouteUpdate**](RouteUpdate.md)| Route Update info. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

