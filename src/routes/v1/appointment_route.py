from http import HTTPStatus

from fastapi import APIRouter, Depends, Response, Request, Query, Body, Path

from src.schemas.paginate_schema import QuerySchema, PaginateResponseSchema
from src.schemas.appointment_schema import AppointmentSchema, AppointmentResponseSchema
from src.schemas.appointment_schema import AppointmentSchema
from src.services.appointment_service import AppointmentService
from src.adapters.repositories.appointment_repository import AppointmentRepository
from src.adapters.repositories.client_repository import ClientRepository
from src.adapters.repositories.doctor_repository import DoctorRepository
from src.adapters.database.settings import database_session
from src.adapters.sns.settings import SimpleNotificationService

router = APIRouter(prefix='/appointments', tags=['Pedido'])


# @router.get(
#     path='/paginate', 
#     summary='Paginate Appointments',
#     response_model=PaginateResponseSchema
# )
# def paginate(
#     query: QuerySchema = Query(...), 
#     database = Depends(database_session)
# ):
#     service = AppointmentService(AppointmentRepository(database))
#     data = PaginateResponseSchema.model_validate(service.paginate(query))
#     return Response(
#         status_code=HTTPStatus.OK,
#         content=data.model_dump_json()
#     )


@router.get(
    path='/{appointment_id}', 
    summary='Get Appointment',
    response_model=AppointmentResponseSchema
)
def search(
    appointment_id: int = Path(...), 
    database = Depends(database_session)
):
    service = AppointmentService(
        AppointmentRepository(database),
        DoctorRepository(database),
        ClientRepository(database),
        SimpleNotificationService()
        )
    data = AppointmentSchema.model_validate(service.search(appointment_id))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


@router.post(
    path='/', 
    summary='Create Appointment',
    response_model=AppointmentResponseSchema
)
def create(
    payload: AppointmentSchema = Body(...), 
    database = Depends(database_session)
):
    service = AppointmentService(
        AppointmentRepository(database),
        DoctorRepository(database),
        ClientRepository(database),
        SimpleNotificationService()
    )
    data = AppointmentSchema.model_validate(service.create(payload))
    return Response(
        status_code=HTTPStatus.CREATED,
        content=data.model_dump_json()
    )


@router.put(
    path='/{appointment_id}', 
    summary='Update Appointent',
    response_model=AppointmentResponseSchema
)
def update(
    appointment_id: int = Path(...), 
    appointment_data: AppointmentSchema = Body(...), 
    database = Depends(database_session)
):
    service = AppointmentService(
        AppointmentRepository(database),
        DoctorRepository(database),
        ClientRepository(database),
        SimpleNotificationService()
    )
    data = AppointmentSchema.model_validate(service.update(appointment_id, appointment_data))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_dump_json()
    )


@router.delete(
    path='/{appointment_id}', 
    summary='Delete Appointment',
    response_model=AppointmentResponseSchema
)
def delete(
    appointment_id: int = Path(...), 
    database = Depends(database_session)
):
    service = AppointmentService(
        AppointmentRepository(database),
        DoctorRepository(database),
        ClientRepository(database),
        SimpleNotificationService()
    )
    data = AppointmentSchema.model_validate(service.delete(appointment_id))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_validate_json()
    )
