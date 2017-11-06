from __future__ import print_function
import time
import stylelens_detect
from stylelens_detect.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_detect.DetectApi()
file = '/Users/bok95/Downloads/test_image.jpg'

try:
    # Query to detect obejects in the image you sent
    api_response = api_instance.detect_objects(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetectApi->detect_objects: %s\n" % e)
