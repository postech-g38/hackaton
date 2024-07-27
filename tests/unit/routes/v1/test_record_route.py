import pytest

from tests.fakers.record_faker import FakerRecord


@pytest.mark.usefixtures('database')
def test_get_record_paginate_then_return_no_content(client):
    # arrange
    # act
    response = client.get('/v1/records/paginate')
    # assert
    assert response.status_code == 204


def test_get_record_paginate_then_return_records_pagination(client, database):
    # arrange
    record = FakerRecord()
    database.add(record.model())
    database.commit()
    # act
    response = client.get('/v1/records/paginate')
    # assert
    assert response.status_code == 200


def test_get_record_then_return_record(client, database):
    # arrange
    record = FakerRecord()
    database.add(record.model())
    database.commit()
    # act
    response = client.get('/v1/records/1')
    # assert
    assert response.status_code == 200


@pytest.mark.usefixtures('database')
def test_update_record_then_return_not_found(client):
    # arrange
    record = {
        "client_id": 1,
        "doctor_id": 1,
        "appointment_id": 1,
        "detail": 'something',
        "status": 'something'
    }   
    # act
    response = client.put('/v1/records/1', json=record)
    # assert
    assert response.status_code == 404


def test_update_record_then_return_record(client, database):
    # arrange
    database.add(FakerRecord().model())
    database.commit()
    record = {
      "client_id": 1,
        "doctor_id": 1,
        "appointment_id": 1,
        "detail": 'something',
        "status": 'something'
    }
    # act
    response = client.put('/v1/records/1', json=record)
    # assert
    assert response.status_code == 202
