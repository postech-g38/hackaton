from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class RecordSchema(BaseModel):
    client_id: int
    doctor_id: int
    appointment_id: int
    
    detail: str
    status: str


class RecordResponseSchema(RecordSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class RecordPaginateResponseSchema(BaseModel):
    data: List[RecordResponseSchema]
    total: int
