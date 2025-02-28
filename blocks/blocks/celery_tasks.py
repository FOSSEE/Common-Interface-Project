from simulationAPI.helpers.scilab_manager import (
    prestart_scilab_instances,
    reap_scilab_instances,
    clean_sessions_thread,
    stop_scilab_instances,
    clean_sessions
)
import os
import redis
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')
django.setup()
import multiprocessing

from celery import Celery
from celery.signals import worker_shutdown
import gevent

from django.conf import settings


app = Celery('blocks')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_connection_retry_on_startup = True

SCILAB_DIR = os.path.abspath(settings.SCILAB_DIR)
SCILAB = os.path.join(SCILAB_DIR, 'bin', 'scilab-adv-cli')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Initialize Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Global keys for startup and shutdown
STARTUP_KEY = "celery_startup_done"
SHUTDOWN_KEY = "celery_shutdown_done"


# ✅ Ensure startup runs **only once** using Redis lock
if multiprocessing.current_process().name == "MainProcess":
    if not redis_client.get(STARTUP_KEY):  # Check if startup was already executed
        print("🚀 Running global startup code only once!")
        redis_client.set(STARTUP_KEY, "1", ex=60)  # Optional: expire after 60s
    else:
        print("🚀 Global startup already executed, skipping.")


@worker_shutdown.connect
def global_shutdown_code(**kwargs):
    """Ensures shutdown logic runs only once globally using Redis."""
    if multiprocessing.current_process().name == "MainProcess":
        if not redis_client.get(SHUTDOWN_KEY):  # Check if shutdown already executed
            print("🔴 Running global shutdown code only once!")
            redis_client.set(SHUTDOWN_KEY, "1", ex=60)  # Optional: expire after 60s
        else:
            print("🔴 Global shutdown already executed, skipping.")
