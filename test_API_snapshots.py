import requests
import json
from snapshottest.file import FileSnapshot
import time
from enum import Enum

#API_BASE_URL = "https://api.consensys.space:8080"
API_BASE_URL = "http://127.0.0.1:8080"
TEST_OBJECT_IDENTIFIER = {'norad_number': 40538}

class RequestMethod(Enum):
    GET = 1
    POST = 2

def api_request(endpoint, expect_json_response, post_data):
    """
    Issues a GET or a POST to an API endpoint, decoding the result and prettifying it if JSON.
    Also prints timing info.

    endpoint - the endpoint to append to API_BASE_URL
    expect_json_response  - True for JSON, false for text
    post_data - If Truthey, a POST is issues with post_data in the body
                If Falsey, a GET is issued and post_data is ignored
    """
    start = time.time()
    if post_data:
      r = requests.post(API_BASE_URL + endpoint, json=post_data)
    else:
      r = requests.get(API_BASE_URL + endpoint)

    end = time.time()
    print(f"{'POST' if post_data else 'GET'} {endpoint} took {end - start} seconds")

    if (expect_json_response):
        output = json.loads(r.content)
        formatted = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))
    else:
        formatted = r.content.decode('utf-8')
    # print(formatted)

    # Munge out date from headers for reproducible tests
    headers = r.headers
    headers['Date'] = 'XXX'

    return f"STATUS: {r.status_code}\n\nHEADERS:{headers}\n\nCONTENT:{formatted}"

def api_post(endpoint, data, expect_json_response=True):
    """
    POSTs a resource to an API endpoint, decoding the response and prettifying it if JSON.
    Also prints timing info.
    """
    return api_request(endpoint, expect_json_response, data)

def api_get(endpoint, is_json):
    """
    GETs a resource from an API endpoint, decoding it and prettifying it if JSON.
    Also prints timing info.
    """
    return api_request(endpoint, is_json, {})

def api_get_json(endpoint):
    """
    GETs JSON from an API endpoint, and prettifies it ready for comparison against a snapshot prettified snapshot
    of a previous test run.
    Also outputs timing info (to see this, run `pytest -s`)
    """
    return api_get(endpoint, True)

def api_get_utf8(endpoint):
    """
    GETs JSON from an API endpoint, and prettifies it ready for comparison against a snapshot prettified snapshot
    of a previous test run.
    Also outputs timing info (to see this, run `pytest -s`)
    """
    return api_get(endpoint, False)

# START GET request section
def test_catalog_priorities(snapshot):
    api_response = api_get_json('/catalog/priorities')
    snapshot.assert_match(api_response)

def test_catalog_undisclosed(snapshot):
    api_response = api_get_json('/catalog/undisclosed')
    snapshot.assert_match(api_response)

def test_catalog_debris(snapshot):
    api_response = api_get_json('/catalog/debris')
    snapshot.assert_match(api_response)

def test_catalog_latest(snapshot):
    api_response = api_get_json('/catalog/latest')
    snapshot.assert_match(api_response)

def test_catalog_all(snapshot):
    api_response = api_get_json('/catalog/all')
    snapshot.assert_match(api_response)

def test_tle_trusat_all(snapshot):
    api_response = api_get_utf8('/tle/trusat_all.txt')
    snapshot.assert_match(api_response)

def test_tle_trusat_priorities(snapshot):
    api_response = api_get_utf8('/tle/trusat_priorities.txt')
    snapshot.assert_match(api_response)

def test_tle_trusat_high_confidence(snapshot):
    api_response = api_get_utf8('/tle/trusat_high_confidence.txt')
    snapshot.assert_match(api_response)

def test_astriagraph(snapshot):
    api_response = api_get_utf8('/astriagraph')
    snapshot.assert_match(api_response)
# END GET request section

# START POST request section
def test_object_influence(snapshot):
    api_response = api_post('/object/influence', TEST_OBJECT_IDENTIFIER)
    snapshot.assert_match(api_response)

def test_object_info(snapshot):
    api_response = api_post('/object/info', TEST_OBJECT_IDENTIFIER)
    snapshot.assert_match(api_response)

def test_tle_object(snapshot):
    api_response = api_post('/tle/object', TEST_OBJECT_IDENTIFIER, expect_json_response=False)
    snapshot.assert_match(api_response)
# END POST request section


