from decimal import Decimal

class ProductView:
    @staticmethod
    def display_product(name: str, price: Decimal, final_price: Decimal):
        print(f"Producto: {name}")
        print(f"Precio original: ${price:.2f}")
        print(f"Precio final con descuento: ${final_price:.2f}")
        print("-" * 30)

