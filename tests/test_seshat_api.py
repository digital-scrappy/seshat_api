from seshat_api import get_variable_name


def test_get_variable_name():
    assert get_variable_name("Camel") == "camel"
    assert get_variable_name("ExampleClass") == "example_class"