from decimal import Decimal
from src.services.strategies.discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: Decimal) -> Decimal:
        return price
