from.attribute import Attribute
import re

from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
class EmailAttribute(Attribute):
    regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'

    def validate(self, value):
        myregex = re.compile(self.regex_email)
        res = myregex.fullmatch(value)
        if not res:
            raise OrderManagementException("contact email is not valid")