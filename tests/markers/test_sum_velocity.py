from time import sleep
import pytest
from functions import sum_numbers


@pytest.mark.slow
def test_slow_sum():
    sleep(1)
    assert sum_numbers(1, 1) == 2


@pytest.mark.fast
def test_fast_sum():
    assert sum_numbers(1, 1) == 2


@pytest.mark.fast
@pytest.mark.slow
def test_slow_and_fast_sum():
    sleep(0.5)
    assert sum_numbers(1, 1) == 2
