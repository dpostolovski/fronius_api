# coding: utf-8

"""
    ThirdPartyApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.realtime_api import RealtimeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRealtimeApi(unittest.TestCase):
    """RealtimeApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.realtime_api.RealtimeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_realtime_get(self):
        """Test case for realtime_get

        Gets realtime values for given pv system for user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
