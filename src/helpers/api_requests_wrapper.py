# Pre built methods for the GET, POST, PATCH, PUT, DELETE Requests

import requests

def get_request(url, auth=None, headers=None, in_json=False):
    response = requests.get(url=url, auth=auth, headers=headers)
    
    if in_json:
        return response, response.json()   # return tuple
    return response




