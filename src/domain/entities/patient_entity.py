

class Patient:
    name: str
    email: str
    document: str

    def dict(self) -> dict:
        ...