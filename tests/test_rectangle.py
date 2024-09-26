import pytest

def test_area(my_int_rectangle):
    assert my_int_rectangle.length == 10
    assert my_int_rectangle.width == 20
    assert my_int_rectangle.area() == my_int_rectangle.width * my_int_rectangle.length


def test_perimeter(my_int_rectangle):
    assert my_int_rectangle.perimeter() == (10 + 20) * 2

def test_float_area(my_float_rectangle):
    assert my_float_rectangle.length == pytest.approx(15.5, 0.001)
    assert my_float_rectangle.width == pytest.approx(5.5, 0.001)
    assert my_float_rectangle.area() == my_float_rectangle.width * my_float_rectangle.length


def test_float_perimeter(my_float_rectangle):
    assert my_float_rectangle.perimeter() == pytest.approx((15.5 + 5.5) * 2.0, 0.001)