"""Email Attribute module"""

import re
from uc3m_logistics.exceptions.exception_messages import ExceptionMessages
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.attribute import Attribute


class EmailAttribute(Attribute):
    """Email Attribute Class"""
    regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'

    def validate(self, value):
        """function validates email attribute"""
        my_regex = re.compile(self.regex_email)
        res = my_regex.fullmatch(value)
        if not res:
            raise OrderManagementException(ExceptionMessages.EMAIL_NOT_VALID.value)
