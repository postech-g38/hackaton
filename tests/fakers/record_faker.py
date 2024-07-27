from datetime import datetime
from dataclasses import dataclass

from src.adapters.database.models.record_model import RecordModel


@dataclass
class FakerRecord(dict):
    id = 1
    created_at = datetime.now()
    updated_at = datetime.now()
    appointment_id = 1
    client_id = 1
    doctor_id = 1
    detail = 'detail'
    status = 'pending'
    
    @staticmethod
    def model() -> RecordModel:
        return RecordModel(
            id=1,
            appointment_id=1,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
            client_id=1,
            doctor_id=1,
            detail='detail',
            status='pending'
        )

    def dict(self) -> dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'client_id': self.client_id,
            'doctor_id': self.doctor_id,
            'detail': self.detail,
            'status': self.status
        }
