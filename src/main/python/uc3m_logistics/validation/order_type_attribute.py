from.attribute import Attribute
import re

from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
class OrderTypeAttribute(Attribute):
    order_type_regex = re.compile(r"(Regular|Premium)")

    def validate(self, value):
        res = self.order_type_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("order_type is not valid")