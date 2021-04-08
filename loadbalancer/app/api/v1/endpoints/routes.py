from fastapi import APIRouter, status

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def hello() -> dict[str, str]:
    return {'detail': 'hello'}
