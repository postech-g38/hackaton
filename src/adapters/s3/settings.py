from typing import Dict
from io import BytesIO

import boto3


class Aws:
    def __init__(self, service: str) -> None:
        self._client = boto3.client(service)


class SimpleStorageService(Aws):
    def __init__(self, bucket_name: str) -> None:
        super().__init__('s3')
        self._bucket_name = bucket_name
    
    def create(self) -> Dict[str, str]:
        return self._client.create_bucket(
            Bucket=self._bucket_name,
        )

    def write(self, data: BytesIO, path: str) -> Dict[str, str]:
        return self._client.put_object(
            Bucket=self._bucket_name, 
            Body=data, 
            Key=path
        )

    def search(self, path: str) -> BytesIO:
        data = BytesIO()
        self._client.download_fileobj(
            Bucket=self._bucket_name, 
            Key=path, 
            Fileobj=data
        )
        data.name = path
        data.seek(0)
        return data.getvalue().decode()

    def erase(self, path: str, version: str = None) -> Dict[str, str]:
        return self._client.delete_object(
            Bucket=self._bucket_name,
            Key=path,
            VersionId=version
        )

    def delete(self) -> Dict[str, str]:
        return self._client.delete_bucket(
            Bucket=self._bucket_name
        )