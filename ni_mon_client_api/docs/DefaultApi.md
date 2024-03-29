# ni_mon_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_measurement**](DefaultApi.md#get_last_measurement) | **GET** /last_measurement/{id}/{measurement_type} | Return the latest value of a measurement of a vnf instance or compute node
[**get_link**](DefaultApi.md#get_link) | **GET** /link/{id} | get a link
[**get_link_between_nodes**](DefaultApi.md#get_link_between_nodes) | **GET** /link_between_nodes | get detailed information of a link between two specific nodes
[**get_links**](DefaultApi.md#get_links) | **GET** /links | get list of link
[**get_measurement**](DefaultApi.md#get_measurement) | **GET** /measurements/{id}/{measurement_type} | Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period
[**get_measurement_types**](DefaultApi.md#get_measurement_types) | **GET** /measurement_types/{id} | get a list of measurements of a vnf instance or a compute node
[**get_node**](DefaultApi.md#get_node) | **GET** /nodes/{id} | get information of a node
[**get_nodes**](DefaultApi.md#get_nodes) | **GET** /nodes | get a list of nodes
[**get_topology**](DefaultApi.md#get_topology) | **GET** /topology | Return a topology with lists of node names and link ids
[**get_vnf_flavor**](DefaultApi.md#get_vnf_flavor) | **GET** /vnfflavors/{id} | get detailed information of a vnfflavor. Only available to VM (container do not have flavor)
[**get_vnf_flavors**](DefaultApi.md#get_vnf_flavors) | **GET** /vnfflavors | get a list of vnfflavors
[**get_vnf_instance**](DefaultApi.md#get_vnf_instance) | **GET** /vnfinstances/{id} | get detailed information of a vnf instance
[**get_vnf_instances**](DefaultApi.md#get_vnf_instances) | **GET** /vnfinstances | get a list of vnf instances


# **get_last_measurement**
> MonitoringEntry get_last_measurement(id, measurement_type)

Return the latest value of a measurement of a vnf instance or compute node

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance or compute node
measurement_type = 'measurement_type_example' # str | The measurement metric, which can be get using getMeasurementTypes()

try:
    # Return the latest value of a measurement of a vnf instance or compute node
    api_response = api_instance.get_last_measurement(id, measurement_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_last_measurement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance or compute node | 
 **measurement_type** | **str**| The measurement metric, which can be get using getMeasurementTypes() | 

### Return type

[**MonitoringEntry**](MonitoringEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> Link get_link(id)

get a link

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the link

try:
    # get a link
    api_response = api_instance.get_link(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the link | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_between_nodes**
> Link get_link_between_nodes(node1_id, node2_id)

get detailed information of a link between two specific nodes

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
node1_id = 'node1_id_example' # str | The id of the first node in the link
node2_id = 'node2_id_example' # str | The id of the second node in the link

try:
    # get detailed information of a link between two specific nodes
    api_response = api_instance.get_link_between_nodes(node1_id, node2_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_link_between_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node1_id** | **str**| The id of the first node in the link | 
 **node2_id** | **str**| The id of the second node in the link | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_links**
> list[Link] get_links()

get list of link

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get list of link
    api_response = api_instance.get_links()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_links: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Link]**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement**
> list[MonitoringEntry] get_measurement(id, measurement_type, start_time, end_time)

Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance or compute node
measurement_type = 'measurement_type_example' # str | The measurement metric, which can be get using getMeasurementTypes()
start_time = '2013-10-20T19:20:30+01:00' # datetime | starting time to get the measurement
end_time = '2013-10-20T19:20:30+01:00' # datetime | ending time to get the measurement

try:
    # Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period
    api_response = api_instance.get_measurement(id, measurement_type, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_measurement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance or compute node | 
 **measurement_type** | **str**| The measurement metric, which can be get using getMeasurementTypes() | 
 **start_time** | **datetime**| starting time to get the measurement | 
 **end_time** | **datetime**| ending time to get the measurement | 

### Return type

[**list[MonitoringEntry]**](MonitoringEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement_types**
> list[str] get_measurement_types(id)

get a list of measurements of a vnf instance or a compute node

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance or compute node

try:
    # get a list of measurements of a vnf instance or a compute node
    api_response = api_instance.get_measurement_types(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_measurement_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance or compute node | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> Node get_node(id)

get information of a node

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the node

try:
    # get information of a node
    api_response = api_instance.get_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the node | 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> list[Node] get_nodes()

get a list of nodes

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of nodes
    api_response = api_instance.get_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology**
> Topology get_topology()

Return a topology with lists of node names and link ids

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # Return a topology with lists of node names and link ids
    api_response = api_instance.get_topology()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_topology: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_flavor**
> VNFFlavor get_vnf_flavor(id)

get detailed information of a vnfflavor. Only available to VM (container do not have flavor)

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnfflavor

try:
    # get detailed information of a vnfflavor. Only available to VM (container do not have flavor)
    api_response = api_instance.get_vnf_flavor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_flavor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnfflavor | 

### Return type

[**VNFFlavor**](VNFFlavor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_flavors**
> list[VNFFlavor] get_vnf_flavors()

get a list of vnfflavors

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of vnfflavors
    api_response = api_instance.get_vnf_flavors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_flavors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VNFFlavor]**](VNFFlavor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_instance**
> VNFInstance get_vnf_instance(id)

get detailed information of a vnf instance

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance

try:
    # get detailed information of a vnf instance
    api_response = api_instance.get_vnf_instance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance | 

### Return type

[**VNFInstance**](VNFInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_instances**
> list[VNFInstance] get_vnf_instances()

get a list of vnf instances

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of vnf instances
    api_response = api_instance.get_vnf_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VNFInstance]**](VNFInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

