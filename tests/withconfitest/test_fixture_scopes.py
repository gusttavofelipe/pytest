def test_fixture_function(fixture_function):
    assert fixture_function == "function scope"


def test_fixture_function_and_class(fixture_function, fixture_class):
    assert fixture_class == "class scope"
    assert fixture_function == "function scope"


def test_fixture_function_class_and_module(
    fixture_function, fixture_class, fixture_module
):
    assert fixture_function == "function scope"
    assert fixture_class == "class scope"
    assert fixture_module == "module scope"


def test_fixture_function_class_module_and_session(
    fixture_function, fixture_class, fixture_module, fixture_session
):
    assert fixture_function == "function scope"
    assert fixture_class == "class scope"
    assert fixture_module == "module scope"
    assert fixture_session == "session scope"
