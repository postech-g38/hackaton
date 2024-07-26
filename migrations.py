from src.adapters.database.settings import sync_engine
from src.adapters.database.models.base_model import BaseModel


def migrations() -> None:
    BaseModel.metadata.create_all(sync_engine, checkfirst=True)


if __name__ == "__main__":
    migrations()
