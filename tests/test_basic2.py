def sum_numbers(a, b):
    return a + b


def length(list_):
    return len(list_)


def test_sum_numbers_and_lenght():
    assert sum_numbers(3, 2) == 5
    assert length([1, 2, 3]) == 3
