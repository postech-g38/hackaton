from typing import Protocol, Dict
from io import BytesIO


class StorageProtocol(Protocol):
    def __init__(self, bucket_name: str) -> None:
        ...
    
    def create(self) -> Dict[str, str]:
        ...

    def write(self, data: BytesIO, path: str) -> Dict[str, str]:
        ...

    def search(self, path: str) -> BytesIO:
        ...

    def erase(self, path: str, version: str = None) -> Dict[str, str]:
        ...

    def delete(self) -> Dict[str, str]:
        ...

