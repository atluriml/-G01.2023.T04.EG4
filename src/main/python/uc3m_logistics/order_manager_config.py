"""Global constants for finding the path"""
import os
from enum import Enum


# path to src folder + "/JsonFiles/
JSON_FILES_PATH = os.path.join(os.path.dirname(__file__),"../../../JsonFiles/")

JSON_FILES_RF2_PATH = JSON_FILES_PATH + "/FR2InputFiles/"


class Config(Enum):
    ORDER_SHIPMENTS_STORE_PATH = JSON_FILES_PATH + "shipments_store.json"
    ORDER_REQUESTS_STORE_PATH = JSON_FILES_PATH + "order_store.json"
    ORDER_DELIVERS_STORE_PATH = JSON_FILES_PATH + "shipments_delivered.json"
