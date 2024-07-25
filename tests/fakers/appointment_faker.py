from datetime import datetime

from src.adapters.database.models.appointments_model import AppointmentModel

class FakerAppointment:

    @staticmethod
    def model() -> AppointmentModel:
        return AppointmentModel(
            id=1,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            client_id=1,
            doctor_id=1,
            record_id=1,
            start_time=datetime.now(),
            end_time=datetime.now(),
            detail='detail',
            status='pending',
            link='link'
        )
