from enum import Enum


class OrderRequestKeys(Enum):
    """Enum representing the keys of the send product input class"""

    ZIP_CODE = "_OrderRequest__zip_code"
    TIME_STAMP = "_OrderRequest__time_stamp"
    PHONE_NUMBER = "_OrderRequest__phone_number"
    DELIVERY_ADDRESS = "_OrderRequest__delivery_address"
    ORDER_TYPE = "_OrderRequest__order_type"
    PRODUCT_ID = "_OrderRequest__product_id"
    ID = "_OrderRequest__order_id"

