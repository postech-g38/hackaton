from sqlalchemy.orm import Mapped

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String

from src.adapters.database.models.base_model import EntityModel


class RecordModel(EntityModel):
    __tablename__ = 'record'

    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id'))
    appointment_id: Mapped[int] = mapped_column(ForeignKey('appointment.id'))
    
    detail: Mapped[str]
    status: Mapped[str]
    