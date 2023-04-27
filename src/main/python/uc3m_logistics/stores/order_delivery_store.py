"""order delivery store module"""
from uc3m_logistics.order_manager_config import Config
from uc3m_logistics.stores.json_store import JsonStore

class OrderDeliveryStore(JsonStore):
    """order delivery store class"""
    _FILE_PATH = Config.ORDER_DELIVERS_STORE_PATH.value

    def find_item_by_key(self, key):
        for item in self.data:
            # pylint: disable=import-outside-toplevel
            from uc3m_logistics.models import OrderDeliveryKeys
            if item[OrderDeliveryKeys.ID.value] == key:
                return item
            return None

    def add_item(self, item):
        self.data.append(item.__dict__)
        self.save()
