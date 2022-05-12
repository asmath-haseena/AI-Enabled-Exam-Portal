from django.contrib import admin

# Register your models here.
from adminapp.models import Suser, Fuser
admin.site.register(Suser)
admin.site.register(Fuser)