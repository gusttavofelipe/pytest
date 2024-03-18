def is_positive(number):
    return number > 0


def test_is_positive():
    assert is_positive(6) is True
    assert is_positive(-6) is False
