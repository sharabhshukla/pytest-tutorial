import pytest

from src.school import EducationalInstitute, Location, Semester
from tests.conftest import delhi, delhi_institute


@pytest.mark.parametrize("lat, long", [(1.1, 2.2), (2, 5), (9.5, 10.5), (100.5, 200.67)])
def test_locations(lat, long):
    location = Location(lat=lat, long=long)
    assert location.lat == lat
    assert location.long == long


@pytest.mark.parametrize("no_students, no_teachers, timetable", [(100, 50, True), (300, 180, False), (250, 20, True),
                                                                 (500, 400, True)])
def test_delhi_institute(delhi, no_students, no_teachers, timetable):
    institute = EducationalInstitute(location=delhi, total_students=no_students,
                                     total_teachers=no_teachers, timetable=timetable)
    assert institute.total_teachers == no_teachers


class TestSemester:
    def setup_method(self, delhi_institute):
        self.institute = EducationalInstitute(location=Location(lat=1.0, long=4.5), total_students=200,
                                              total_teachers=300, timetable=False)
        self.semester = Semester(self.institute)

    def test_prepare_timetable(self):
        self.semester.prepare_timetable()
        assert self.institute.timetable is True, "Failed to prepare timetable"

    def test_add_students(self):
        init_total_students = self.institute.total_students
        self.semester.add_students(20)
        assert (
                self.institute.total_students == init_total_students + 20
        ), "Failed to add students"

    def test_add_teachers(self):
        init_total_teachers = self.institute.total_teachers
        self.semester.add_teachers(6)
        assert (
                self.institute.total_teachers == init_total_teachers + 6
        ), "Failed to add teachers"

    def test_add_students_float(self):
        with pytest.raises(TypeError):
            self.semester.add_students(20.5)

    def test_add_teachers_float(self):
        with pytest.raises(TypeError):
            self.semester.add_teachers(6.5)
