from django.contrib import admin
from home import models
# Register your models here.
from .models import *
admin.site.register(semester_info)
admin.site.register(Database)

