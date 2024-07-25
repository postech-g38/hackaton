from typing import List

from sqlalchemy.future import select
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.adapters.protocols.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.client_model import ClientModel


class ClientRepository(SQLAlchemyRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.session_db = session
        self.entity_model = ClientModel
