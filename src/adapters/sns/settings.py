from typing import Dict
from io import BytesIO

import boto3


class Aws:
    def __init__(self, service: str) -> None:
        self._client = boto3.client(service)


class SimpleNotificationService(Aws):
    def __init__(self,) -> None:
        super().__init__("sns")

    def sms(self, phone: str, message: str) -> Dict:
        return self._client.publish(
            PhoneNumber=phone, 
            Message=message
        )