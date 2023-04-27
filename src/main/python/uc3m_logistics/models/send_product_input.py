"""Send Product Input Module"""
import json
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.validation.email_attribute import EmailAttribute
from uc3m_logistics.validation.order_id_attribute import OrderIdAttributes

class SendProductInput:
    """SendProductInput Class"""
    def __init__(self, order_id, email):
        self.__order_id = OrderIdAttributes(order_id).value
        self.__email = EmailAttribute(email).value

    @property
    def order_id(self):
        """order id function"""
        return self.__order_id

    @property
    def email(self):
        """email function"""
        return self.__email

    @classmethod
    def from_json(cls, file_path):
        """from json method"""
        try:
            with open(file_path, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as exception:
            # file is not found
            raise OrderManagementException("File is not found") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
        if "ContactEmail" not in data:
            raise OrderManagementException("Bad label")
        if "OrderID" not in data:
            raise OrderManagementException("Bad label")

        return cls(data["OrderID"], data["ContactEmail"])
