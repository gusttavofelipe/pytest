import pytest
import math

from functions import calc_fatorial, generate_random_number_list


@pytest.mark.parametrize("number", generate_random_number_list(positive=True)[:3])
def test_calc_fatorial_positive(number):
    assert calc_fatorial(number) == math.factorial(number)


@pytest.mark.parametrize("number", generate_random_number_list(positive=False)[:3])
def test_calc_fatorial_negative(number):
    with pytest.raises(ValueError):
        calc_fatorial(number)
