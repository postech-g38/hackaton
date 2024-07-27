from functools import lru_cache
from typing import ClassVar
from enum import Enum

from pydantic_settings import BaseSettings
from pydantic import Field
from sqlalchemy.engine import URL


class Env(str, Enum):
    PRD = 'prd'
    STG = 'stg'
    DEV = 'dev'
    UNITTEST = 'unittest'


class ApplicationSettings(BaseSettings):
    application_name: str = Field(..., validation_alias='APPLICATION_NAME')
    application_host: str = Field(..., validation_alias='APPLICATION_HOST')
    application_port: int = Field(..., validation_alias='APPLICATION_PORT')
    environment: Env = Field(..., validation_alias='ENVIRONMENT')
    workers: int = Field(..., validation_alias='WORKERS')
    timeout_graceful_shutdown: int = Field(..., validation_alias='TIMEOUT_GRACEFUL_SHUTDOWN')

    def execution_environment(self, env: Env) -> bool:
        return self.environment == env.value


class LoggingSettings(BaseSettings):
    logging_level: str = Field(..., validation_alias='LOGGING_LEVEL')
    logging_format: str = Field(..., validation_alias='LOGGING_FORMAT')
    logging_datetime_format: str = Field(..., validation_alias='LOGGING_DATETIME_FORMAT')


class DatabaseSettings(BaseSettings):
    database_username: str = Field(..., validation_alias='DATABASE_USERNAME')
    database_password: str = Field(..., validation_alias='DATABASE_PASSWORD')
    database_host: str = Field(..., validation_alias='DATABASE_HOST')
    database_port: int = Field(..., validation_alias='DATABASE_PORT')
    database_name: str = Field(..., validation_alias='DATABASE_NAME')

    @property
    def database_unittest_sync_uri(self) -> str:
        return self.__build_memory_uri('sqlite', 'unittest.db')
    
    @property
    def database_unittest_async_uri(self) -> str:
        return self.__build_memory_uri('aiosqlite', 'unittest.db')

    @property
    def database_sync_uri(self) -> URL:
        return self.__build_uri('postgresql', 'psycopg2')
    
    @property
    def database_async_uri(self) -> URL:
        return self.__build_uri('postgresql', 'asyncpg')

    def __build_memory_uri(self, driver: str, path: str) -> str:
        return f"{driver}:///unittest.db"

    def __build_uri(self, driver: str, dialect: str) -> URL:
        return URL.create(
            drivername=f"{driver}+{dialect}",
            username=self.database_username, 
            password=self.database_password, 
            host=self.database_host, 
            port=self.database_port, 
            database=self.database_name
        )


class AwsSettings(BaseSettings):
    simple_storage_service_bucket_name: str = Field(..., validation_alias='AWS_SIMPLE_STORAGE_SERVICE_BUCKET_NAME')
    simple_notification_service_topic_name: str = Field(..., validation_alias='AWS_SIMPLE_NOTIFICATION_SERVICE_TOPIC_NAME')


class GeneralSettings(BaseSettings):
    application_settings: ClassVar = ApplicationSettings()
    database_settings: ClassVar = DatabaseSettings()
    aws_settings: ClassVar = AwsSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()

