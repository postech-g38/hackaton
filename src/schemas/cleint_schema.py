from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ClientSchema(BaseModel):
    email: str
    cpf: str
    password: str


class ClientResponseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
