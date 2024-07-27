from dataclasses import dataclass
from datetime import datetime

from src.adapters.database.models.doctor_model import DoctorModel


@dataclass(init=True)
class FakerDoctor(dict):
    id = 1
    created_at = datetime.now()
    updated_at = datetime.now()
    name = 'Sirius'
    crm = '123456'
    speciality = 'Cardiologist'
    appointment_duration = '00:30:00'
    distance = 10.0
    rate = 5.0

    def model(self) -> DoctorModel:
        return DoctorModel(
            id=1,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
            name=self.name,
            crm=self.crm,
            speciality=self.speciality,
            appointment_duration=self.appointment_duration,
            distance=self.distance,
            rate=self.rate
        )

    def dict(self) -> dict:
        return {
            'id': 1,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'deleted_at': None,
            'name': self.name,
            'crm': self.crm,
            'speciality': self.speciality,
            'appointment_duration': self.appointment_duration,
            'distance': self.distance,
            'rate': self.rate
        }
