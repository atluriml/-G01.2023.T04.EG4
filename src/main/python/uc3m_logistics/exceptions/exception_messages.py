from enum import Enum

class ExceptionMessages():

    WRONG_FILE_OR_PATH = "wrong provided file or path"
    JSON_DECODE_ERROR = "JSON decoding error"
    ORDERS_DATA_MANIPULATED = "'Orders' data have been manipulated"
    ORDER_ID_ALREADY_EXISTS = "Order_id is already registered in order_stores"

    """ATTRIBUTES"""
    ADDRESS_NOT_VALID = "address is not valid"
    EAN13_NOT_VALID = "Invalid EAN13 code string"
    EAN13_CONTROL_DIGIT_NOT_VALID = " Invalid EAN13 control digit"
    EMAIL_NOT_VALID = "contact email is not valid"
    ORDER_ID_NOT_VALID = "order id is not valid"
    ORDER_ID_NOT_FOUND = "order id was not found"
    ORDER_TYPE_NOT_VALID = "order_type is not valid"
    PHONE_NUMBER_NOT_VALID = "phone number is not valid"
    TRACKING_CODE_NOT_VALID = "tracking code is not valid"
    ZIP_CODE_FORMAT_NOT_VALID = "zip code format is not valid"
    ZIP_CODE_NOT_VALID = "zip code is not valid"
    CONTACT_EMAIL_NOT_PRESENT = "ContactEmail is not present"

    """ORDER DELIVERY"""

    TRACKING_CODE_IS_NOT_FOUND = "tracking_code is not found"
    TODAY_IS_NOT_DELIVERY_DATE = "Today is not the delivery date"
