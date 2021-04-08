import os
import secrets
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'

    PROJECT_NAME: str = 'loadbalancer'

    CELERY_BROKER_URL: Optional[str] = os.environ.get('BROKER_URL')
    CELERY_ACCEPT_CONTENT: list[str] = ['application/json']
    CELERY_RESULT_SERIALIZER: str = 'json'
    CELERY_TASK_SERIALIZER: str = 'json'

    CODERUNNER_ROOT_URL: str = 'http://glot:8088'
    CODERUNNER_API_KEY: str = 'token'

    class Config:
        case_sensitive = True


settings = Settings()
