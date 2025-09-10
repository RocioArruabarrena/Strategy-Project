from decimal import Decimal
from strategies import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: Decimal):
        self.percent = percent
    
    def apply_discount(self, price: Decimal) -> Decimal:
        return price * (1 - self.percent / 100)

    def process(self, price: Decimal) -> Decimal:
        return price * (1 - self.percent / 100)