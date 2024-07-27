import pytest

from tests.fakers.appointment_faker import FakerAppointment
from tests.fakers.client_faker import FakerClient


@pytest.mark.usefixtures('database')
def test_get_appointments_paginate_then_return_no_content(client):
    # arrange
    # act
    response = client.get('/v1/appointments/paginate')
    # assert
    assert response.status_code == 204


def test_get_appointments_paginate_then_return_appointments_pagination(client, database):
    # arrange
    appointment = FakerAppointment()
    database.add(appointment.model())
    database.commit()
    # act
    response = client.get('/v1/appointments/paginate')
    # assert
    assert response.status_code == 200


@pytest.mark.usefixtures('database')
def test_create_appointment_then_return_appointment(client):
    # arrange
    appointment = FakerAppointment()
    # act
    response = client.post('/v1/appointments', json=appointment.dict())
    # assert
    assert response.status_code == 201


def test_get_appointments_then_return_not_found(client, database):
    # arrange
    # act
    response = client.get('/api/v1/appointments')
    # assert
    assert response.status_code == 404


def test_get_appointment_then_return_appointment(client, database):
    # arrange
    appointment = FakerAppointment()
    database.add(appointment.model())
    database.commit()
    # act
    response = client.get('/v1/appointments/1')
    # assert
    assert response.status_code == 200


@pytest.mark.usefixtures('database')
def test_update_appointment_then_return_not_found(client):
    # arrange
    appointment = FakerAppointment()
    # act
    response = client.put('/v1/appointments/1', json=appointment.dict())
    # assert
    assert response.status_code == 404


def test_update_appointment_then_return_appointment(client, database):
    # arrange
    appointment = FakerAppointment()
    database.add(appointment.model())
    database.add(FakerClient().model())
    database.commit()
    # act
    response = client.put('/v1/appointments/1', json=appointment.dict())
    # assert
    assert response.status_code == 202


@pytest.mark.usefixtures('database')
def test_delete_appointment_then_return_not_found(client):
    # arrange
    # act
    response = client.delete('/v1/appointments/1')
    # assert
    assert response.status_code == 404


def test_delete_appointment_then_return_appointment(client, database):
    # arrange
    appointment = FakerAppointment()
    database.add(appointment.model())
    database.commit()
    # act
    response = client.delete('/v1/appointments/1')
    # assert
    assert response.status_code == 202
