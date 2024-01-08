from celery import Celery
from celery.schedules import crontab

from common.config import settings

celery_app = Celery('tasks', broker=settings.RABBITMQ_URL, include=['celery_worker.tasks'])
celery_app.conf.timezone = 'Asia/Ho_Chi_Minh'

celery_app.conf.beat_schedule = {
    'add-every-12-am': {
        'task': 'celery_worker.tasks.send_email_remind_buying',
        'schedule': crontab(minute='0', hour='0')
    },
}
