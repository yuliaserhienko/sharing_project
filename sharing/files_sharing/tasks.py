from django.utils import timezone

from celery import shared_task
from files_sharing.models import File


@shared_task
def delete_old_files():
    files = File.objects.filter(file_lifetime_date__lte=timezone.now())
    deleted = len([file.delete() for file in files])
    return f'Files deleted: {deleted}'
