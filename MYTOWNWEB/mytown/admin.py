from django.contrib import admin
from .models import *
# from automation.models import Trigger

# class RequestDemoAdmin(admin.ModelAdmin):
#     list_display = ("title", "city", "description", "location", "photo")  # Assuming these are valid fields in AddReport model

# admin.site.register(AddReport, RequestDemoAdmin)
@admin.register(AddReport)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddReport._meta.get_fields()]

@admin.register(Workerlogin)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Workerlogin._meta.get_fields()]


# @admin.register(Trigger)
# class TriggerAdmin(admin.ModelAdmin):
#     model = Trigger
#     list_display = ('Title', 'city', 'description', 'location','photo')
#     list_filter = ('Title', 'city', 'description')