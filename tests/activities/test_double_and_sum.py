from functions import double_and_sum


def test_double_and_sum(random_number_list):
    result = double_and_sum(random_number_list)

    assert result == sum(x * 2 for x in random_number_list)


def test_double_and_sum_empty_list(random_number_list):
    random_number_list.clear()
    result = double_and_sum(random_number_list)

    assert result == 0
