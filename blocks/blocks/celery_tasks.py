import sys

# Apply monkey patching only if running Celery
if "celery" in sys.argv[0]:
    from gevent.monkey import patch_all

    patch_all(aggresive=False)

    from simulationAPI.helpers.scilab_manager import \
        start_threads, stop_threads

import os
from celery import Celery
from celery.signals import worker_ready, worker_shutdown
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')

app = Celery('blocks')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_connection_retry_on_startup = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@worker_ready.connect
def startup_code(**kwargs):
    print("Running global startup code")
    start_threads()


@worker_shutdown.connect
def shutdown_code(**kwargs):
    print("Running global shutdown code")
    stop_threads()
