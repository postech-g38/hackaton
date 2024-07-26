from typing import List

from sqlalchemy.future import select
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.adapters.protocols.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.doctor_model import DoctorModel


class DoctorRepository(SQLAlchemyRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.session_db = session
        self.entity_model = DoctorModel
    
    def search_discover(self, specialty: str, distance: float) -> List[DoctorModel]:
        stmt = select(self.entity_model).where(
            and_(
                self.entity_model.speciality == specialty, 
                self.entity_model.distance == distance
            )
        )
        results = self.session_db.execute(stmt)
        return results
    
    def search_discover_with_rate(self, specialty: str, distance: float, rate: float) -> List[DoctorModel]:
        stmt = select(self.entity_model).where(
            and_(
                self.entity_model.speciality == specialty, 
                self.entity_model.distance <= distance,
                self.entity_model.rate >= rate
            )
        ).order_by(self.entity_model.distance.asc())
        results = self.session_db.execute(stmt)
        return results
    