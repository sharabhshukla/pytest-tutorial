import pytest

from src.shapes import Square


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (3, 9), (4, 16), (8, 64), (3.0, 9.0)])
def test_multiple_square_area(side_length, expected_area):
    assert Square(side_length).area() == pytest.approx(expected_area, 0.001)


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20), (3.0, 12.0), (1.5, 6.0)])
def test_multple_square_perimeters(side_length, expected_perimeter):
    assert Square(side_length).perimeter() == expected_perimeter
