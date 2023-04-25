from isort.sorting import Config

from uc3m_logistics.models.keys.order_shipping_keys import OrderShippingKeys
from uc3m_logistics.stores import JsonStore


class OrderShippingStore(JsonStore):
    _FILE_PATH = Config.ORDER_SHIPMENTS_STORE_PATH.value

    def find_item_by_key(self, key: str):
        for item in self.data:
            if item[OrderShippingKeys.ID.value] == key:
                return item
        return None

    def add_item(self, new_item):
        self.data.append(new_item.__dict__)
        self.data = self.data