from datetime import datetime

from src.enums import AppointmentStatus


class Appointment:
    patient_id: str
    doctor_id: str
    record_id: str

    start_time: datetime
    end_time: datetime
    detail: str
    status: AppointmentStatus
    link: str
    
    def dict(self) -> dict:
        ...