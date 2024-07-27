from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator, ConfigDict
from pydantic.types import FutureDatetime

from src.enums import AppointmentStatus


class AppointmentSchema(BaseModel):
    client_id: int
    doctor_id: int

    start_time: datetime
    end_time: datetime
    
    detail: Optional[str]
    status: AppointmentStatus = AppointmentStatus.PENDING_CONFIRMATION
    link: Optional[str] = None


class AppointmentResponseSchema(AppointmentSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    link: str


class AppointmentPaginateResponseSchema(BaseModel):
    data: List[AppointmentResponseSchema]
    total: int
