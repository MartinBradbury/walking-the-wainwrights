from django.contrib import admin
from .models import CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)