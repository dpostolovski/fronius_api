# coding: utf-8

"""
    ThirdPartyApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AggregatedValuesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aggregated_values_get_month_values(self, pv_system_id, year, month, access_token, **kwargs):  # noqa: E501
        """Gets dayly aggregated values for given pv system, year and month  (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_month_values(pv_system_id, year, month, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param int year: The year to get aggregated days for. (required)
        :param int month: The month to get aggregated days for. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregated_values_get_month_values_with_http_info(pv_system_id, year, month, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregated_values_get_month_values_with_http_info(pv_system_id, year, month, access_token, **kwargs)  # noqa: E501
            return data

    def aggregated_values_get_month_values_with_http_info(self, pv_system_id, year, month, access_token, **kwargs):  # noqa: E501
        """Gets dayly aggregated values for given pv system, year and month  (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_month_values_with_http_info(pv_system_id, year, month, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param int year: The year to get aggregated days for. (required)
        :param int month: The month to get aggregated days for. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pv_system_id', 'year', 'month', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregated_values_get_month_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pv_system_id' is set
        if ('pv_system_id' not in params or
                params['pv_system_id'] is None):
            raise ValueError("Missing the required parameter `pv_system_id` when calling `aggregated_values_get_month_values`")  # noqa: E501
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `aggregated_values_get_month_values`")  # noqa: E501
        # verify the required parameter 'month' is set
        if ('month' not in params or
                params['month'] is None):
            raise ValueError("Missing the required parameter `month` when calling `aggregated_values_get_month_values`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `aggregated_values_get_month_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pv_system_id' in params:
            query_params.append(('pvSystemId', params['pv_system_id']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'month' in params:
            query_params.append(('month', params['month']))  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['AccessToken'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/aggvalues/month', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggValuesModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aggregated_values_get_total_values(self, pv_system_id, access_token, **kwargs):  # noqa: E501
        """Gets yearly aggregated values for given pv system (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_total_values(pv_system_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregated_values_get_total_values_with_http_info(pv_system_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregated_values_get_total_values_with_http_info(pv_system_id, access_token, **kwargs)  # noqa: E501
            return data

    def aggregated_values_get_total_values_with_http_info(self, pv_system_id, access_token, **kwargs):  # noqa: E501
        """Gets yearly aggregated values for given pv system (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_total_values_with_http_info(pv_system_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pv_system_id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregated_values_get_total_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pv_system_id' is set
        if ('pv_system_id' not in params or
                params['pv_system_id'] is None):
            raise ValueError("Missing the required parameter `pv_system_id` when calling `aggregated_values_get_total_values`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `aggregated_values_get_total_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pv_system_id' in params:
            query_params.append(('pvSystemId', params['pv_system_id']))  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['AccessToken'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/aggvalues/total', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggValuesModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aggregated_values_get_year_values(self, pv_system_id, year, access_token, **kwargs):  # noqa: E501
        """Gets monthly aggregated values for given pv system and year  (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_year_values(pv_system_id, year, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param int year: The year to get aggregated months for. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregated_values_get_year_values_with_http_info(pv_system_id, year, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregated_values_get_year_values_with_http_info(pv_system_id, year, access_token, **kwargs)  # noqa: E501
            return data

    def aggregated_values_get_year_values_with_http_info(self, pv_system_id, year, access_token, **kwargs):  # noqa: E501
        """Gets monthly aggregated values for given pv system and year  (only available with expert package).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregated_values_get_year_values_with_http_info(pv_system_id, year, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param int year: The year to get aggregated months for. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :return: AggValuesModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pv_system_id', 'year', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregated_values_get_year_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pv_system_id' is set
        if ('pv_system_id' not in params or
                params['pv_system_id'] is None):
            raise ValueError("Missing the required parameter `pv_system_id` when calling `aggregated_values_get_year_values`")  # noqa: E501
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `aggregated_values_get_year_values`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `aggregated_values_get_year_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pv_system_id' in params:
            query_params.append(('pvSystemId', params['pv_system_id']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['AccessToken'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/aggvalues/year', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggValuesModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)