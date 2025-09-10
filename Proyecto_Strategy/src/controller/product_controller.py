from src.services.product_service import ProductService
from src.views.product_view import ProductView

class ProductController:
    def __init__(self, service: ProductService, view: ProductView):
        self.service = service
        self.view = view

    def update_view(self):
        product = self.service.get_product()
        final_price = product.get_final_price()
        self.view.display_product(product.name, product.price, final_price)

    def change_discount(self, discount_strategy):
        self.service.apply_discount(discount_strategy)
        self.update_view()

