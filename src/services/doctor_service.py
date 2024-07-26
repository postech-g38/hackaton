from typing import List

from src.adapters.protocols.repository_protocol import RepositoryProtocol
from src.services.service_base import BaseService
from src.common.date_helper import DateHelper
from src.domain.entities.doctor_entity import Doctor


class DoctorService(BaseService):

    def __init__(self, doctor_repository: RepositoryProtocol) -> None:
        self._doctor_repository = doctor_repository
    
    def paginate(self) -> List[Doctor]:
        pass

    def search(self, doctor_id) -> Doctor:
        return self.query_result(self._doctor_repository.search_by_id(doctor_id))
    
    def create(self, doctor) -> Doctor:
        return self._doctor_repository.save(doctor)
    
    def update(self, doctor_id, doctor) -> Doctor:
        doctor = self.query_result(self._doctor_repository.search_by_id(doctor_id))
        return self._doctor_repository.update(doctor_id, doctor)
    
    def delete(self, doctor_id) -> Doctor:
        doctor = self.query_result(self._doctor_repository.search_by_id(doctor_id))
        doctor.deleted_at = DateHelper.now()
        self._doctor_repository.delete(doctor)
        return doctor
    
    def search_discover(self, distance_kilometers: float, specialty: str, rate: float) -> List[Doctor]:
        return self.query_result(self._doctor_repository.search_discover(distance_kilometers, specialty, rate))