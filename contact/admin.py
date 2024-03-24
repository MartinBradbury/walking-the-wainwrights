from django.contrib import admin
from .models import CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)