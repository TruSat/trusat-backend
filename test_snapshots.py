from collections import defaultdict
import requests
import json
from snapshottest.file import FileSnapshot
import time

#API_BASE_URL = "https://api.consensys.space:8080"
API_BASE_URL = "http://127.0.0.1:8080"

def api_get(endpoint, is_json):
    """
    GETs a resource from an API endpoint, decoding it and pretifying it if JSON.
    Also prints timing info.
    """
    start = time.time()
    r = requests.get(API_BASE_URL + endpoint)
    end = time.time()
    print(f"GET {endpoint} took {end - start} seconds")

    if (is_json):
        output = json.loads(r.content)
        formatted = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))
    else:
        formatted = r.content.decode('utf-8')
    # print(formatted)

    # Munge out date from headers for reproducible tests
    headers = r.headers
    headers['Date'] = 'XXX'

    return f"STATUS: {r.status_code}\n\nHEADERS:{headers}\n\nCONTENT:{formatted}" # TODO: add headers and strip out date header

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

def test_catalog_priorities(snapshot):
    my_api_response = api_get_json('/catalog/priorities')
    snapshot.assert_match(my_api_response)

def test_catalog_undisclosed(snapshot):
    my_api_response = api_get_json('/catalog/undisclosed')
    snapshot.assert_match(my_api_response)

def test_catalog_debris(snapshot):
    my_api_response = api_get_json('/catalog/debris')
    snapshot.assert_match(my_api_response)

def test_catalog_latest(snapshot):
    my_api_response = api_get_json('/catalog/latest')
    snapshot.assert_match(my_api_response)

def test_catalog_all(snapshot):
    my_api_response = api_get_json('/catalog/all')
    snapshot.assert_match(my_api_response)

def test_tle_trusat_all(snapshot):
    my_api_response = api_get_utf8('/tle/trusat_all.txt')
    snapshot.assert_match(my_api_response)

def test_tle_trusat_priorities(snapshot):
    my_api_response = api_get_utf8('/tle/trusat_priorities.txt')
    snapshot.assert_match(my_api_response)

def test_tle_trusat_high_confidence(snapshot):
    my_api_response = api_get_utf8('/tle/trusat_high_confidence.txt')
    snapshot.assert_match(my_api_response)

def test_astriagraph(snapshot):
    my_api_response = api_get_utf8('/astriagraph')
    snapshot.assert_match(my_api_response)