"""Json Store Module"""
import json
from abc import ABC, ABCMeta, abstractmethod
from uc3m_logistics.exceptions.exception_messages import ExceptionMessages
from uc3m_logistics.singleton_metaclass import SingletonMeta
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException


class FinalMeta(ABCMeta, SingletonMeta):
    """Final Meta Class"""


class JsonStore(ABC, metaclass=FinalMeta):
    """JSON Store Class"""
    _FILE_PATH = None

    def __init__(self):
        self.__data = self.load()

    def load(self):
        """load function"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError:
            # file is not found , so init my data
            data = []
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as ex:
            raise OrderManagementException(ExceptionMessages.JSON_DECODE_ERROR.value) from ex
        return data

    def save(self):
        """save function"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self.__data, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException(ExceptionMessages.WRONG_FILE_OR_PATH.value) from ex

    @abstractmethod
    def find_item_by_key(self, key):
        """find item by key function"""

    @abstractmethod
    def add_item(self, item):
        """add item function"""

    @property
    def data(self):
        """data function"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter function"""
        self.__data = value
        self.save()
