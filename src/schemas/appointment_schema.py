from datetime import datetime

from pydantic import BaseModel
from pydantic.types import FutureDatetime

from src.enums import AppointmentStatus


class AppointmentSchema(BaseModel):
    patient_id: str
    doctor_id: str
    record_id: str

    start_time: FutureDatetime
    end_time: FutureDatetime
    detail: str
    status: AppointmentStatus = AppointmentStatus.PENDING_CONFIRMATION
    link: str


class AppointmentResponseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    