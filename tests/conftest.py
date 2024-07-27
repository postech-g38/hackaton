from typing import Generator, Any

import pytest
from starlette.testclient import TestClient
from sqlalchemy.orm import Session

from src.adapters.database.settings import get_session
from src.app import app
from tests import DatabaseHelper

@pytest.fixture(scope='function')
def client() -> Generator[TestClient, Any, None]:
    with TestClient(app, 'http://localhost:8000') as client:
        yield client


@pytest.fixture(scope='function')
def database() -> Generator[DatabaseHelper, None, None]:
    with get_session() as session:
        db = DatabaseHelper(session)
        db.create()
        yield db
        db.destroy()
