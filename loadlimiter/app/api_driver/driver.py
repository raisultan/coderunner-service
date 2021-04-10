import logging
from typing import Optional, Union
from json import JSONDecodeError

import httpx

from app import schemas
from app.config import settings

from .logger import coderunner_api_driver_logger_init


class CodeRunnerAPIDriver:
    _api_root_url: str = settings.CODERUNNER_ROOT_URL
    _api_key: str = settings.CODERUNNER_API_KEY

    logger: logging.Logger = coderunner_api_driver_logger_init()

    READ_TIMEOUT: float = 15.0

    class LoggerMsgTemplates:
        REQUEST: str = 'REQUEST: url: {url} headers: {headers} body: {body}'
        RESPONSE: str = (
            'RESPONSE: status_code: {status_code} url: {url} headers: {headers} '
            'body: {body} error: {error}'
        )

    class Route:
        RUN: str = '/run'

    @classmethod
    def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    def run(cls, data: schemas.CodeRun) -> dict:
        url = cls._build_url(cls.Route.RUN)
        headers = {'X-Access-Token': cls._api_key}

        cls._log_request(url, headers, data)

        resp = httpx.post(
            url,
            headers=headers,
            json=data,
            timeout=httpx.Timeout(timeout=cls.READ_TIMEOUT)
        )

        try:
            resp_body = resp.json()
            error = None
        except JSONDecodeError as exc:
            resp_body = None
            error = str(exc)

        cls._log_response(resp.url, resp.status_code, resp.headers, resp_body, error)

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
            body: Union[None, dict, str] = None,
            error: Optional[str] = None,
    ) -> None:
        cls.logger.info(
            msg=cls.LoggerMsgTemplates.RESPONSE.format(
                url=url,
                status_code=status_code,
                headers=headers,
                body=body,
                error=error,
            )
        )
