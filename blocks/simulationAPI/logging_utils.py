import logging
from celery.utils.log import get_task_logger


class TaskLoggerAdapter(logging.LoggerAdapter):
    """LoggerAdapter that injects task_name and task_id into log records."""
    def process(self, msg, kwargs):
        kwargs["extra"] = kwargs.get("extra", {})
        kwargs["extra"].setdefault("task_name", self.extra.get("task_name", "UNKNOWN_TASK"))
        kwargs["extra"].setdefault("task_id", self.extra.get("task_id", "N/A"))
        return msg, kwargs


def get_task_logger_adapter(name):
    """Returns a LoggerAdapter for Celery tasks."""
    base_logger = get_task_logger(name)
    return TaskLoggerAdapter(base_logger, {})
