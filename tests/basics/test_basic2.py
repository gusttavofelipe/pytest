from functions import length, sum_numbers


def test_sum_numbers_and_lenght():
    assert sum_numbers(3, 2) == 5
    assert length([1, 2, 3]) == 3
