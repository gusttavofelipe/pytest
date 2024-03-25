import pytest
from functions import access_index


def test_accsess_index_return_success():
    with pytest.raises((IndexError, TypeError)):
        access_index(3)


def test_accsess_index_return_int():
    result = access_index(1)

    assert isinstance(result, int)
