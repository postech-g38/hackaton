from http import HTTPStatus

from fastapi import APIRouter, Depends, Response, Request, Query, Body, Path

from src.schemas.doctor_schema import DoctorSchema, SearchDoctorSchema, DoctorResponseSchema
from src.services.doctor_service import DoctorService
from src.adapters.repositories.doctor_repository import DoctorRepository
from src.adapters.database.settings import database_session



router = APIRouter(prefix='/doctors', tags=['Doctors'])


# @router.get(
#     path='/paginate', 
#     summary='Paginate Doctors',
#     response_model=PaginateResponseSchema
# )
# def paginate(
#     query: QuerySchema = Query(...), 
#     database = Depends(database_session)
# ):
#     service = DoctorService(DoctorRepository(database))
#     data = PaginateResponseSchema.model_validate(service.paginate(query))
#     return Response(
#         status_code=HTTPStatus.OK,
#         content=data.model_dump_json()
#     )


@router.get(
    path='/{doctor_id}', 
    summary='Get Doctor',
    response_model=DoctorResponseSchema
)
def search(
    doctor_id: int = Path(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorResponseSchema.model_validate(service.search(doctor_id))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


@router.post(
    path='/', 
    summary='Create Doctor',
    response_model=DoctorResponseSchema
)
def create(
    payload: DoctorSchema = Body(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorSchema.model_validate(service.create(payload))
    return Response(
        status_code=HTTPStatus.CREATED,
        content=data.model_dump_json()
    )


@router.put(
    path='/{doctor_id}', 
    summary='Update Doctor',
    response_model=DoctorResponseSchema
)
def update(
    doctor_id: int = Path(...), 
    payload: DoctorSchema = Body(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorSchema.model_validate(service.update(doctor_id, payload))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


@router.delete(
    path='/{doctor_id}', 
    summary='Delete Doctor',
    response_model=DoctorResponseSchema
)
def delete(
    doctor_id: int = Path(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorResponseSchema.model_validate(service.delete(doctor_id))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


@router.get(
    path='/search/discover', 
    summary='Search Doctor by Distance(Km), Specialty and Rate',
    response_model=DoctorResponseSchema
)
def search_discover(
    query: SearchDoctorSchema = Query(...),
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorResponseSchema.model_validate(service.search_discover(query.distance, query.specialty, query.rate))
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )
