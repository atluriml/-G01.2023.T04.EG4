from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.json_store import JsonStore

from freezegun import freeze_time
from datetime import datetime


class OrderDeliveryStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "delivery_store.json"

    def find_item_by_key(self, key):
        for item in self.data:
            if item["_OrderDelivery__order_id"] == key:
                return item
            return None

    def add_item(self, new_item):
        self.data.append(new_item.__dict__)
        self.data = self.data
