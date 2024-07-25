from typing import Protocol


class NotificationProtocol(Protocol):
    ...

def sms(self, send_to: str, message) -> bool:
    ...
    