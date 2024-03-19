from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Route, Comment

@admin.register(Route)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'flagged',)
    search_fields = ['title', 'content', 'flagged',]
    list_filter = ('status', 'created_on', 'flagged',)
    
    def publish_posts(self, request, queryset):
        queryset.update(status=1)
    publish_posts.short_description = "Publish selected posts"

    def flagged_posts(self, request, queryset):
        queryset.update(flagged=True)
    flagged_posts.short_description = "Flag selected posts"
    
    actions = [publish_posts, flagged_posts]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved', 'flagged',)
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'email', 'body')

    def approve_comment(self, request, queryset):
        queryset.update(approved=1)
    approve_comment.short_description = "Approve selected comments"

    def flagged_comment(self, request, queryset):
        queryset.update(flagged=True)
    flagged_comment.short_description = "Flag selected comment"
    
    actions = [approve_comment, flagged_comment]
