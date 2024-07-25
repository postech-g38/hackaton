
from src.adapters.protocols.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.record_model import RecordModel


class RecordRepository(SQLAlchemyRepository):
    def __init__(self, session) -> None:
        super().__init__(session)
        self.entity_model = RecordModel
        