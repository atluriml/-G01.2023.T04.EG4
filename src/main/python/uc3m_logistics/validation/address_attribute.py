"""Address Attribute Module"""

import re
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from .attribute import Attribute

class AddressAttribute(Attribute):
    """Address Attribute DocString"""
    regex = re.compile(r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$")

    def validate(self, value):
        """Validates address value"""
        res = self.regex.fullmatch(value)
        if not res:
            raise OrderManagementException("address is not valid")
