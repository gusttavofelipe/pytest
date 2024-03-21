import pytest
from functions import calc_total_price


# o pytest executa o teste usando todas as combinações de valores possiveis,
# executando o teste de acordo com a quantidade de combinações


@pytest.mark.parametrize("price", [10, 50, 10, 34])
@pytest.mark.parametrize("discount_percent", [0, 13, 33])
@pytest.mark.parametrize("tax_percent", [0, 84, 56, 3])
def test_total_price(price, discount_percent, tax_percent):
    expected_price = round(
        price * (1 - discount_percent / 100) * (1 + tax_percent / 100), 2
    )
    assert calc_total_price(price, discount_percent, tax_percent) == expected_price
