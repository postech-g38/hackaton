from typing import List

from pydantic import BaseModel, ConfigDict


class QuerySchema(BaseModel):
    pass


class PaginateResponseSchema(BaseModel):
    data: List
    total: int
