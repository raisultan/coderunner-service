from celery import Celery

from .settings import settings

celery_app = Celery('loadbalancer')
celery_app.config_from_object(settings, namespace='CELERY')
celery_app.autodiscover_tasks()
