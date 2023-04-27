"""Tracking Code Validation Module"""

import re
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.attribute import Attribute


class TrackingCodeAttribute(Attribute):
    """Tracking Code Validation Class"""

    tracking_code_regex = re.compile(r"[0-9a-fA-F]{64}$")

    def validate(self, value):
        """tracking code validate function"""
        res = self.tracking_code_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("tracking_code format is not valid")
