

from dataclasses import dataclass
from datetime import datetime

from src.adapters.database.models.client_model import ClientModel


@dataclass(init=True)
class FakerClient(dict):
    id = 1
    created_at = datetime.now()
    updated_at = datetime.now()
    email = 'someemail'
    cpf = '12345678910'
    password = 'somepassword'


    def model(self) -> ClientModel:
        return ClientModel(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            email=self.email,
            cpf=self.cpf,
            password=self.password
        )

    def dict(self) -> dict:
        return {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'email': self.email,
            'cpf': self.cpf,
            'password': self.password
        }
