from seshat_api import get_variable_name


def test_get_variable_name():
    assert get_variable_name("Camels") == "camel"
    assert get_variable_name("ExampleClasses") == "example_class"
    assert get_variable_name("BigPonies") == "big_pony"
    assert get_variable_name("AlreadySingular") == "already_singular"