import threading
import time
import logging
from django.conf import settings
import requests

LOGGER = logging.getLogger("self_pinger")

PING_INTERVAL_SECONDS = 14 * 60  # 14 minutes


def ping_once():
    """Send one GET request to the RENDER_SELF_URL and return status code or None on error."""
    try:
        resp = requests.get(settings.RENDER_SELF_URL, timeout=10)
        LOGGER.info("Self-ping to %s returned %s", settings.RENDER_SELF_URL, resp.status_code)
        return resp.status_code
    except Exception:
        LOGGER.exception("Self-ping to %s failed", settings.RENDER_SELF_URL)
        return None


def _loop():
    while True:
        ping_once()
        time.sleep(PING_INTERVAL_SECONDS)


def start_self_pinger():
    """Start a background daemon thread that pings the render URL every interval."""
    t = threading.Thread(target=_loop, name="self-pinger", daemon=True)
    t.start()
    LOGGER.info("Background self-pinger thread launched")
