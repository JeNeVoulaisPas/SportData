from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Réglez les paramètres de configuration de Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportsDataForNerds.settings')

# Créez une instance de l'application Celery
app = Celery('sportsDataForNerds')

# Chargez la configuration de votre projet Django dans Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Découvrez les tâches à partir des modules enregistrés dans l'application Django
app.autodiscover_tasks()