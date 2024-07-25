import pytest
from unittest.mock import Mock

from src.services.record_service import RecordService
from src.adapters.repositories.record_repository import RecordRepository
from src.adapters.s3.settings import SimpleStorageService
from src.services.service_base import NotFoundExcepition
from tests.fakers.record_faker import FakerRecord


def test_record_service_search_then_raise_not_found_exception():
    # arrange
    record_id = 1
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = None
    sorage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, sorage_mock)

    # act
    with pytest.raises(NotFoundExcepition):
        record_service.search(record_id)

    # assert
    record_repository_mock.search_by_id.assert_called_once_with(record_id)


def test_record_service_search_then_return_record_object():
    # arrange
    record_id = 1
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = FakerRecord.model()
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    result = record_service.search(record_id)

    # assert
    record_repository_mock.search_by_id.assert_called_once()
    assert result


def test_record_service_create_then_object():
    # arrange
    record = Mock(FakerRecord)
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = FakerRecord.model()
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    result = record_service.create(record)

    # assert
    record_repository_mock.save.assert_called_once_with(record)
    assert result


def test_record_service_update_then_raise_not_found_exception():
    # arrange
    record_id = 1
    record = Mock(FakerRecord)
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = None
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    with pytest.raises(NotFoundExcepition):
        record_service.update(record_id, record)

    # assert
    record_repository_mock.search_by_id.assert_called_once_with(record_id)


def test_record_service_update_then_object():
    # arrange
    record_id = 1
    record = Mock(FakerRecord)
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = FakerRecord.model()
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    result = record_service.update(record_id, record)

    # assert
    record_repository_mock.search_by_id.assert_called_once()
    record_repository_mock.update.assert_called_once()
    assert result


def test_record_service_delete_then_raise_not_found_exception():
    # arrange
    record_id = 1
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = None
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    with pytest.raises(NotFoundExcepition):
        record_service.delete(record_id)

    # assert
    record_repository_mock.search_by_id.assert_called_once_with(record_id)


def test_record_service_delete_then_object():
    # arrange
    record_id = 1
    record_repository_mock = Mock(RecordRepository)
    record_repository_mock.search_by_id.return_value = FakerRecord.model()
    storage_mock = Mock(SimpleStorageService)

    record_service = RecordService(record_repository_mock, storage_mock)

    # act
    result = record_service.delete(record_id)

    # assert
    record_repository_mock.search_by_id.assert_called_once_with(record_id)
    assert result
