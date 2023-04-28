"""order delivery store module"""
from abc import ABC

from uc3m_logistics.order_manager_config import Config
from uc3m_logistics.stores.json_store import JsonStore


class OrderDeliveryStore(JsonStore, ABC):
    """takes control of the singleton pattern"""
    class __OrderDeliveryStore:
        """order delivery store class"""
        _FILE_PATH = Config.ORDER_DELIVERS_STORE_PATH.value

        def __init__(self):
            pass

        def find_item_by_key(self, key):
            """finds the item by the key"""
            for item in self.data:
                # pylint: disable=import-outside-toplevel
                from uc3m_logistics.models import OrderDeliveryKeys
                if item[OrderDeliveryKeys.ID.value] == key:
                    return item
            return None

        def add_item(self, item):
            """adds item to dictionary"""
            self.data.append(item.__dict__)
            self.save()

        _instance = None
        def __new__(cls):
            if not OrderDeliveryStore._instance:
                OrderDeliveryStore._instance = OrderDeliveryStore.__OrderDeliveryStore()
            return OrderDeliveryStore._instance

        def __getattr__(self, item):
            return getattr(self._instance, item)

        def __setattr__(self, key, value):
            return setattr(self._instance, key, value)
