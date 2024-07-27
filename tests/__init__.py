
from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import text

from src.adapters.database.models.base_model import BaseModel
from src.adapters.database.settings import sync_engine


class DatabaseHelper:
    def __init__(self, session: Session) -> None:
        self._session = session
    
    def create(self) -> None:
        BaseModel.metadata.create_all(sync_engine)

    def destroy(self) -> None:
        BaseModel.metadata.drop_all(sync_engine)

    def query(self, stmt: str) -> Any:
        return self._session.execute(text(stmt))
    
    def add(self, entity: Any) -> None:
        return self._session.add(entity)
    
    def commit(self) -> None:
        self._session.commit()
        self._session.flush()
