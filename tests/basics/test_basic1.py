from functions import is_positive


def test_is_positive():
    assert is_positive(6) is True
    assert is_positive(-6) is False
