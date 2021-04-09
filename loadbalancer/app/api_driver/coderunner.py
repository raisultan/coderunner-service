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
    def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    def run(cls, data: schemas.CodeRun) -> httpx.Response:
        url = cls._build_url(cls.Route.RUN)

        resp = httpx.post(
            url,
            headers={'X-Access-Token': cls.api_key},
            json=data,
        )

        return resp
