from src.domain.product import Product
from src.services.strategies.discount_strategy import NoDiscount

class ProductService:
    def __init__(self, name: str, price: float):
        self.product = Product(name, price, NoDiscount())

    def get_product(self):
        return self.product

    def apply_discount(self, strategy):
        self.product.set_discount_strategy(strategy)
        return self.product

