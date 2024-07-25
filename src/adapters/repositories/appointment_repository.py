from typing import List, Type

from sqlalchemy.future import select
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from src.adapters.database.models.base_model import EntityModel
from src.adapters.protocols.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.appointments_model import AppointmentModel


class AppointmentRepository(SQLAlchemyRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.session_db = session
        self.entity_model = AppointmentModel

    def get_by_doctor_and_status(self, doctor_id: int, status: str) -> List[AppointmentModel]:
        stmt = select(self.entity_model).where(
            and_(
                self.entity_model.doctor_id == doctor_id,
                self.entity_model.status == status
                )
        )
        results = self.session_db.execute(stmt)
        return results

    def search_by_time_window(self, start_time, end_time) -> List[AppointmentModel]:
        stmt = select(self.entity_model).where(
            or_(
                self.entity_model.start_time >= start_time,
                self.entity_model.start_time < end_time,
                self.entity_model.end_time > start_time,
                self.entity_model.end_time <= end_time
            )
        )
        results = self.session_db.execute(stmt)
        return results