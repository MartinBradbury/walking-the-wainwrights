from django.contrib import admin
from .models import Route
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Route)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'flagged',)
    search_fields = ['title', 'content', 'flagged',]
    list_filter = ('status', 'created_on', 'flagged',)
    
