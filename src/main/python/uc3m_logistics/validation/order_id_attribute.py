from.attribute import Attribute
import re

from uc3m_logistics.order_management_exception import OrderManagementException

class OrderIdAttributes(Attribute):

    order_id_regex = re.compile(r"[0-9a-fA-F]{32}$")

    def validate(self, value):
        res = self.order_id_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("order id is not valid")