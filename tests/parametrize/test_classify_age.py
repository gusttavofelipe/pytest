import pytest
from functions import classify_age


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, "teen"),
        (30, "adult"),
        (60, "senior"),
    ],
)
def test_classify_age(age, expected):
    assert classify_age(age) == expected
