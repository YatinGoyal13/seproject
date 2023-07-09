from django.contrib import admin
from .models import *


@admin.register(User)
class StartupUser(admin.ModelAdmin):
    list_display =  [
    'startUpName',
    'founder',
    'email',
    'description' ,
    'pitch_link' ,
    'video_link']
    actions = ["delete_selected"]

    def delete_selected(self, request, queryset):
        for element in queryset:
            element.delete()

    delete_selected.short_description = "Delete selected elements"
