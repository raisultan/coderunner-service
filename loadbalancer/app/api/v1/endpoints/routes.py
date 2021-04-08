from fastapi import APIRouter, status

from app import schemas
from app.api_driver import CodeRunnerAPIDriver

router = APIRouter()


@router.post('/run', status_code=status.HTTP_200_OK)
async def run(data: schemas.CodeRun) -> dict:
    resp = await CodeRunnerAPIDriver.run(data)
    return resp.json()
