from http import HTTPStatus

from fastapi import APIRouter, Depends, Response, Request, Query, Body, Path

from src.schemas.cleint_schema import ClientSchema, ClientResponseSchema
from src.services.doctor_service import DoctorService
from src.adapters.repositories.doctor_repository import DoctorRepository
from src.adapters.database.settings import database_session
from src.schemas.paginate_schema import QuerySchema

router = APIRouter(prefix='/clients', tags=['Clients'])


@router.post(
    path='/', 
    summary='Create Client',
    response_model=ClientResponseSchema
)
def create(
    payload: ClientSchema = Body(...), 
    database = Depends(database_session)
):
    service = DoctorService(DoctorRepository(database))
    data = ClientSchema.model_validate(service.create(payload))
    return Response(
        status_code=HTTPStatus.CREATED,
        content=data.model_dump_json()
    )
