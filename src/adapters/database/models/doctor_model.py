from sqlalchemy.orm import Mapped

from src.adapters.database.models.base_model import EntityModel


class DoctorModel(EntityModel):
    __tablename__ = 'doctor'
    
    speciality: Mapped[str]
    appointment_duration: Mapped[str]
    distance: Mapped[float]
