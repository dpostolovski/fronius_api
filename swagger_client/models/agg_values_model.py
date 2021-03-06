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


class AggValuesModel(object):
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
        'pv_system_id': 'str',
        'interval': 'str',
        'year': 'int',
        'month': 'int',
        'week': 'int',
        'values': 'dict(str, dict(str, float))'
    }

    attribute_map = {
        'pv_system_id': 'PvSystemId',
        'interval': 'Interval',
        'year': 'Year',
        'month': 'Month',
        'week': 'Week',
        'values': 'Values'
    }

    def __init__(self, pv_system_id=None, interval=None, year=None, month=None, week=None, values=None):  # noqa: E501
        """AggValuesModel - a model defined in Swagger"""  # noqa: E501

        self._pv_system_id = None
        self._interval = None
        self._year = None
        self._month = None
        self._week = None
        self._values = None
        self.discriminator = None

        if pv_system_id is not None:
            self.pv_system_id = pv_system_id
        if interval is not None:
            self.interval = interval
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if week is not None:
            self.week = week
        if values is not None:
            self.values = values

    @property
    def pv_system_id(self):
        """Gets the pv_system_id of this AggValuesModel.  # noqa: E501

        PV system ID as Guid.  # noqa: E501

        :return: The pv_system_id of this AggValuesModel.  # noqa: E501
        :rtype: str
        """
        return self._pv_system_id

    @pv_system_id.setter
    def pv_system_id(self, pv_system_id):
        """Sets the pv_system_id of this AggValuesModel.

        PV system ID as Guid.  # noqa: E501

        :param pv_system_id: The pv_system_id of this AggValuesModel.  # noqa: E501
        :type: str
        """

        self._pv_system_id = pv_system_id

    @property
    def interval(self):
        """Gets the interval of this AggValuesModel.  # noqa: E501

        Aggregation interval.  # noqa: E501

        :return: The interval of this AggValuesModel.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this AggValuesModel.

        Aggregation interval.  # noqa: E501

        :param interval: The interval of this AggValuesModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Total", "Year", "Month", "Week", "Day"]  # noqa: E501
        if interval not in allowed_values:
            raise ValueError(
                "Invalid value for `interval` ({0}), must be one of {1}"  # noqa: E501
                .format(interval, allowed_values)
            )

        self._interval = interval

    @property
    def year(self):
        """Gets the year of this AggValuesModel.  # noqa: E501

        Year of data (not used for interval Total).  # noqa: E501

        :return: The year of this AggValuesModel.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this AggValuesModel.

        Year of data (not used for interval Total).  # noqa: E501

        :param year: The year of this AggValuesModel.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def month(self):
        """Gets the month of this AggValuesModel.  # noqa: E501

        Month of data (not used for intervals Total and Year).  # noqa: E501

        :return: The month of this AggValuesModel.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this AggValuesModel.

        Month of data (not used for intervals Total and Year).  # noqa: E501

        :param month: The month of this AggValuesModel.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def week(self):
        """Gets the week of this AggValuesModel.  # noqa: E501

        Week of data (not used for intervals Total, Year and Month).  # noqa: E501

        :return: The week of this AggValuesModel.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this AggValuesModel.

        Week of data (not used for intervals Total, Year and Month).  # noqa: E501

        :param week: The week of this AggValuesModel.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def values(self):
        """Gets the values of this AggValuesModel.  # noqa: E501

        Values per channel.  # noqa: E501

        :return: The values of this AggValuesModel.  # noqa: E501
        :rtype: dict(str, dict(str, float))
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AggValuesModel.

        Values per channel.  # noqa: E501

        :param values: The values of this AggValuesModel.  # noqa: E501
        :type: dict(str, dict(str, float))
        """

        self._values = values

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
        if issubclass(AggValuesModel, dict):
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
        if not isinstance(other, AggValuesModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
