class InventoryManagementSystem:

    def add_item(self, item_name: str, quantity: int) -> dict:
        if item_name in self:
            self[item_name] += quantity
        else:
            self[item_name] = quantity
        return self

    def update_stock(self, item_name: str, new_quantity: int) -> dict:
        if item_name not in self:
            raise KeyError("Not found")
        self[item_name] = new_quantity
        return self

    def get_item_stock(self, item_name: str) -> int:
        if item_name not in self:
            raise KeyError("Not found")
        return self[item_name]

    def get_available_items(self) -> list:
        result = []
        for item, quantity in self.items():
            if quantity > 0:
                result.append(item)
        return result