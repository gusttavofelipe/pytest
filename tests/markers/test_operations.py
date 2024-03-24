import pytest
import time

from functions import multiply_numbers, sum_numbers


# slow se torna um marcador do teste.
# na excução dos testes passa-se o marcador
# como parametro para executar apenas
# os testes especificos
@pytest.mark.slow
def test_slow_sum():
    time.sleep(2)
    assert sum_numbers(1, 1) == 2


@pytest.mark.normal
def test_sum():
    assert sum_numbers(1, 1) == 2


@pytest.mark.slow
def test_slow_multiply():
    time.sleep(2)
    assert multiply_numbers(1, 1) == 1


@pytest.mark.normal
def test_multiply():
    assert multiply_numbers(1, 1) == 1
