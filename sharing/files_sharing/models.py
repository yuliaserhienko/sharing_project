import datetime

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    file_lifetime = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    file_lifetime_date = models.DateTimeField(null=True)

    @property
    def name(self):
        return str(self.file).split('/')[1]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.file_lifetime_date = self.created + datetime.timedelta(days=self.file_lifetime)
        super().save(*args, **kwargs)


@receiver(post_delete, sender=File)
def delete_file_from_server(sender, instance, **kwargs):
    instance.file.delete(False)
