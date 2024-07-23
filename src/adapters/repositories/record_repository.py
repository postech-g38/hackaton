
from src.adapters.protocols.sqlalchemy_repository import SQLAlchemyRepository


class RecordRepository(SQLAlchemyRepository):
    def __init__(self, session) -> None:
        super().__init__(session)
        