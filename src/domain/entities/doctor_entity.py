from datetime import datetime


class Doctor:
    name: str
    specialty: str
    consult_duration: datetime
    rate: float
    distance: float

    def dict(self) -> dict:
        ...
