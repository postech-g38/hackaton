from http import HTTPStatus

from fastapi import APIRouter, Depends, Response, Request, Query, Body, Path

from src.schemas.doctor_schema import DoctorSchema, SearchDoctorSchema, DoctorResponseSchema, DoctorPaginateResponseSchema
from src.services.doctor_service import DoctorService
from src.adapters.repositories.doctor_repository import DoctorRepository
from src.adapters.database.settings import database_session
from src.schemas.paginate_schema import QuerySchema

router = APIRouter(prefix='/doctors', tags=['Doctors'])


@router.get(
    path='/paginate', 
    summary='Paginate Doctors',
    response_model=DoctorPaginateResponseSchema
)
def paginate(
    # query: QuerySchema = Query(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    load = service.paginate()
    data = DoctorPaginateResponseSchema.model_validate({
        'data': load, 
        'total': len(load)
    })
    return Response(
        status_code=HTTPStatus.OK,
        content=data.model_dump_json()
    )


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
    data = DoctorResponseSchema.model_validate(service.create(payload))
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
    data = DoctorResponseSchema.model_validate(service.update(doctor_id, payload))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
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
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_dump_json()
    )


@router.get(
    path='/search-discover', 
    summary='Search Doctor by Distance(Km), Specialty and Rate',
    response_model=DoctorResponseSchema
)
def search_discover(
    query: SearchDoctorSchema = Body(...),
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = DoctorResponseSchema.model_validate(service.search_discover(query.distance, query.specialty, query.rate))
    return Response(
        status_code=HTTPStatus.ACCEPTED,
        content=data.model_dump_json()
    )
