import pytest

from tests.fakers.doctor_faker import FakerDoctor


@pytest.mark.usefixtures('database')
def test_get_doctors_paginate_then_return_no_content(client):
    # arrange
    # act
    response = client.get('/v1/doctors/paginate')
    # assert
    assert response.status_code == 204

def test_get_doctor_paginate_then_return_doctor(client, database):
    # arrange
    doctor = FakerDoctor()
    database.add(doctor.model())
    database.commit()
    # act
    response = client.get('/v1/doctors/1')
    # assert
    assert response.status_code == 200


def test_update_doctor_then_return_not_found(client, database):
    # arrange
    doctor = FakerDoctor()
    # act
    response = client.put('/v1/doctors/1', json=doctor.dict())
    # assert
    assert response.status_code == 404


@pytest.mark.usefixtures('database')
def test_create_doctor_then_return_doctor(client):
    # arrange
    doctor = FakerDoctor()
    # act
    response = client.post('/v1/doctors/', json=doctor.dict())
    # assert
    assert response.status_code == 201


@pytest.mark.usefixtures('database')
def test_delete_doctor_then_return_not_fount(client):
    # arrange
    # act
    response = client.delete('/v1/doctors/1')
    # assert
    assert response.status_code == 404


def test_delete_doctor_then_return_doctor(client, database):
    # arrange
    database.add(FakerDoctor().model())
    database.commit()
    # act
    response = client.delete('/v1/doctors/1')
    # assert
    assert response.status_code == 202
