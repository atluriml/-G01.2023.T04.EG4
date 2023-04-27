from datetime import datetime
from freezegun import freeze_time

from uc3m_logistics.exceptions import OrderManagementException
from uc3m_logistics.exceptions.exception_messages import ExceptionMessages
from uc3m_logistics.models.keys.order_request_keys import OrderRequestKeys
from uc3m_logistics.stores import JsonStore

from uc3m_logistics.order_manager_config import Config, JSON_FILES_PATH


class OrderRequestStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "orders_store.json"

    def find_item_by_key(self, key: str):
        found_item: dict or None = None
        for item in self.data:
            if item[OrderRequestKeys.ID.value] == key:
                found_item = item
                break
        if found_item:
            product_id = found_item[OrderRequestKeys.PRODUCT_ID.value]
            order_type = found_item[OrderRequestKeys.ORDER_TYPE.value]
            address = found_item[OrderRequestKeys.DELIVERY_ADDRESS.value]
            phone = found_item[OrderRequestKeys.PHONE_NUMBER.value]
            order_timestamp = found_item[OrderRequestKeys.TIME_STAMP.value]
            zip_code = found_item[OrderRequestKeys.ZIP_CODE.value]

            with freeze_time(datetime.fromtimestamp(order_timestamp).date()): # lazy import
                from uc3m_logistics.models.order_request import OrderRequest
                order = OrderRequest(product_id=product_id,
                                     order_type=order_type,
                                     delivery_address=address,
                                     phone_number=phone,
                                     zip_code=zip_code)
            if order.order_id != found_item[OrderRequestKeys.ID.value]:
                raise OrderManagementException(ExceptionMessages.ORDERS_DATA_MANIPULATED.value)
            return order
        raise OrderManagementException(ExceptionMessages.ORDER_ID_NOT_FOUND.value)

    def add_item(self, item):
        found = False
        for i in self.data:
            if i[OrderRequestKeys.ID.value] == item.order_id:
                found = True
            if not found:
                self.data.append(item.__dict__)
                self.save()
            else:
                raise OrderManagementException(ExceptionMessages.ORDER_ID_ALREADY_EXISTS.value)
