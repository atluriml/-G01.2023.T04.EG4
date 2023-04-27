from enum import Enum


class OrderShippingKeys(Enum):
    """Enum representing the keys of the send product input class"""

    ZIP_CODE = "_OrderShipping__zip_code"
    TIME_STAMP = "_OrderShipping__time_stamp"
    PHONE_NUMBER = "_OrderShipping__phone_number"
    DELIVERY_ADDRESS = "_OrderShipping__delivery_address"
    ORDER_TYPE = "_OrderShipping__order_type"
    PRODUCT_ID = "_OrderShipping__product_id"
    ID = "_OrderShipping__order_id"