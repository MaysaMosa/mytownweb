from django.contrib import admin
from .models import *


@admin.register(AddReport)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddReport._meta.get_fields()]

@admin.register(Workerlogin)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Workerlogin._meta.get_fields()]