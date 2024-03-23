from django.contrib import admin
from .models import About, Wainwright
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Wainwright)
class WainwrightAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
