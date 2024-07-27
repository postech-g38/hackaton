from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, field_validator, ConfigDict, Field


class SearchDoctorSchema(BaseModel):
    distance: float
    speciality: str
    rate: float = Field(5.0)

    @field_validator("rate")
    def rate_must_be_positive(cls, value: float) -> float:
        if  0.0 < value <= 5.0:
            raise ValueError("rate must be betwrren 0 and 5")
        return value
    

class DoctorSchema(BaseModel):
    name: str
    speciality: str
    rate: float
    distance: float
    crm: str
    appointment_duration: str


class DoctorResponseSchema(DoctorSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class DoctorPaginateResponseSchema(BaseModel):
    data: List[DoctorResponseSchema]
    total: int