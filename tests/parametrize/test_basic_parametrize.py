from functions import sum_numbers
import pytest


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 11),
    ]
    # o ultimo argumento representa o ultimo valor das tuplas,
    # sendo o resultado esperado da ultilização dos argumentos anteriores
)
def test_sum(a, b, expected):
    assert sum_numbers(a, b) == expected
