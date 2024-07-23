from typing import Protocol, Type, Dict, Any, Optional


class RepositoryProtocol(Protocol):
    def __init__(self, session) -> None:
        ...
    
    @property
    def _session(self):
        ...

    @property
    def _model(self):
        ...

    def get_all(self) -> tuple[Type, int] | None:
        ...

    def search_by_id(self, model_id: int | str) -> Type | None:
        ...

    def save(self, model) -> Type:
        ...

    def update(self, model_id: int, values: Dict[str, Any]) -> tuple[Any] | None:
        ...

    def delete(self, model_id: Optional[Type]) -> None:
        ...
    
    def refresh(self, model: Type) -> Type:
        ...

    def commit(self) -> None:
        ...
        