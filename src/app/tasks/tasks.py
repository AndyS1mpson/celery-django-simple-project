from proj.celery_app import app


@app.task
def supper_sum(x, y):
    print(x+y)
    return x + y


@app.task(bind=True, default_retry_delay=5*60)
def my_task_retry(self, x, y):
    try:
        print(x+y)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

