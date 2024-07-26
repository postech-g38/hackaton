from typing import Optional

from pydantic import BaseModel, field_validator


class SearchDoctorSchema(BaseModel):
    distance: float
    specialty: str
    rate: int = 5.0

    @field_validator("rate")
    def rate_must_be_positive(cls, value: float) -> float:
        if  0 < value <= 5:
            raise ValueError("rate must be betwrren 0 and 5")
        return value
    

class DoctorSchema(BaseModel):
    name: str
    specialty: str
    rate: int


class DoctorResponseSchema(DoctorSchema):
    id: int
    created_at: str
    updated_at: str
    deleted_at: Optional[str]

