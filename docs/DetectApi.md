# stylelens_detect.DetectApi

All URIs are relative to *http://objdetect.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detect_objects**](DetectApi.md#detect_objects) | **POST** / | Query to detect obejects in the image you sent


# **detect_objects**
> DetectObjectsResponse detect_objects(file=file)

Query to detect obejects in the image you sent

Image file that needs to be detected objects

### Example 
```python
from __future__ import print_function
import time
import stylelens_detect
from stylelens_detect.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_detect.DetectApi()
file = '/path/to/file.txt' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to detect obejects in the image you sent
    api_response = api_instance.detect_objects(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetectApi->detect_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**DetectObjectsResponse**](DetectObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

