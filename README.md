class CouponBalanceTracker:

    def __init__(self):
        self.coupons = {}

    def add_coupon_points(self, customer_id: str, points: int) -> dict:
        if customer_id in self.coupons:
            self.coupons[customer_id] += points
        else:
            self.coupons[customer_id] = points
        return self.coupons

    def redeem_points(self, customer_id: str, points: int) -> dict:
        if customer_id not in self.coupons or self.coupons[customer_id] < points:
            raise ValueError("Insufficient coupon points")

        self.coupons[customer_id] -= points
        return self.coupons

    def transfer_balance(self, old_customer_id: str, new_customer_id: str) -> dict:
        if old_customer_id not in self.coupons:
            return self.coupons

        old_balance = self.coupons[old_customer_id]

        if new_customer_id in self.coupons:
            self.coupons[new_customer_id] += old_balance
        else:
            self.coupons[new_customer_id] = old_balance

        del self.coupons[old_customer_id]
        return self.coupons

    def active_customers(self) -> list:
        active = []

        for customer_id in self.coupons:
            if self.coupons[customer_id] > 0:
                active.append(customer_id)

        return active
