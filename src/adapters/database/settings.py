import logging
from typing import Generator

from contextlib import contextmanager


from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.engine import create_engine, Engine, URL
from sqlalchemy.orm.session import Session
from sqlalchemy import text

from src.settings import  get_settings, Env

_logger = logging.getLogger(__name__)


def _get_sync_uri() -> URL | str:
    if get_settings().application_settings.execution_environment(Env.UNITTEST):
        return get_settings().database_settings.database_unittest_sync_uri
    return get_settings().database_settings.database_sync_uri


def _create_sync_engine() -> Engine:
    return create_engine(
        url=_get_sync_uri(),
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=True,
    )


sync_engine = _create_sync_engine()

SyncSessionLocal = sessionmaker(
    bind=sync_engine, 
    class_=Session, 
    autoflush=False, 
    autocommit=False, 
    expire_on_commit=False, 
    future=True
    )


@contextmanager
def get_session() -> Generator[Session, None, None]:
    _sync_scoped_session: scoped_session = scoped_session(session_factory=SyncSessionLocal)
    try:
        yield _sync_scoped_session()
        _sync_scoped_session.commit()
    except Exception as ex:
        _sync_scoped_session.rollback()
        raise
    finally:
        _sync_scoped_session.remove()


@contextmanager
def get_connection() -> Generator[Session, None, None]:
    with sync_engine.connect() as connection:
        with connection.begin():
            yield connection


def run_migrations() -> None:
    with get_connection() as conn:
        with open('seeds/seed.sql') as file:
            conn.execute(text(file.read()))


def database_session():
    with get_session() as session:
        yield session
        