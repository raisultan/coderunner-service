from fastapi import APIRouter, status

from app import schemas
from app.tasks import coderunner_run

router = APIRouter()


@router.post('/run', status_code=status.HTTP_200_OK)
async def run(data: schemas.CodeRun) -> None:
    coderunner_run.delay(data.dict())
    return
