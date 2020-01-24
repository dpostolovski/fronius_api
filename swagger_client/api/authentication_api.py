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


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authentication_login(self, body, **kwargs):  # noqa: E501
        """User login to get AccessToken to query API data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginModel body: Login data (username, password, etc.). (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_login_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_login_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_login_with_http_info(self, body, **kwargs):  # noqa: E501
        """User login to get AccessToken to query API data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginModel body: Login data (username, password, etc.). (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'username' in params:
              # noqa: E501
        if 'password' in params:
              # noqa: E501
        if 'api_key' in params:
              # noqa: E501
        if 'device_id' in params:
              # noqa: E501
        if 'device_description' in params:
              # noqa: E501
        if 'app_version' in params:
              # noqa: E501
        if 'os_version' in params:
              # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_login(self, username, password, api_key, device_id, device_description, app_version, os_version, **kwargs):  # noqa: E501
        """User login to get AccessToken to query API data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login(username, password, api_key, device_id, device_description, app_version, os_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :param str password: (required)
        :param str api_key: (required)
        :param str device_id: (required)
        :param str device_description: (required)
        :param str app_version: (required)
        :param str os_version: (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_login_with_http_info(username, password, api_key, device_id, device_description, app_version, os_version, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_login_with_http_info(username, password, api_key, device_id, device_description, app_version, os_version, **kwargs)  # noqa: E501
            return data

    def authentication_login_with_http_info(self, username, password, api_key, device_id, device_description, app_version, os_version, **kwargs):  # noqa: E501
        """User login to get AccessToken to query API data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_login_with_http_info(username, password, api_key, device_id, device_description, app_version, os_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :param str password: (required)
        :param str api_key: (required)
        :param str device_id: (required)
        :param str device_description: (required)
        :param str app_version: (required)
        :param str os_version: (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'password', 'api_key', 'device_id', 'device_description', 'app_version', 'os_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'device_description' is set
        if ('device_description' not in params or
                params['device_description'] is None):
            raise ValueError("Missing the required parameter `device_description` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'app_version' is set
        if ('app_version' not in params or
                params['app_version'] is None):
            raise ValueError("Missing the required parameter `app_version` when calling `authentication_login`")  # noqa: E501
        # verify the required parameter 'os_version' is set
        if ('os_version' not in params or
                params['os_version'] is None):
            raise ValueError("Missing the required parameter `os_version` when calling `authentication_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'username' in params:
              # noqa: E501
        if 'password' in params:
              # noqa: E501
        if 'api_key' in params:
              # noqa: E501
        if 'device_id' in params:
              # noqa: E501
        if 'device_description' in params:
              # noqa: E501
        if 'app_version' in params:
              # noqa: E501
        if 'os_version' in params:
              # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_refresh(self, body, **kwargs):  # noqa: E501
        """Refresh AccessToken, i.e. get a new AccessToken without loging in.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshModel body: Refresh data (current AccessToken, RefreshToken, etc.). (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_refresh_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_refresh_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_refresh_with_http_info(self, body, **kwargs):  # noqa: E501
        """Refresh AccessToken, i.e. get a new AccessToken without loging in.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshModel body: Refresh data (current AccessToken, RefreshToken, etc.). (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_refresh" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_refresh`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
              # noqa: E501
        if 'refresh_token' in params:
              # noqa: E501
        if 'device_id' in params:
              # noqa: E501
        if 'device_description' in params:
              # noqa: E501
        if 'app_version' in params:
              # noqa: E501
        if 'os_version' in params:
              # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_refresh(self, access_token, refresh_token, device_id, device_description, app_version, os_version, **kwargs):  # noqa: E501
        """Refresh AccessToken, i.e. get a new AccessToken without loging in.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh(access_token, refresh_token, device_id, device_description, app_version, os_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: (required)
        :param str refresh_token: (required)
        :param str device_id: (required)
        :param str device_description: (required)
        :param str app_version: (required)
        :param str os_version: (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_refresh_with_http_info(access_token, refresh_token, device_id, device_description, app_version, os_version, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_refresh_with_http_info(access_token, refresh_token, device_id, device_description, app_version, os_version, **kwargs)  # noqa: E501
            return data

    def authentication_refresh_with_http_info(self, access_token, refresh_token, device_id, device_description, app_version, os_version, **kwargs):  # noqa: E501
        """Refresh AccessToken, i.e. get a new AccessToken without loging in.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_refresh_with_http_info(access_token, refresh_token, device_id, device_description, app_version, os_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: (required)
        :param str refresh_token: (required)
        :param str device_id: (required)
        :param str device_description: (required)
        :param str app_version: (required)
        :param str os_version: (required)
        :return: AuthenticationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'refresh_token', 'device_id', 'device_description', 'app_version', 'os_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_refresh" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `authentication_refresh`")  # noqa: E501
        # verify the required parameter 'refresh_token' is set
        if ('refresh_token' not in params or
                params['refresh_token'] is None):
            raise ValueError("Missing the required parameter `refresh_token` when calling `authentication_refresh`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `authentication_refresh`")  # noqa: E501
        # verify the required parameter 'device_description' is set
        if ('device_description' not in params or
                params['device_description'] is None):
            raise ValueError("Missing the required parameter `device_description` when calling `authentication_refresh`")  # noqa: E501
        # verify the required parameter 'app_version' is set
        if ('app_version' not in params or
                params['app_version'] is None):
            raise ValueError("Missing the required parameter `app_version` when calling `authentication_refresh`")  # noqa: E501
        # verify the required parameter 'os_version' is set
        if ('os_version' not in params or
                params['os_version'] is None):
            raise ValueError("Missing the required parameter `os_version` when calling `authentication_refresh`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
              # noqa: E501
        if 'refresh_token' in params:
              # noqa: E501
        if 'device_id' in params:
              # noqa: E501
        if 'device_description' in params:
              # noqa: E501
        if 'app_version' in params:
              # noqa: E501
        if 'os_version' in params:
              # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
