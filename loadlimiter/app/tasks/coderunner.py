import httpx

from app.api_driver import CodeRunnerAPIDriver
from app.config import celery_app


@celery_app.task(name='coderunner_run', bind=True, max_retries=5)
def coderunner_run(self, data: dict) -> None:
    try:
        resp = CodeRunnerAPIDriver.run(data)
    except httpx.ReadTimeout:
        self.retry(countdown=2**self.request.retries)
    else:
        return resp
