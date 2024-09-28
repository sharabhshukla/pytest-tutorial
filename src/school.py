from pydantic import BaseModel, Field, conint


class EducationalInstitute(BaseModel):
    total_students: int = conint(ge=1, le=1000000)
    total_teachers: int = conint(ge=1, le=1000000)
    location


class School
