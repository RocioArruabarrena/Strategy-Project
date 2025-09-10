from decimal import Decimal
from strategies import DiscountStrategy


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: Decimal):
        self.amount = amount
    
    def apply_discount(self, price: Decimal) -> Decimal:
        return max(0, price - self.amount)

    def process(self, price: Decimal) -> Decimal:
        return max(0, price - self.amount)
