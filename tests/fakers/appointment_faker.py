from datetime import datetime
from dataclasses import dataclass

from src.adapters.database.models.appointments_model import AppointmentModel


@dataclass(init=True)
class FakerAppointment(dict):
    id = 1
    created_at = datetime.now()
    updated_at = datetime.now()
    
    client_id = 1
    doctor_id = 1
    start_time = datetime.now()
    end_time = datetime.now()
    detail = 'detail'
    status = 'confirmed'
    link = 'link'

    def model(self) -> AppointmentModel:
        return AppointmentModel(
            deleted_at=None,
            client_id=self.client_id,
            doctor_id=self.doctor_id,
            start_time=self.start_time,
            end_time=self.end_time,
            detail=self.detail,
            status=self.status,
            link=self.link
        )
    
    def dict(self) -> dict:
        return {
            'deleted_at': None,
            'client_id': self.client_id,
            'doctor_id': self.doctor_id,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'detail': self.detail,
            'status': self.status,
            'link': self.link
        }
