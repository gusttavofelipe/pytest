from functions import email_is_valid, divide


def test_email_is_valid():
    assert email_is_valid("gu@gmail.com") is True
    assert email_is_valid("gu@hotmail") is False
    assert email_is_valid("gu.com") is False
    assert email_is_valid("gu") is False


def test_divde():
    assert divide(1, 2) == 0.5
    assert divide(-1, 2) == -0.5
    assert divide(0, 2) is None
