from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.adapters.database.models.base_model import EntityModel


class AppointmentModel(EntityModel):
    __tablename__ = 'appointment'
    
    patient_id: Mapped[int] = mapped_column(ForeignKey('patieent.id'))
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id'))
    record_id: Mapped[int] = mapped_column(ForeignKey('record.id'))

    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    detail: Mapped[Optional[str]]
    status: Mapped[str]
    link: Mapped[str]
