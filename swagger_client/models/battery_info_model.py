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


class BatteryInfoModel(object):
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
        'serial_number': 'str',
        'capacity': 'float'
    }

    attribute_map = {
        'serial_number': 'SerialNumber',
        'capacity': 'Capacity'
    }

    def __init__(self, serial_number=None, capacity=None):  # noqa: E501
        """BatteryInfoModel - a model defined in Swagger"""  # noqa: E501

        self._serial_number = None
        self._capacity = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if capacity is not None:
            self.capacity = capacity

    @property
    def serial_number(self):
        """Gets the serial_number of this BatteryInfoModel.  # noqa: E501

        Serial number of battery.  # noqa: E501

        :return: The serial_number of this BatteryInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this BatteryInfoModel.

        Serial number of battery.  # noqa: E501

        :param serial_number: The serial_number of this BatteryInfoModel.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def capacity(self):
        """Gets the capacity of this BatteryInfoModel.  # noqa: E501

        Max. capacity of battery.  # noqa: E501

        :return: The capacity of this BatteryInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this BatteryInfoModel.

        Max. capacity of battery.  # noqa: E501

        :param capacity: The capacity of this BatteryInfoModel.  # noqa: E501
        :type: float
        """

        self._capacity = capacity

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
        if issubclass(BatteryInfoModel, dict):
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
        if not isinstance(other, BatteryInfoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other