# coding: utf-8

"""
    ThirdPartyApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AddressModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'country': 'str',
        'zip_code': 'str',
        'street': 'str',
        'city': 'str',
        'state': 'str'
    }

    attribute_map = {
        'country': 'Country',
        'zip_code': 'ZipCode',
        'street': 'Street',
        'city': 'City',
        'state': 'State'
    }

    def __init__(self, country=None, zip_code=None, street=None, city=None, state=None):  # noqa: E501
        """AddressModel - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._zip_code = None
        self._street = None
        self._city = None
        self._state = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if zip_code is not None:
            self.zip_code = zip_code
        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state

    @property
    def country(self):
        """Gets the country of this AddressModel.  # noqa: E501

        Two letter ISO country code.  # noqa: E501

        :return: The country of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressModel.

        Two letter ISO country code.  # noqa: E501

        :param country: The country of this AddressModel.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def zip_code(self):
        """Gets the zip_code of this AddressModel.  # noqa: E501

        Zip code.  # noqa: E501

        :return: The zip_code of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this AddressModel.

        Zip code.  # noqa: E501

        :param zip_code: The zip_code of this AddressModel.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def street(self):
        """Gets the street of this AddressModel.  # noqa: E501

        Street.  # noqa: E501

        :return: The street of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this AddressModel.

        Street.  # noqa: E501

        :param street: The street of this AddressModel.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this AddressModel.  # noqa: E501

        City.  # noqa: E501

        :return: The city of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressModel.

        City.  # noqa: E501

        :param city: The city of this AddressModel.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this AddressModel.  # noqa: E501

        State.  # noqa: E501

        :return: The state of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AddressModel.

        State.  # noqa: E501

        :param state: The state of this AddressModel.  # noqa: E501
        :type: str
        """

        self._state = state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AddressModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddressModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
