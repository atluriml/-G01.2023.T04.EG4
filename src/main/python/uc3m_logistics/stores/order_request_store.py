from uc3m_logistics.models.keys.order_request_keys import OrderRequestKeys
from uc3m_logistics.stores import JsonStore
from freezegun import freeze_time

from uc3m_logistics.order_manager_config import Config


class OrderRequestStore(JsonStore):
    _FILE_PATH =  Config.ORDER_REQUESTS_STORE_PATH.value

    def find_item_by_key(self, key: str):
        found_item: dict or None = None
        for item in self.data:
            if item[OrderRequestKeys.ID.value] == key:
                found_item = item
                break
        if found_item:
            product_id = found_item[OrderRequestKeys.PRODUCT_ID.value]






