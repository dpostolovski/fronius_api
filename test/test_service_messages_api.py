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
from swagger_client.api.service_messages_api import ServiceMessagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestServiceMessagesApi(unittest.TestCase):
    """ServiceMessagesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.service_messages_api.ServiceMessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_service_messages_get_service_messages(self):
        """Test case for service_messages_get_service_messages

        Gets a list of errors and events for a given PV system and date range with texts in given language.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
