from unittest.mock import Mock

import pytest

from src.adapters.repositories import AppointmentRepository, DoctorRepository, RecordRepository, ClientRepository
from src.adapters.sns.settings import SimpleNotificationService
from src.services.appointment_service import AppointmentService
from src.services.service_base import NotFoundExcepition, NoConentException
from tests.fakers.appointment_faker import FakerAppointment


def test_appointment_service_search_then_raise_not_found_exception():
    # arrange
    appointment_id = 1
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.search_by_id.return_value = None
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    with pytest.raises(NotFoundExcepition):
        result = appointment_service.search(appointment_id)

    # assert
    assert appointment_repository_mock.search_by_id.called_once_with(appointment_id)


def test_appointment_service_create_then_return_occupied():
    # arrange
    appointment = Mock(FakerAppointment)
    appointment.start_time = FakerAppointment.model().start_time
    appointment.end_time = FakerAppointment.model().end_time
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.save.return_value = FakerAppointment.model()
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    with pytest.raises(NoConentException):
        appointment_service.create(appointment)

    # assert
    assert appointment_repository_mock.save.called_once_with(appointment)


def test_appointment_service_create_then_return_object():
    # arrange
    appointment = Mock(FakerAppointment)
    appointment.start_time = FakerAppointment.model().start_time
    appointment.end_time = FakerAppointment.model().end_time
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.search_by_time_window.return_value = None
    appointment_repository_mock.save.return_value = FakerAppointment.model()
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    result = appointment_service.create(appointment)

    # assert
    assert appointment_repository_mock.save.called_once_with(appointment)
    assert result


def test_appointment_service_update_then_raise_not_found_exception():
    # arrange
    appointment_id = 1
    appointment = Mock()
    appointment.client_id = 1
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.search_by_id.return_value = None
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    with pytest.raises(NotFoundExcepition):
        appointment_service.update(appointment_id, appointment)

    # assert
    assert appointment_repository_mock.update.called_once_with(appointment_id, appointment)
    assert client_repository_mock.search_by_id.called_once_with(appointment.client_id)
    assert notification_mock.sms.called_once()


def test_appointment_service_update_then_object():
    # arrange
    appointment_id = 1
    appointment = Mock()
    appointment.client_id = 1
    appointment_repository_mock = Mock(AppointmentRepository)
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    result = appointment_service.update(appointment_id, appointment)

    # assert
    assert appointment_repository_mock.update.called_once_with(appointment_id, appointment)
    assert client_repository_mock.search_by_id.called_once_with(appointment.client_id)
    assert notification_mock.sms.called_once()
    assert result


def test_appointment_service_delete_then_raise_not_found_exception():
    # arrange
    appointment_id = 1
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.search_by_id.return_value = None
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    with pytest.raises(NotFoundExcepition):
        appointment_service.delete(appointment_id)

    # assert
    assert appointment_repository_mock.search_by_id.called_once_with(appointment_id)


def test_appointment_service_delete_then_object():
    # arrange
    appointment_id = 1
    appointment_repository_mock = Mock(AppointmentRepository)
    appointment_repository_mock.search_by_id.return_value = FakerAppointment.model()
    doctor_repository_mock = Mock(DoctorRepository)
    client_repository_mock = Mock(ClientRepository)
    notification_mock = Mock(SimpleNotificationService)

    appointment_service = AppointmentService(
        appointment_repository_mock, doctor_repository_mock, client_repository_mock, notification_mock
    )

    # act
    result = appointment_service.delete(appointment_id)

    # assert
    assert appointment_repository_mock.search_by_id.called_once_with(appointment_id)
    assert appointment_repository_mock.delete.called_once()
    assert result.deleted_at
