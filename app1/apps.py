from django.apps import AppConfig
from django.conf import settings
import logging


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        # Don't start the self-pinger during tests
        if getattr(settings, "TESTING", False):
            logging.getLogger("app1").info("TEST mode detected — self-pinger will not be started.")
            return
        # Prevent multiple starts (e.g., autoreloader)
        if getattr(settings, "SELF_PINGER_STARTED", False):
            return
        try:
            from .self_pinger import start_self_pinger
            start_self_pinger()
            settings.SELF_PINGER_STARTED = True
            logging.getLogger("app1").info("Self-pinger started.")
        except Exception:
            logging.getLogger("app1").exception("Failed to start self-pinger")
