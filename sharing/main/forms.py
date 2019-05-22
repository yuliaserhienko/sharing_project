from django.forms import forms, fields
from django.contrib.auth import models


class AuthorizationForm(forms.Form):
    username = fields.CharField()
    password = fields.CharField()

