  # myapp/tasks.py
from celery import shared_task

@shared_task
def send_query(query):
    # Your email sending logic here
    print(query) 