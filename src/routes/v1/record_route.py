from http import HTTPStatus

from fastapi import APIRouter, Depends, Response, Request, Query, Body, Path

from src.schemas.paginate_schema import QuerySchema, PaginateResponseSchema
from src.schemas.appointment_schema import AppointmentSchema
from src.services.record_service import RecordService
from src.adapters.repositories.record_repository import RecordRepository
from src.schemas.record_schema import RecordSchema, RecordResponseSchema
from src.adapters.database.settings import database_session

router = APIRouter(prefix='/records', tags=['Pedido'])


# @router.get(
#     path='/paginate', 
#     summary='Paginate Records',
#     response_model=PaginateResponseSchema
# )
# def paginate(
#     query: QuerySchema = Query(...),
#     database = Depends(database_session)
# ):
#     service = RecordService(RecordRepository(database))
#     data = PaginateResponseSchema.model_validate(service.paginate(query))
#     return Response(
#         status_code=HTTPStatus.OK,
#         content=data.model_dump_json()
#     )


@router.get(
    path='/{record_id}', 
    summary='Get Record',
    response_model=RecordResponseSchema
)
def search(
    record_id: int = Path(...), 
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.search(record_id))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


@router.post(
    path='/', 
    summary='Create Record',
    response_model=RecordResponseSchema
)
def create(
    payload: AppointmentSchema = Body(...), 
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.create(payload))
    return Response(
        status_code=HTTPStatus.CREATED,
        content=data.model_dump_json()
    )


@router.put(
    path='/{record_id}', 
    summary='Update Appointent',
    response_model=RecordResponseSchema
)
def update(
    record_id: int = Path(...), 
    payload: AppointmentSchema = Body(...), 
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.update(record_id, payload))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_dump_json()
    )


@router.delete(
    path='/{record_id}', 
    summary='Delete Appointment',
    response_model=RecordResponseSchema
)
def delete(
    record_id: int = Path(...), 
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.delete(record_id))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_dump_json()
    )


@router.post(
    path='/{record_id}/doctor/{doctor_id}',
    summary='Add Doctor to Allow List',
    response_model=RecordResponseSchema
)
def allow_doctor_read(
    record_id: int = Path(...), 
    doctor_id: int = Path(...),
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.allow_doctor_read(record_id, doctor_id))
    return Response(
        status_code=201,
        content=data.model_dump_json()
    )


@router.delete(
    path='/{record_id}/doctor/{doctor_id}',
    summary='Remove Doctor from Allow List',
    response_model=RecordResponseSchema
)
def remove_doctor_read(
    record_id: int = Path(...), 
    doctor_id: int = Path(...),
    database = Depends(database_session)
):
    service = RecordService(RecordRepository(database))
    data = RecordResponseSchema.model_validate(service.remove_doctor_read(record_id, doctor_id))
    return Response(
        status_code=201,
        content=data.model_dump_json()
    )
