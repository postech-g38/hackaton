from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.adapters.database.models.base_model import EntityModel


class ClientModel(EntityModel):
    __tablename__ = 'client'

    email: Mapped[str]
    cpf: Mapped[str]
    password: Mapped[str]
