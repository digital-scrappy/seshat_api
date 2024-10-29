from seshat_api import get_variable_name, seshat_class_instance
from seshat_api.wf import Camels


def test_get_variable_name():
    assert get_variable_name("Camels") == "camel"
    assert get_variable_name("ExampleClasses") == "example_class"
    assert get_variable_name("BigPonies") == "big_pony"
    assert get_variable_name("AlreadySingular") == "already_singular"
    assert get_variable_name("Judges") == "judge"


# def test_seshat_class_instance():
#     class_instance = seshat_class_instance("Camels", "camel")
#     assert isinstance(class_instance, Camels)