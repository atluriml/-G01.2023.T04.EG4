"""order delivery keys module"""
from enum import Enum

class OrderDeliveryKeys(Enum):
    """Enum representing the keys of the product input class"""

    ZIP_CODE = "_OrderDelivery__zip_code"
    TIME_STAMP = "_OrderDelivery__time_stamp"
    PHONE_NUMBER = "_OrderDelivery__phone_number"
    DELIVERY_ADDRESS = "_OrderDelivery__delivery_address"
    ORDER_TYPE = "_OrderDelivery__order_type"
    PRODUCT_ID = "_OrderDelivery__product_id"
    ID = "_OrderDelivery__order_id"
