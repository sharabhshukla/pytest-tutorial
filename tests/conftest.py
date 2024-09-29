import pytest

from src.school import Location, EducationalInstitute
from src.shapes import Rectangle


@pytest.fixture
def my_int_rectangle():
    return Rectangle(10, 20)

@pytest.fixture
def my_float_rectangle():
    return Rectangle(15.5, 5.5)


@pytest.fixture
def delhi():
    return Location(lat=1.5, long=5.5)


@pytest.fixture
def mumbai():
    return Location(lat=10.50, long=3.25)


@pytest.fixture
def delhi_institute(delhi):
    return EducationalInstitute(location=delhi, total_students=300, total_teachers=50, timetable=True)
