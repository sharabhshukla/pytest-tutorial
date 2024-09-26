import pytest
import src.shapes as shapes
import math

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(radius=10.0)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_radius(self):
        assert self.circle.radius == pytest.approx(10.0, 0.001)

    def test_area(self):
        assert math.pi * self.circle.radius ** 2 == pytest.approx(self.circle.area(), 0.001)

    def test_perimeter(self):
        assert 2 * math.pi * self.circle.radius == pytest.approx(self.circle.perimeter(), 0.001)