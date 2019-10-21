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

from swagger_client.models.battery_info_model import BatteryInfoModel  # noqa: F401,E501
from swagger_client.models.inverter_info_model import InverterInfoModel  # noqa: F401,E501


class DeviceInfoModel(object):
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
        'inverter_info': 'list[InverterInfoModel]',
        'battery_info': 'list[BatteryInfoModel]'
    }

    attribute_map = {
        'inverter_info': 'InverterInfo',
        'battery_info': 'BatteryInfo'
    }

    def __init__(self, inverter_info=None, battery_info=None):  # noqa: E501
        """DeviceInfoModel - a model defined in Swagger"""  # noqa: E501

        self._inverter_info = None
        self._battery_info = None
        self.discriminator = None

        if inverter_info is not None:
            self.inverter_info = inverter_info
        if battery_info is not None:
            self.battery_info = battery_info

    @property
    def inverter_info(self):
        """Gets the inverter_info of this DeviceInfoModel.  # noqa: E501

        List of inverter infos.  # noqa: E501

        :return: The inverter_info of this DeviceInfoModel.  # noqa: E501
        :rtype: list[InverterInfoModel]
        """
        return self._inverter_info

    @inverter_info.setter
    def inverter_info(self, inverter_info):
        """Sets the inverter_info of this DeviceInfoModel.

        List of inverter infos.  # noqa: E501

        :param inverter_info: The inverter_info of this DeviceInfoModel.  # noqa: E501
        :type: list[InverterInfoModel]
        """

        self._inverter_info = inverter_info

    @property
    def battery_info(self):
        """Gets the battery_info of this DeviceInfoModel.  # noqa: E501

        List of battery infos.  # noqa: E501

        :return: The battery_info of this DeviceInfoModel.  # noqa: E501
        :rtype: list[BatteryInfoModel]
        """
        return self._battery_info

    @battery_info.setter
    def battery_info(self, battery_info):
        """Sets the battery_info of this DeviceInfoModel.

        List of battery infos.  # noqa: E501

        :param battery_info: The battery_info of this DeviceInfoModel.  # noqa: E501
        :type: list[BatteryInfoModel]
        """

        self._battery_info = battery_info

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
        if issubclass(DeviceInfoModel, dict):
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
        if not isinstance(other, DeviceInfoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other