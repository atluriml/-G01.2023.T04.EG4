



class OrderShippingStore(JsonStore):
    _FILE_PATH = Config.ORDER_SHIPMENTS_STORE_PATH.value

    def find_item_by_key(self, key: str):
        for item in self.data:
            if item[OrderShippingKeys.ID.value] == key:
                return item
        return None

    def add_item(self, new_item):
        self.data.append(new_item.__dict__)
        self.data = self.data