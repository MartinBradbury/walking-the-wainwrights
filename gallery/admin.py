from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status','flagged',)
    search_fields = ['title', 'author', 'flagged', 'status',]
    list_filter = ('status', 'flagged',)