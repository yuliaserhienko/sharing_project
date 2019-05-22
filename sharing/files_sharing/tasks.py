from celery import shared_task
from files_sharing.models import File


@shared_task
def print_name():
    files = File.objects.all()
    for file in files:
        file.delete()
    return 'Yuliia'
