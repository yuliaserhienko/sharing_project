from django.forms import ModelForm
from files_sharing import models


class FileUploadForm(ModelForm):

    class Meta:
        model = models.File
        fields = ['file', 'file_lifetime']

