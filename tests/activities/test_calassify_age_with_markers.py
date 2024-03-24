import pytest
from functions import classify_age


@pytest.mark.teen
def test_classify_age_teen():
    assert classify_age(15) == "teen"


@pytest.mark.adult
def test_classify_age_adult():
    assert classify_age(25) == "adult"


@pytest.mark.senior
def test_classify_age_senior():
    assert classify_age(65) == "senior"
