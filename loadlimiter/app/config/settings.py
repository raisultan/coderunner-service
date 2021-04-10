import os
import logging
import secrets
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'
    PROJECT_NAME: str = 'loadlimiter'

    CODERUNNER_ROOT_URL: str = 'http://glot:8088'
    CODERUNNER_API_KEY: str = 'token'

    LOGS_DIR: str = 'logs/'

    class CeleryConf:
        broker_url: Optional[str] = os.environ.get('BROKER_URL')
        accept_content: list[str] = ['application/json']
        result_serializer: str = 'json'
        task_serializer: str = 'json'
        ignore_result: bool = True

    class CeleryLogging:
        FILENAME: str = 'celery.log'
        MAX_BYTES: int = 5 * (1024 * 1024)
        BACKUP_COUNT: int = 10
        FORMATTER: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    class Config:
        case_sensitive = True


settings = Settings()
