from datetime import datetime

from src.adapters.database.models.record_model import RecordModel

class FakerRecord:
    
    @staticmethod
    def model() -> RecordModel:
        return RecordModel(
            id=1,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            client_id=1,
            doctor_id=1,
            detail='detail',
            status='pending'
        )
