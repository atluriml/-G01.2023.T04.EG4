"""Global constants for finding the path"""
import os
#path to src folder + "/JsonFiles/"
JSON_FILES_PATH = os.path.join(os.path.dirname(__file__),"../../../JsonFiles/")
#JSON_FILES_PATH = os.path.join(os.path.dirname(__file__),"/JsonFiles/")

JSON_FILES_RF2_PATH = JSON_FILES_PATH + "/FR2InputFiles/"


class Config():
    ORDER_SHIPMENTS_STORE_PATH = JSON_FILES_PATH + "shipments_store.json"