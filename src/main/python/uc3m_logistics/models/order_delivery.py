import datetime

from uc3m_logistics.exceptions import OrderManagementException
from uc3m_logistics.exceptions.exception_messages import ExceptionMessages
from uc3m_logistics.stores import OrderShippingStore
from uc3m_logistics.stores.order_delivery_store import OrderDeliveryStore
from uc3m_logistics.validation import TrackingCodeAttribute


class OrderDelivery:
    
    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCodeAttribute(tracking_code).value
        self.__delivery_date = str(datetime.utcnow())
        
    @property
    def tracking_code(self):
        return self.__tracking_code
    
    @tracking_code.setter
    def tracking_code(self, value):
        self.__tracking_code = TrackingCodeAttribute(value).value
    
    @property
    def delivery_dte(self):
        return self.__delivery_date
    
    def save_to_store(self):
        OrderDeliveryStore().add_item(self)

    @classmethod
    def from_order_tracking_code(cls, tracking_code):
        TrackingCodeAttribute(tracking_code)
        order_shipping = OrderShippingStore().find_item_by_key(tracking_code)
        if not order_shipping:
            raise OrderManagementException(ExceptionMessages.TRACKING_CODE_IS_NOT_FOUND.value)

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(order_shipping["_OrderShipping__delivery_day"]).date()
        if delivery_date != today:
            raise OrderManagementException(ExceptionMessages.TODAY_IS_NOT_DELIVERY_DATE.value)
        return cls(tracking_code)