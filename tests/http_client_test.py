import collections
import json
import unittest
from unittest.mock import patch

from requests import Response

from fortnox import HttpClient, Configuration


class HttpClientTest(unittest.TestCase):
    """
    Test cases for HttpClient class
    """

    def setUp(self):
        options = {
            'base_url': 'https://api.fortnox.se',
            'access_token': 'this-is-my-access-token',
            'timeout': 20,
            'client_secret': 'my-test-client-secret'
        }
        self.ClientClass = HttpClient
        self.config = Configuration(**options)

    def test_request_method(self):
        client = self.ClientClass(self.config)
        url = '/accounts'
        with patch('requests.request') as mocked_request:
            data = {
                "MetaInformation": {
                    "@TotalResources": 1210,
                    "@TotalPages": 13,
                    "@CurrentPage": 1
                },
                "Accounts": [
                    {
                        "@url": "https://api.fortnox.se/3/accounts/1010?financialyear=1",
                        "Active": False,
                        "BalanceBroughtForward": 0,
                        "CostCenter": None,
                        "CostCenterSettings": "ALLOWED",
                        "Description": "Utvecklingsutgifter",
                        "Number": 1010,
                        "Project": "",
                        "ProjectSettings": "ALLOWED",
                        "SRU": 7201,
                        "Year": 2,
                        "VATCode": None
                    }
                ]
            }
            _response_client = Response()
            _response_client._content = json.dumps(data).encode('utf-8')
            _response_client.status_code = 200
            _response_client.headers = {"Content-Type": "application/json"}
            mocked_request.return_value = _response_client
            response = client.request('get', url, **{'raw': True})
            self.assertEqual(response[0], 200)
            self.assertEqual(response[1], {"Content-Type": "application/json"})
            self.assertEqual(response[2], data)
