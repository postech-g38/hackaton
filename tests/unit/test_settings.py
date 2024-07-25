from unittest.mock import patch
import os

import pytest

from src.settings import ApplicationSettings, DatabaseSettings, GeneralSettings, LoggingSettings, Env


def test_application_settings():
    # arrange
    application_settings_mock = {
        'APPLICATION_NAME': 'application_name',
        'APPLICATION_HOST': 'application_host',
        'APPLICATION_PORT': '8000',
        'ENVIRONMENT': 'dev',
        'WORKERS': '1',
        'TIMEOUT_GRACEFUL_SHUTDOWN': '5'
    }

    # act
    with patch.dict(os.environ, application_settings_mock):
        application_settings = ApplicationSettings()

    # assert
    assert application_settings.application_name == application_settings_mock['APPLICATION_NAME']
    assert application_settings.application_host == application_settings_mock['APPLICATION_HOST']
    assert application_settings.application_port == int(application_settings_mock['APPLICATION_PORT'])
    assert application_settings.environment == application_settings_mock['ENVIRONMENT']
    assert application_settings.workers == int(application_settings_mock['WORKERS'])
    assert application_settings.timeout_graceful_shutdown == int(application_settings_mock['TIMEOUT_GRACEFUL_SHUTDOWN'])



def test_logging_settings():
    # arrange
    logging_settings_mock = {
        'LOGGING_LEVEL': 'logging_level',
        'LOGGING_FORMAT': 'logging_format',
        'LOGGING_DATETIME_FORMAT': 'logging_datetime_format'
    }

    # act
    with patch.dict(os.environ, logging_settings_mock):
        logging_settings = LoggingSettings()

    # assert
    assert logging_settings.logging_level == logging_settings_mock['LOGGING_LEVEL']
    assert logging_settings.logging_format == logging_settings_mock['LOGGING_FORMAT']
    assert logging_settings.logging_datetime_format == logging_settings_mock['LOGGING_DATETIME_FORMAT']


def test_database_settings():
    # arrange
    database_settings_mock = {
        'DATABASE_USERNAME': 'database_username',
        'DATABASE_PASSWORD': 'database_password',
        'DATABASE_HOST': 'database_host',
        'DATABASE_PORT': '5432',
        'DATABASE_NAME': 'database_name'
    }

    # act
    with patch.dict(os.environ, database_settings_mock):
        database_settings = DatabaseSettings()

    # assert
    assert database_settings.database_username == database_settings_mock['DATABASE_USERNAME']
    assert database_settings.database_password == database_settings_mock['DATABASE_PASSWORD']
    assert database_settings.database_host == database_settings_mock['DATABASE_HOST']
    assert database_settings.database_port == int(database_settings_mock['DATABASE_PORT'])
    assert database_settings.database_name == database_settings_mock['DATABASE_NAME']
