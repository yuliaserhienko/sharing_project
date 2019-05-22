import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharing.settings')

app = Celery('sharing')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
