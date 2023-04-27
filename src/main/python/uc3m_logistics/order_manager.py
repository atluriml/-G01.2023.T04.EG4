""" Order Manager Module """
import re
import json
from uc3m_logistics.models.order_request import OrderRequest
from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from uc3m_logistics.models.order_shipping import OrderShipping
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.models.order_delivery import OrderDelivery
from .singleton_metaclass import SingletonMeta

from uc3m_logistics.models.send_product_input import SendProductInput



class OrderManager:



    class __OrderManager:

        # pylint: disable=too-many-arguments
        def register_order(self, product_id,
                           order_type,
                           address,
                           phone_number,
                           zip_code):
            """Register the orders into the order's file"""

            order_request = OrderRequest(product_id,
                                         order_type,
                                         address,
                                         phone_number,
                                         zip_code)

            order_request.save_to_store()

            return order_request.order_id

        # pylint: disable=too-many-locals
        def send_product(input_file):
            """Sends the order included in the input_file"""

            order_shipping = OrderShipping.from_send_input_file(input_file)
            order_shipping.save_to_store()

            return order_shipping.tracking_code

        def deliver_product(self, tracking_code):
            """Register the delivery of the product"""

            order_delivery = OrderDelivery.from_order_tracking_code(tracking_code)
            order_delivery.save_to_store()

            return True

    _instance = None

    def __new__(cls):
        if not OrderManager._instance:
            OrderManager._instance = OrderManager.__OrderManager()
        return OrderManager._instance

    def __getattr__(self, instances):
        return getattr(self.instances_, instances)

    def __setattr__(self, instances, value):
        return setattr(self.instances_, instances, value)

