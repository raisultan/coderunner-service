import os
import logging
from logging.handlers import RotatingFileHandler

from app.config import settings


def coderunner_logger_init() -> logging.Logger:
    logger = logging.getLogger(__name__)

    if not os.path.exists(settings.LOGS_DIR):
        os.makedirs(settings.LOGS_DIR)

    rfh = RotatingFileHandler(
        filename=f'{settings.LOGS_DIR}{settings.CoderunnerAPIDriverLogger.FILENAME}',
        maxBytes=settings.CoderunnerAPIDriverLogger.MAX_BYTES,
        backupCount=settings.CoderunnerAPIDriverLogger.BACKUP_COUNT,
    )
    rfh.setFormatter(settings.CoderunnerAPIDriverLogger.FORMATTER)
    logger.addHandler(rfh)
    return logger
