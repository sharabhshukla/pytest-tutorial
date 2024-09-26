import pytest
from src.shapes import Rectangle

@pytest.fixture
def my_int_rectangle():
    return Rectangle(10, 20)

@pytest.fixture
def my_float_rectangle():
    return Rectangle(15.5, 5.5)