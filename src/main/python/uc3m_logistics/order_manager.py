""" Order Manager Module """
from uc3m_logistics.models.order_request import OrderRequest
from uc3m_logistics.models.order_shipping import OrderShipping
from uc3m_logistics.models.order_delivery import OrderDelivery

class OrderManager:
    """Class for providing the methods for managing the orders process"""

    class __OrderManager:

        @staticmethod
        # pylint: disable=too-many-arguments
        def register_order(product_id,
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
        def send_product(self, input_file):
            """Sends the order included in the input_file"""

            order_shipping = OrderShipping.from_send_input_file(input_file)
            order_shipping.save_to_store()

            return order_shipping.tracking_code

        @staticmethod
        def deliver_product(tracking_code):
            """Register the delivery of the product"""

            order_delivery = OrderDelivery.from_order_tracking_code(tracking_code)
            order_delivery.save_to_store()

            return True

    _instance = None

    def __new__(cls):
        if not OrderManager._instance:
            OrderManager._instance = OrderManager.__OrderManager()
        return OrderManager._instance

    def __getattr__(self, item):
        return getattr(self._instance, item)

    def __setattr__(self, key, value):
        return setattr(self._instance, key, value)



