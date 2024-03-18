from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Route # Assuming Route is your model

@admin.register(Route)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'flagged',)
    search_fields = ['title', 'content', 'flagged',]
    list_filter = ('status', 'created_on', 'flagged',)
    
    # publish action
    def publish_posts(self, request, queryset):
        queryset.update(status=1)
    publish_posts.short_description = "Publish selected posts"
    
    # flag action
    def flagged_posts(self, request, queryset):
        queryset.update(flagged=True)
    flagged_posts.short_description = "Flag selected posts"
    
    # Add actions to the actions list
    actions = [publish_posts, flagged_posts]
