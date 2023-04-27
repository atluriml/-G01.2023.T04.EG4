from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics import JSON_FILES_PATH
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
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
        #TODO finish this MAKE SURE TESTS MATCH
        if "ContactEmail" not in data:
            raise OrderManagementException("Bad label Contact Email")
        if "OrderID" not in data:
            raise OrderManagementException("Bad label Order ID")

        return cls(data["OrderID"], data["ContactEmail"])

    def save_store(data):
        """Method for saving the orders store"""
        file_store = JSON_FILES_PATH + "orders_store.json"
        # first read the file
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data.order_id:
                found = True
        if found is False:
            data_list.append(data.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return True