import asyncio

from celery import shared_task, Celery
from celery.utils.log import get_task_logger

from helper.config import config
from helper.email_helper import send_mail

celery = Celery(__name__)
celery.conf.broker_url = config['CELERY_BROKER_URL']

logger = get_task_logger(__name__)

@shared_task(name="send_email_task")
def send_email_task(data):
    asyncio.get_event_loop().run_until_complete(send_mail(data))