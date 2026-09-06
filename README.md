```python
class MobileDataUsageSystem:
    def __init__(self):
        self.data = {}

    def add_customer(self, customer_id, name, plan_name, data_used):
        if customer_id in self.data:
            raise ValueError("Customer already exists")
        
        self.data[customer_id] = {
            "name": name,
            "plan_name": plan_name,
            "data_used": data_used,
            "status": "Active"
        }
        
        return self.data

    def update_data_usage(self, customer_id, new_usage):
        if customer_id not in self.data:
            raise KeyError("Customer not found")
        
        self.data[customer_id]["data_used"] = new_usage
        
        return self.data

    def get_customer_details(self, customer_id):
        if customer_id not in self.data:
            raise KeyError("Customer not found")
        
        return self.data[customer_id]

    def get_high_data_users(self, usage_threshold):
        return [
            cid for cid, info in self.data.items()
            if info["data_used"] >= usage_threshold
        ]
```
