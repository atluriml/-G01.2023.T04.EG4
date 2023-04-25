import json
from src.main.python.uc3m_logistics.order_management_exception import OrderManagementException
from abc import ABC, ABCMeta
from uc3m_logistics.exceptions.exception_messages import ExceptionMessages
from uc3m_logistics.singleton_metaclass import SingletonMeta


class FinalMeta(ABCMeta,SingletonMeta):
    pass
class JsonStore(ABC, metaclass=FinalMeta):
    _FILE_PATH = None

    def __init__(self):
        self.__data = self.load()

    def load(self):
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError:
            # file is not found , so init my data
            data = []
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except json.JSONDecoder as ex:
            raise OrderManagementException(ExceptionMessages.JSON_DECODE_ERROR.value) from ex
        return data