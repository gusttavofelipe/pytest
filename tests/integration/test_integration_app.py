from integraton_app import Stock, Product


def test_add_product_and_verify_quantity():
    stock = Stock()

    apple = Product("Apple", 10)
    stock.add_product(apple)

    banana = Product("Banana", 5)
    stock.add_product(banana)

    melon = Product("Melon", 5)
    stock.add_product(melon)

    assert stock.view_stock("Apple") == 10
    assert stock.view_stock("Banana") == 5
    assert stock.view_stock("Melon") == 5


def test_add_existent_product_and_verify_quantity():
    stock = Stock()

    apple = Product("Apple", 10)
    stock.add_product(apple)

    apple = Product("Apple", 5)
    stock.add_product(apple)

    assert stock.view_stock("Apple") == 15
