from typing import Any

import httpx

from app import schemas
from app.config import settings


class CodeRunnerAPIDriver:
    _api_root_url: str = settings.CODERUNNER_ROOT_URL

    api_key: str = settings.CODERUNNER_API_KEY
    logger: Any

    class Route:
        RUN: str = '/run'

    @classmethod
    async def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    async def run(cls, data: schemas.CodeRun) -> httpx.Response:
        url = await cls._build_url(cls.Route.RUN)

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                headers={'X-Access-Token': cls.api_key},
                data=data.json(),
            )

        return resp
