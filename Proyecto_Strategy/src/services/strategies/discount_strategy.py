from abc import ABC, abstractmethod
from decimal import Decimal

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: Decimal) -> Decimal:
        pass


        
    