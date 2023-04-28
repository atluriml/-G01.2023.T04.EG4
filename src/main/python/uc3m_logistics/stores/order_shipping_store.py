"""order shipping store module"""
from uc3m_logistics.models.keys.order_shipping_keys import OrderShippingKeys
from uc3m_logistics.order_manager_config import Config
from uc3m_logistics.stores import JsonStore


class OrderShippingStore(JsonStore):
    """Order shipping store class"""
    class __OrderShippingStore:
        _FILE_PATH = Config.ORDER_SHIPMENTS_STORE_PATH.value

        def find_item_by_key(self, key: str):
            """finding item by key"""
            for item in self.data:
                if item[OrderShippingKeys.ID.value] == key:
                    return item
            return None

        def add_item(self, item):
            """adds item to dictionary"""
            self.data.append(item.__dict__)
            self.save()

        _instance = None

        def __new__(cls):
            if not OrderShippingStore._instance:
                OrderShippingStore._instance = OrderShippingStore.__OrderShippingStore()
            return OrderShippingStore._instance

        def __getattr__(self, item):
            return getattr(self._instance, item)

        def __setattr__(self, key, value):
            return setattr(self._instance, key, value)


