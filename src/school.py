from pydantic import BaseModel, conint


class Location(BaseModel):
    lat: float
    long: float


class EducationalInstitute(BaseModel):
    location: Location
    total_students: conint(ge=1, le=1000000)
    total_teachers: conint(ge=1, le=1000000)
    timetable: bool


class Semester:

    def __init__(self, institute: EducationalInstitute):
        self.institute = institute

    def prepare_timetable(self):
        self.institute.timetable = True

    def add_students(self, no_students: int):
        if not isinstance(no_students, int):
            raise TypeError("no of students can only be integers")
        self.institute.total_students += no_students

    def add_teachers(self, no_teachers: int | float):
        if not isinstance(no_teachers, int):
            raise TypeError("no of teachers can only be an integer")
        self.institute.total_teachers += no_teachers
