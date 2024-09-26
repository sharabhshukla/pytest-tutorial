import pytest
import src.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("I like", " burgers.")
    assert result == "I like burgers."

def test_add_floats():
    result = my_functions.add(0.1, 0.3)
    assert result == pytest.approx(0.4, rel=0.001)


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(expected_exception=ValueError):
        result = my_functions.divide(10, 0)
