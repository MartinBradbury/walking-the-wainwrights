from django.contrib import admin
from .models import About, Wainwright, Carousel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Wainwright)
class WainwrightAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'img_1', 'img_2', 'img_3')
