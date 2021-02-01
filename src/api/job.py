import logging
import time

from celery import group
from kombu.exceptions import EncodeError

from setup import Setup
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)
setup = Setup()
conf = setup.get_config()
celery = setup.get_celery()


@celery.task()
def execute_group(group_to_exec: str):
    """Executes command."""
    try:
        log.info("Executing group in Celery: %s", group_to_exec)
        jobs_to_exec = conf['group'][group_to_exec]
        return group([execute_job.delay(job) for job in jobs_to_exec])
    except EncodeError:
        pass


@celery.task(track_started=True)
def execute_job(job_to_exec: str):
    """Executes command."""
    try:
        log.info("Executing job in Celery: %s", job_to_exec)
        time.sleep(200)
        command_to_exec = conf['job'][job_to_exec]
        log.info("Executing command in Celery: %s", command_to_exec)
    except EncodeError:
        pass
