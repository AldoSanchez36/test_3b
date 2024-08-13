from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configura el módulo de settings de Django para Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_3b.settings')

app = Celery('test_3b')

# Usa la configuración de Django para Celery.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga tareas de todos los módulos registrados en `INSTALLED_APPS`.
app.autodiscover_tasks()
