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


class ServiceMessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_messages_get_service_messages(self, pv_system_id, access_token, **kwargs):  # noqa: E501
        """Gets a list of errors and events for a given PV system and date range with texts in given language.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_messages_get_service_messages(pv_system_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :param datetime start_date: Start date, default today (UTC).
        :param datetime end_date: End date, default today (UTC).
        :param str language_code: Two letter ISO language code.
        :return: list[ServiceMessageModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_messages_get_service_messages_with_http_info(pv_system_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.service_messages_get_service_messages_with_http_info(pv_system_id, access_token, **kwargs)  # noqa: E501
            return data

    def service_messages_get_service_messages_with_http_info(self, pv_system_id, access_token, **kwargs):  # noqa: E501
        """Gets a list of errors and events for a given PV system and date range with texts in given language.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_messages_get_service_messages_with_http_info(pv_system_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pv_system_id: PV system ID as Guid. (required)
        :param str access_token: access token obtained from the service method /auth/login (required)
        :param datetime start_date: Start date, default today (UTC).
        :param datetime end_date: End date, default today (UTC).
        :param str language_code: Two letter ISO language code.
        :return: list[ServiceMessageModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pv_system_id', 'access_token', 'start_date', 'end_date', 'language_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_messages_get_service_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pv_system_id' is set
        if ('pv_system_id' not in params or
                params['pv_system_id'] is None):
            raise ValueError("Missing the required parameter `pv_system_id` when calling `service_messages_get_service_messages`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `service_messages_get_service_messages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pv_system_id' in params:
            path_params['pvSystemId'] = params['pv_system_id']  # noqa: E501

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('languageCode', params['language_code']))  # noqa: E501

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
            '/servicemessages/{pvSystemId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceMessageModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
