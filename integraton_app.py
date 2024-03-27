class Product:
    def __init__(self, name, quantity) -> None:
        self.name = name
        self.quantity = quantity


class Stock:
    def __init__(
        self,
    ) -> None:
        self.products = {}

    def add_product(self, product: Product) -> None:
        if product.name not in self.products:
            self.products[product.name] = product.quantity
        else:
            self.products[product.name] += product.quantity

    def view_stock(self, product_name) -> None:
        return self.products.get(product_name, "Product not found")
