from typing import Protocol


class NotificationProtocol(Protocol):
    ...

def send(self, send_to: str, message) -> bool:
    ...
    