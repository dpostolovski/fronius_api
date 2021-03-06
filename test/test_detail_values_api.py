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
from swagger_client.api.detail_values_api import DetailValuesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDetailValuesApi(unittest.TestCase):
    """DetailValuesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.detail_values_api.DetailValuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_detail_values_get_detail_values(self):
        """Test case for detail_values_get_detail_values

        Gets a list of values for the given pv system, date range and channel type, whereby the date range is restricted to 24 hours   (some channels are only available with expert package).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
