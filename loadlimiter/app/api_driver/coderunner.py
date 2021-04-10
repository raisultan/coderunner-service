import logging
from typing import Any, Optional

import httpx

from app import schemas
from app.config import settings

from .logger import coderunner_logger_init


class CodeRunnerAPIDriver:
    _api_root_url: str = settings.CODERUNNER_ROOT_URL

    api_key: str = settings.CODERUNNER_API_KEY

    logger: logging.Logger = coderunner_logger_init()

    READ_TIMEOUT: float = 15.0

    class LoggerMsgTemplates:
        REQUEST: str = 'REQUEST: url: {url} headers: {headers} body: {body}'
        RESPONSE: str = (
            'RESPONSE: status_code: {status_code} url: {url} headers: {headers} body: {body}'
        )

    class Route:
        RUN: str = '/run'

    @classmethod
    def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    def run(cls, data: schemas.CodeRun) -> dict:
        url = cls._build_url(cls.Route.RUN)
        headers = {'X-Access-Token': cls.api_key}

        cls._log_request(url, headers, data)

        resp = httpx.post(
            url,
            headers=headers,
            json=data,
            timeout=httpx.Timeout(timeout=cls.READ_TIMEOUT)
        )

        cls._log_response(resp.url, resp.status_code, resp.headers, resp.json())

        return resp.json()

    @classmethod
    def _log_request(cls, url: str, headers: dict[str, str], body: dict) -> None:
        cls.logger.info(
            msg=cls.LoggerMsgTemplates.REQUEST.format(
                url=url,
                headers=headers,
                body=body,
            )
        )

    @classmethod
    def _log_response(
            cls,
            url: Optional[httpx.URL],
            status_code: int,
            headers: dict[str, str],
            body: Optional[dict],
    ) -> None:
        cls.logger.info(
            msg=cls.LoggerMsgTemplates.RESPONSE.format(
                url=url,
                status_code=status_code,
                headers=headers,
                body=body,
            )
        )
