from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Gallery, Comment

@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status','flagged',)
    search_fields = ['title', 'author', 'flagged', 'status',]
    list_filter = ('status', 'flagged',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved', 'flagged', 'feature_img')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'email', 'body')

    def approve_comment(self, request, queryset):
        queryset.update(approved=1)
    approve_comment.short_description = "Approve selected comments"

    def flagged_comment(self, request, queryset):
        queryset.update(flagged=True)
    flagged_comment.short_description = "Flag selected comment"
    
    actions = [approve_comment, flagged_comment]