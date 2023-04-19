from.attribute import Attribute
import re

from uc3m_logistics.order_management_exception import OrderManagementException
class EAN13Attribute(Attribute):

    regex_ean13 = re.compile("^[0-9]{13}$")

    def validate(self, value):
        checksum = 0
        code_read = -1
        res = False
        valid_ean13_format = self.regex_ean13.fullmatch(value)
        if valid_ean13_format is None:
            raise OrderManagementException("Invalid EAN13 code string")

        for i, digit in enumerate(reversed(value)):
            try:
                current_digit = int(digit)
            except ValueError as v_e:
                raise OrderManagementException("Invalid EAN13 code string") from v_e
            if i == 0:
                code_read = current_digit
            else:
                checksum += (current_digit) * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read != -1) and (code_read == control_digit):
            res = True
        else:
            raise OrderManagementException("Invalid EAN13 control digit")
        return res
