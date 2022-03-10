import os
from datetime import timedelta
from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'proj.settings')


app = Celery()

# Загружаем конфигурацию
app.config_from_object('django.conf:settings', namespace='CELERY')


# Автоматический поиск задач
app.autodiscover_tasks()

@app.task()
def add(x, y):
    return x+y


app.conf.beat_schedule = {
    'sum_every_minute' : {
        'task': 'app.tasks.tasks.supper_sum',
        'schedule': timedelta(seconds=5),
        'args': (5, 8),
    }
}
