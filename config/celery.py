import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'config.settings.staging_alibaba'
)

app = Celery('tms_backend')

app.config_from_object('config.celeryconfig', namespace='CELERY')

app.autodiscover_tasks()
