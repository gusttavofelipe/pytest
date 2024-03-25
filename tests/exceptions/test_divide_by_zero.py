import pytest
from functions import divide


def test_divide_by_zero_return_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_by_zero_and_message_error():
    with pytest.raises(ZeroDivisionError) as exc:
        divide(10, 0)
    assert "Cannot divide by zero" in str(exc)
