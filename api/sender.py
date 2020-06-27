import requests
import json

def search_results(results):
    requests.post(static.core_api_url, data=json.dumps(results), headers=static.core_api_response_headers)

from api import static