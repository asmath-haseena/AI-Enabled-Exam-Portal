from django import forms
from django.forms import ModelForm
from django.db import models
from django.db.models import fields
from adminapp.models import Suser, Fuser

class Suserprofileform(ModelForm):
    class Meta:
        model=Suser
        fields="__all__"

class Fuserprofileform(ModelForm):
    class Meta:
        model=Fuser
        fields="__all__"