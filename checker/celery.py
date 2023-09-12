from celery import Celery


app = Celery('checker', include=['checker.tasks'])
app.config_from_object('checker.celeryconfig')
app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'checker.tasks.check',
        'schedule': 10.0
    }
}
