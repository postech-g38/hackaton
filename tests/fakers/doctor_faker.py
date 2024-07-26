from dataclasses import dataclass

from src.adapters.database.models.doctor_model import DoctorModel


@dataclass(init=True)
class FakerDoctor:
    name = 'Sirius'
    crm = '123456'
    speciality = 'Cardiologist'
    appointment_duration = '00:30:00'
    distance = 10.0
    rate = 5.0

    def model(self) -> DoctorModel:
        return DoctorModel(
            name=self.name,
            crm=self.crm,
            speciality=self.speciality,
            appointment_duration=self.appointment_duration,
            distance=self.distance,
            rate=self.rate
        )
