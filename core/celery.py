import os
from celery import Celery

# Django settings faylini ko‘rsatamiz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Django settings.py dan CELERY_ bilan boshlanadigan sozlamalarni o‘qiydi
app.config_from_object('django.conf:settings', namespace='CELERY')

# Barcha app’lardan tasklarni avtomatik yuklab oladi
app.autodiscover_tasks()