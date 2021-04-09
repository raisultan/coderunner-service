import os
import secrets
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'

    PROJECT_NAME: str = 'loadbalancer'

    CODERUNNER_ROOT_URL: str = 'http://glot:8088'
    CODERUNNER_API_KEY: str = 'token'

    class Celery:
        broker_url: Optional[str] = os.environ.get('BROKER_URL')
        accept_content: list[str] = ['application/json']
        result_serializer: str = 'json'
        task_serializer: str = 'json'
        ignore_result: bool = True

    class Config:
        case_sensitive = True


settings = Settings()
