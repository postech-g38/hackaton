from typing import List


from src.adapters.protocols.repository_protocol import RepositoryProtocol
from src.adapters.protocols.storage_protocol import StorageProtocol
from src.domain.entities.record_entity import Record
from src.common.date_helper import DateHelper
from src.services.service_base import BaseService


class RecordService(BaseService):
    def __init__(self, record_repository: RepositoryProtocol, storage: StorageProtocol) -> None:
        self._record_repository = record_repository
        self._storage = storage

    def paginate(self) -> List[Record]:
        pass

    def get_patient(self, patient_id: str) -> List[Record]:
        pass

    def get_doctor(self, doctor_id: str) -> List[Record]:
        pass

    def search(self, record_id: int) -> Record:
        return self.query_result(self._record_repository.search_by_id(record_id))

    def create(self, record: Record) -> Record:
        return self._record_repository.save(record)

    def update(self, record_id: str, record: Record) -> Record:
        record = self.query_result(self._record_repository.search_by_id(record_id))
        return self._record_repository.update(record_id, record)
    
    def delete(self, record_id: str) -> Record:
        record = self.query_result(self._record_repository.search_by_id(record_id))
        record.deleted_at = DateHelper.now()
        self._record_repository.delete(record)
        return record
    