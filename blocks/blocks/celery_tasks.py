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

TASK_LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(task_name)s/%(task_id)s]: %(message)s"
WORKER_LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(processName)s/%(process)d]: %(message)s"

LOG_DATE_FORMAT = "%H:%M:%S"

CELERY_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "task_formatter": {
            "format": TASK_LOG_FORMAT,
            "datefmt": LOG_DATE_FORMAT,
        },
        "worker_formatter": {
            "format": WORKER_LOG_FORMAT,
            "datefmt": LOG_DATE_FORMAT,
        },
    },
    "filters": {
        "date_change_filter": {
            "()": DateChangeFilter,
        },
    },
    "handlers": {
        "task_console": {
            "class": "logging.StreamHandler",
            "formatter": "task_formatter",
        },
        "worker_console": {
            "class": "logging.StreamHandler",
            "formatter": "worker_formatter",
            "filters": ["date_change_filter"],
        },
        "task_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_FILE,
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "formatter": "task_formatter",
            "encoding": "utf-8",
        },
        "worker_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_FILE,
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "formatter": "worker_formatter",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "celery.task": {
            "handlers": ["task_console", "task_file"],
            "level": "INFO",
            "propagate": False,
        },
        "celery": {
            "handlers": ["worker_console", "worker_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(CELERY_LOGGING_CONFIG)

worker_logger = logging.getLogger("celery")

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
    worker_logger.info("Running global startup code")
    start_threads()


@worker_shutdown.connect
def shutdown_code(**kwargs):
    worker_logger.info("Running global shutdown code")
    stop_threads()
