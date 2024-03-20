def test_equal_lists():
    expected_list = [1, 2, 3, 4, 5]
    result_list = [1, 2, 3, 4]

    assert result_list == expected_list, "The lists aren't equals"
