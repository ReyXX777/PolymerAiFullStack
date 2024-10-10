from celery import Celery

celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task
def polymer_property_task(input_data):
    # Simulate async long-running ML task
    return "Task Complete"
