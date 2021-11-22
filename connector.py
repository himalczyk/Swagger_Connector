#main stuff happens here, create requests, initialize the object and methods
import requests
import json
from config import password, username, dev_eu_url

class MakeConnection():
    
    def __init__(self, username, password, base_url, ssl_verify=True, timeout=100):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.timeout = timeout
        
    def make_request(self, uri, method, body=None):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        if body:
            body = json.dumps(body)

        response = requests.request(
            url = self.base_url + uri,
            method = method,
            auth=(self.username, self.password),
            headers=headers,
            data=body,
            verify=self.ssl_verify,
            timeout=self.timeout
        )

        if response.status_code >= 300:
            raise Exception(f"{response.status_code}: {response.text}")

        response_data = response.json()
        assert 'token' in response_data

        return response_data
        
    def getToken(self):
        uri = 'api/v1/auth/login'
        method = 'POST'
        body = {  
                "ameliaUrl": dev_eu_url,
                "password": password,
                "username": username
                }
        
        return self.make_request(uri, method, body)