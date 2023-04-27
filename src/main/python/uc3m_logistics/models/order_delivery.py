import datetime

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
        pass