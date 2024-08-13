from __future__ import absolute_import, unicode_literals

# Importa Celery para asegurar que se registre el módulo.
from .celery import app as celery_app

__all__ = ('celery_app',)
