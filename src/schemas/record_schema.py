from datetime import datetime

from pydantic import BaseModel


class RecordSchema(BaseModel):
    pass


class RecordResponseSchema(RecordSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime