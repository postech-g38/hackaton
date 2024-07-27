from typing import List

from src.adapters.protocols.repository_protocol import RepositoryProtocol
from src.adapters.protocols.notification_protocol import NotificationProtocol
from src.domain.entities.appointment_entity import Appointment
from src.domain.entities.doctor_entity import Doctor
from src.domain.ports.payload_port import DoctorSearchPayload
from src.common.date_helper import DateHelper
from src.services.service_base import BaseService, NoConentException
from src.adapters.database.models.appointments_model import AppointmentModel

from src.enums import AppointmentStatus



class AppointmentService(BaseService):

    def __init__(
        self, 
        appointment_repository: RepositoryProtocol, 
        doctor_repository: RepositoryProtocol,
        client_repository: RepositoryProtocol,
        notification: NotificationProtocol
    ) -> None:
        self._appointment_repository = appointment_repository
        self._doctor_repository = doctor_repository
        self._client_repository = client_repository
        self._notification = notification
    
    def paginate(self) -> List[Appointment]:
        if paginate := self._appointment_repository.get_all():
            return paginate
        raise NoConentException('Appointments')

    def search(self, appointment_id: int) -> Appointment:
        return self.query_result(self._appointment_repository.search_by_id(appointment_id))

    def create(self, appointment: Appointment) -> Appointment:
        appointment.link = 'https://meet.google.com/abc-123'
        return self._appointment_repository.save(AppointmentModel(**appointment.dict()))

    def update(self, appointment_id: int, appointment: Appointment) -> Appointment:
        data = self.query_result(self._appointment_repository.search_by_id(appointment_id))
        self._appointment_repository.update(appointment_id, appointment.dict())

        if appointment.status == AppointmentStatus.CONFIRMED.value:
            client = self._client_repository.search_by_id(appointment.client_id)
            self._notification.sms(client.email, 'Your appointment has been confirmed')
        
        return data
    
    def delete(self, appointment_id: int) -> Appointment:
        appointment = self.query_result(self._appointment_repository.search_by_id(appointment_id))
        appointment.deleted_at = DateHelper.now()
        self._appointment_repository.delete(appointment_id)
        return appointment

    def medic_distance(self, search: DoctorSearchPayload) -> List[Doctor]:
        # input: distance_kilometers, specialty
        # list of doctors filtered by specialty and distance
        return self._doctor_repository.search_by_specialty_and_distance(search.specialty, search.distance_kilometers)

    def avaliable_appointments(self, doctor_id: int) -> List[Appointment]:
        # input: doctor_id

        # filter appointments by docttor_id and confirmed
        schedules = self._appointment_repository.get_all()

        schedules = [
            appointment 
            for appointment in schedules 
            if appointment.doctor_id == doctor_id 
            and appointment.status in (AppointmentStatus.CONFIRMED, AppointmentStatus.PENDING_CONFIRMATION)
        ]

        # list of doctor unavaliable times
        return schedules

    def pending(self, doctor_id: int) -> List[Appointment]:
        # filter appointments and not confirmed
        return self._appointment_repository.get_by_doctor_and_status(doctor_id, AppointmentStatus.PENDING_CONFIRMATION)
