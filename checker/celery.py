from celery import Celery
from celery.schedules import crontab

app = Celery('checker', include=['checker.tasks'])
app.config_from_object('checker.celeryconfig')
app.conf.beat_schedule = {
    'run-me-every-one-hour': {
        'task': 'checker.tasks.check',
        'schedule': crontab(minute='*/30'),
    }
}
