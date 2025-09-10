from decimal import Decimal
from src.services.strategies.discount_strategy import DiscountStrategy

class Product:
    def __init__(self, name: str, price: Decimal, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy
    
    def get_final_price(self) -> Decimal:
        return self.discount_strategy.apply_discount(self.price)
    
    def set_discount_strategy(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy

    