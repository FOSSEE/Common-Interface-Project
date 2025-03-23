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
from datetime import datetime
from django.conf import settings
import logging
import logging.config


class DateChangeFilter(logging.Filter):
    last_date = None

    def filter(self, record):
        current_date = datetime.now().date()
        if DateChangeFilter.last_date != current_date:
            DateChangeFilter.last_date = current_date
            logging.getLogger().info(f"--- {current_date} ---")
        return True


# Define log format
LOG_FILE = "logs/celery.log"

LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(threadName)s]: %(message)s"

LOG_DATE_FORMAT = "%H:%M:%S"

CELERY_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "formatter": {
            "format": LOG_FORMAT,
            "datefmt": LOG_DATE_FORMAT,
        },
    },
    "filters": {
        "date_change_filter": {
            "()": DateChangeFilter,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "formatter",
            "filters": ["date_change_filter"],
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_FILE,
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "formatter": "formatter",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "celery.task": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(CELERY_LOGGING_CONFIG)

logger = logging.getLogger("celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')

app = Celery('blocks')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_connection_retry_on_startup = True
app.conf.worker_hijack_root_logger = False


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@worker_ready.connect
def startup_code(**kwargs):
    logger.info("Running global startup code")
    start_threads()


@worker_shutdown.connect
def shutdown_code(**kwargs):
    logger.info("Running global shutdown code")
    stop_threads()
