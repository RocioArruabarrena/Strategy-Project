from decimal import Decimal
from src.services.product_service import ProductService
from src.controller.product_controller import ProductController
from src.views.product_view import ProductView
from src.services.strategies.discount_strategy import NoDiscount, PercentageDiscount, FixedDiscount

if __name__ == "__main__":
    service = ProductService("Café Zeppe", Decimal("100.0"))
    view = ProductView()
    controller = ProductController(service, view)

    controller.update_view()

    controller.change_discount(PercentageDiscount(Decimal("20")))
    controller.change_discount(FixedDiscount(Decimal("15")))

