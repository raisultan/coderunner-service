from app.config import celery_app
from app.api_driver import CodeRunnerAPIDriver


@celery_app.task(name='coderunner_run')
def coderunner_run(data: dict) -> None:
    resp = CodeRunnerAPIDriver.run(data)
    return resp
