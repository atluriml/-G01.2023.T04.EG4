from src.main.python.uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.validation.email_attribute import EmailAttribute
from uc3m_logistics.validation.order_id_attribute import OrderIdAttributes
import json


class SendProductInput:

    def __init__(self, order_id, email):
        self.__order_id = OrderIdAttributes(order_id).value
        self.__email = EmailAttribute(email).value

    @property
    def order_id(self):
        return self.__order_id

    def email(self):
        return self.__email

    def from_json(cls, file_path):
        try:
            with open(file_path, "r", encoding="utf-8", newline="") as file_path:
                data = json.load(file_path)
        except FileNotFoundError as exception:
            # file is not found
            raise OrderManagementException("File is not found") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
