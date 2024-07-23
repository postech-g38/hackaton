from enum import Enum


class UserType(str, Enum):
    PACIENT = 'cliente'
    DOCTOR = 'doctor'


class AppointmentStatus(str, Enum):
    PENDING_CONFIRMATION = 'pending_confirmation'

    CONFIRMED = 'confirmed'
    DENIED = 'denied'

    COMPLETED = 'completed'
    NO_SHOW = 'no_show'
