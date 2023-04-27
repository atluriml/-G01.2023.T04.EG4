import datetime

from uc3m_logistics import JSON_FILES_PATH
from uc3m_logistics.stores import JsonStore


class OrderDeliveryStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "deliver_store.json"

    def find_item_by_key(self, key):
        for item in self.data:
            if item["_OrderShipping__delivery_day"] == key:
                return item
        return None

    def add_item(self, new_item):
        today = datetime.now().date()
