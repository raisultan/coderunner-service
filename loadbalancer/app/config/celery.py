from celery import Celery

from .settings import settings

celery_app = Celery('celery_app')
celery_app.config_from_object(settings, namespace='CELERY')
celery_app.autodiscover_tasks(packages=['app.tasks'])
