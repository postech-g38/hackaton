from dataclasses import dataclass
from typing import Any, List, Dict, Type
from http import HTTPStatus
import logging

from fastapi import  HTTPException


_logger = logging.getLogger(__name__)


class NotFoundExcepition(HTTPException):
    def __init__(self, model: str = 'values') -> None:
        super().__init__(HTTPStatus.NOT_FOUND, f"{model} not found")


@dataclass
class BaseService:

    @classmethod
    def cache_miss(cls, result: List[Type | Dict] | Dict[str, Any] | None) -> Any:
        """Log if cache is not found"""
        if result:
            return result
        _logger.info("Cache Miss")

    @classmethod
    def query_result(cls, result: List[Type | Dict] | Dict[str, Any] | None) -> Any:
        """Return the result if exists or raise exception"""
        if result:
            return result
        raise NotFoundExcepition()
        