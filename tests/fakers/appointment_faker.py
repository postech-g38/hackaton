from datetime import datetime
from dataclasses import dataclass

from src.adapters.database.models.appointments_model import AppointmentModel


@dataclass(init=True)
class FakerAppointment:
    id=1
    created_at=datetime.now()
    updated_at=datetime.now()
    client_id=1
    doctor_id=1
    record_id=1
    start_time=datetime.now()
    end_time=datetime.now()
    detail='detail'
    status='pending'
    link='link'

    def model(self) -> AppointmentModel:
        return AppointmentModel(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            client_id=self.client_id,
            doctor_id=self.doctor_id,
            record_id=self.record_id,
            start_time=self.start_time,
            end_time=self.end_time,
            detail=self.detail,
            status=self.status,
            link=self.link
        )
