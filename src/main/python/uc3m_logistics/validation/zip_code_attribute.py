"""Zipcode Attribute Module"""

from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from .attribute import Attribute

class ZipCodeAttribute(Attribute):
    """Zipcode Attribute Class"""

    def validate(self, value):
        """validates zipcode attribute"""
        if value.isnumeric() and len(value) == 5:
            if (int(value) > 52999 or int(value) < 1000):
                raise OrderManagementException("zip_code is not valid")
        else:
            raise OrderManagementException("zip_code format is not valid")
