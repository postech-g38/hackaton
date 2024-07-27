from typing import List

from src.adapters.protocols.repository_protocol import RepositoryProtocol
from src.services.service_base import BaseService, NoConentException
from src.adapters.database.models.client_model import ClientModel
from src.common.date_helper import DateHelper
from src.domain.entities.doctor_entity import Doctor


class DoctorService(BaseService):

    def __init__(self, client_repository: RepositoryProtocol) -> None:
        self._client_repository = client_repository


    def create(self, client: Doctor) -> Doctor:
        return self._client_repository.save(ClientModel(**client.dict()))
    