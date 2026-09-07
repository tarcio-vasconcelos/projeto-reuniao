# seu_app/apps.py
from django.apps import AppConfig

class ReuniaoConfig(AppConfig):
    name = 'reuniao'

    def ready(self):
        import reuniao.signals