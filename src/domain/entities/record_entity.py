

class Record:
    appointment_id: str
    patient_id: int
    doctor_id: str

    doctor_note: str
    required_exams: list[str]
    executed_procedurea: list[str]
    medical_prescription: str
    appointment_show_on_certification: str

    def dict(self) -> dict:
        ...
    