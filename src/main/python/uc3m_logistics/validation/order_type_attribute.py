"""Order Type Module"""
import re
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.attribute import Attribute


class OrderTypeAttribute(Attribute):
    """Order Type Attribute"""
    order_type_regex = re.compile(r"(Regular|Premium)")

    def validate(self, value):
        """validates order type attribute"""
        res = self.order_type_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("order_type is not valid")
