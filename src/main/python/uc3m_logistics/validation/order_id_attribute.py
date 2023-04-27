"""Order Id Attribute Module"""

import re
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.attribute import Attribute


class OrderIdAttributes(Attribute):
    """order id Attribute class"""

    order_id_regex = re.compile(r"[0-9a-fA-F]{32}$")

    def validate(self, value):
        """validates the order id attribute"""
        res = self.order_id_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("order id is not valid")
