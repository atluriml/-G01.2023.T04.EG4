"""phone number attribute module"""
import re
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.attribute import Attribute


class PhoneNumberAttribute(Attribute):
    """phone number attribute class"""

    phone_num_regex = re.compile(r"^(\+)[0-9]{11}")

    def validate(self, value):
        """validates phone number attribute"""
        res = self.phone_num_regex.fullmatch(value)
        if not res:
            raise OrderManagementException("phone number is not valid")
