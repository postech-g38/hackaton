from sqlalchemy.orm import Mapped

from src.adapters.database.models.base_model import EntityModel


class DoctorModel(EntityModel):
    __tablename__ = 'doctor'
    
    name: Mapped[str]
    crm: Mapped[str]
    speciality: Mapped[str]
    appointment_duration: Mapped[str]
    distance: Mapped[float]
