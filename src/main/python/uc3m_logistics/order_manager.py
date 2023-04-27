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
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_tracking_code(t_c):
        """Method for validating sha256 values"""
        tracking_code_regex = re.compile(r"[0-9a-fA-F]{64}$")
        res = tracking_code_regex.fullmatch(t_c)
        if not res:
            raise OrderManagementException("tracking_code format is not valid")


    @staticmethod
    def save_fast(data): # TODO change names to be more descriptive
        """Method for saving the orders store"""
        orders_store = JSON_FILES_PATH + "orders_store.json"
        with open(orders_store, "r+", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
            data_list.append(data.__dict__)
            file.seek(0)
            json.dump(data_list, file, indent=2)

    @staticmethod
    def save_orders_shipped( shipment ):
        """Saves the shipping object into a file"""
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #append the shipments list
        data_list.append(shipment.__dict__)

        try:
            with open(shimpents_store_file, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex


    #pylint: disable=too-many-arguments
    def register_order( self, product_id,
                        order_type,
                        address,
                        phone_number,
                        zip_code ):
        """Register the orders into the order's file"""

        my_order = OrderRequest(product_id,
                                order_type,
                                address,
                                phone_number,
                                zip_code)

        self.save_store(my_order)

        return my_order.order_id

    #pylint: disable=too-many-locals
    def send_product (input_file ):
        """Sends the order included in the input_file"""

        order_shipping = OrderShipping.from_send_input_file(input_file)
        order_shipping.save_to_store()

        return order_shipping.tracking_code

        '''

        # TODO this is what the function should look like
        # order_shipping = OrderShipping.from_send_input_file(input_file)
        # order_shipping.save_to_store()


        #TODO THIS IS THE FIRST PART for this method i jsut commented it out
        #send_product_input = SendProductInput.from_json(input_file)


        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            # file is not found
            raise OrderManagementException("File is not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #check all the information
        try:
            myregex = re.compile(r"[0-9a-fA-F]{32}$")
            res = myregex.fullmatch(data["OrderID"])
            if not res:
                raise OrderManagementException("order id is not valid")
        except KeyError as ex:
            raise  OrderManagementException("Bad label") from ex

        try:
            regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'
            myregex = re.compile(regex_email)
            res = myregex.fullmatch(data["ContactEmail"])
            if not res:
                raise OrderManagementException("contact email is not valid")
        except KeyError as ex:
            raise OrderManagementException("Bad label") from ex
        file_store = JSON_FILES_PATH + "orders_store.json"

        # TODO implement this part still
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data["OrderID"]:
                found = True
                #retrieve the orders data
                proid = item["_OrderRequest__product_id"]
                address = item["_OrderRequest__delivery_address"]
                reg_type = item["_OrderRequest__order_type"]
                phone = item["_OrderRequest__phone_number"]
                order_timestamp = item["_OrderRequest__time_stamp"]
                zip_code = item["_OrderRequest__zip_code"]
                #set the time when the order was registered for checking the md5
                with freeze_time(datetime.fromtimestamp(order_timestamp).date()):
                    order = OrderRequest(product_id=proid,
                                         delivery_address=address,
                                         order_type=reg_type,
                                         phone_number=phone,
                                         zip_code=zip_code)

                if order.order_id != data["OrderID"]:
                    raise OrderManagementException("Orders' data have been manipulated")

        if not found:
            raise OrderManagementException("order_id not found")

        my_sign= OrderShipping(product_id=proid,
                               order_id=data["OrderID"],
                               order_type=reg_type,
                               delivery_email=data["ContactEmail"])

        #save the OrderShipping in shipments_store.json

        self.save_orders_shipped(my_sign)

        return my_sign.tracking_code'''

    def deliver_product( self, tracking_code ):
        """Register the delivery of the product"""

        order_delivery = OrderDelivery.from_order_tracking_code(tracking_code)
        order_delivery.save_to_store()

        return True

        '''
        self.validate_tracking_code(tracking_code)

        # check if this tracking_code is in shipments_store
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
        except FileNotFoundError as exception:
            raise OrderManagementException("shipments_store not found") from exception
        # search this tracking_code
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")

        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"

        try:
            with open(shipments_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as exception:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception

            # append the delivery info
        data_list.append(str(tracking_code))
        data_list.append(str(datetime.utcnow()))
        try:
            with open(shipments_file, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as exception:
            raise OrderManagementException("Wrong file or file path") from exception
        return True'''
