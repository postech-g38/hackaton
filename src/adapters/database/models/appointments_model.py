from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.adapters.database.models.base_model import EntityModel


class AppointmentModel(EntityModel):
    __tablename__ = 'appointment'
    
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id'))

    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    detail: Mapped[Optional[str]]
    status: Mapped[str]
    link: Mapped[str]
