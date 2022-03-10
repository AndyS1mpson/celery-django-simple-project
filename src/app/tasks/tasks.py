from proj.celery_app import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def supper_sum(x, y):
    print("Calculating value:")
    print(x+y)
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@app.task(bind=True, default_retry_delay=5*60)
def my_task_retry(self, x, y):
    try:
        print(x+y)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
