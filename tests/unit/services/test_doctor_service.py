import pytest
from unittest.mock import Mock

from src.adapters.repositories.doctor_repository import DoctorRepository
from src.services.doctor_service import DoctorService
from tests.fakers.doctor_faker import FakerDoctor


def test_doctor_service_search_then_raise_not_found_exception():
    # arrange
    doctor_id = 1
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = None
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    with pytest.raises(Exception):
        doctor_service.search(doctor_id)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once_with(doctor_id)


def test_doctor_service_search_then_return_doctor_object():
    # arrange
    doctor_id = 1
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = FakerDoctor().model()
    doctor_service = DoctorService(doctor_repository_mock)  

    # act
    result = doctor_service.search(doctor_id)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once_with(doctor_id)
    assert result


def test_doctor_service_create_then_return_doctor_object():
    # arrange
    doctor = Mock()
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.save.return_value = FakerDoctor().model()
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    result = doctor_service.create(doctor)

    # assert
    doctor_repository_mock.save.assert_called_once_with(doctor)
    assert result


def test_doctor_service_update_then_raise_not_found_exception():
    # arrange
    doctor_id = 1
    doctor = Mock(FakerDoctor)
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = None
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    with pytest.raises(Exception):
        doctor_service.update(doctor_id, doctor)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once_with(doctor_id)


def test_doctor_service_update_then_return_doctor_object():
    # arrange
    doctor_id = 1
    doctor = Mock(FakerDoctor)
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = FakerDoctor().model()
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    result = doctor_service.update(doctor_id, doctor)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once_with(doctor_id)
    doctor_repository_mock.update.assert_called_once()
    assert result


def test_doctor_service_delete_then_raise_not_found_exception():
    # arrange
    doctor_id = 1
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = None
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    with pytest.raises(Exception):
        doctor_service.delete(doctor_id)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once_with(doctor_id)


def test_doctor_service_delete_then_return_doctor_object():
    # arrange
    doctor_id = 1
    doctor = Mock(FakerDoctor)
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_by_id.return_value = doctor
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    result = doctor_service.delete(doctor_id)

    # assert
    doctor_repository_mock.search_by_id.assert_called_once()
    doctor_repository_mock.delete.assert_called_once()
    assert result


def test_doctor_service_search_discover_then_return_doctor_list():
    # arrange
    distance_kilometers = 10.0
    specialty = 'Cardiologist'
    rate = 5.0
    doctor_repository_mock = Mock(DoctorRepository)
    doctor_repository_mock.search_discover.return_value = [FakerDoctor().model()]
    doctor_service = DoctorService(doctor_repository_mock)

    # act
    result = doctor_service.search_discover(distance_kilometers, specialty, rate)

    # assert
    doctor_repository_mock.search_discover.assert_called_once()
    assert result