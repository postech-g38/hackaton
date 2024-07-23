from http import HTTPStatus
import json

from fastapi import APIRouter, Response

router = APIRouter()


@router.get(
    path='/healthcheck', 
    tags=['Health Check'], 
    description='Is API alive ?'
)
def health_check() -> Response:
    payload = {
        'status': 'alive',
        'message': 'hello world'
    }
    return Response(
        status_code=HTTPStatus.OK,
        content=json.dumps(payload)
    )
