import os
import logging
from logging.handlers import RotatingFileHandler
from celery import Celery
from celery.signals import after_setup_logger

from .settings import settings

logger = logging.getLogger(__name__)

celery_app = Celery('celery_app')
celery_app.config_from_object(settings.CeleryConf)
celery_app.autodiscover_tasks(packages=['app.tasks'])


@after_setup_logger.connect
def setup_loggers(logger: logging.Logger, *_, **__) -> None:
    if not os.path.exists(settings.LOGS_DIR):
        os.makedirs(settings.LOGS_DIR)

    rfh = RotatingFileHandler(
        filename=f'{settings.LOGS_DIR}{settings.CeleryLogger.FILENAME}',
        maxBytes=settings.CeleryLogger.MAX_BYTES,
        backupCount=settings.CeleryLogger.BACKUP_COUNT,
    )
    rfh.setFormatter(settings.CeleryLogger.FORMATTER)
    logger.addHandler(rfh)
