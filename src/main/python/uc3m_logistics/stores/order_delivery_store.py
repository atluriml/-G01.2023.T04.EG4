
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.json_store import JsonStore


from freezegun import freeze_time
from datetime import datetime


class OrderDeliveryStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "delivery_store.json"

    def find_item_by_key(self, key):
        for item in self.data:
            from uc3m_logistics.models import OrderDeliveryKeys
            if item[OrderDeliveryKeys.ID.value] == key:
                return item
            return None

    def add_item(self, new_item):
        self.data.append(new_item.__dict__)
        self.save()
