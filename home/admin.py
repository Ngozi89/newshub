from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register post models and post admin class.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
# Search field.
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')

    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Allows admin to mamage comments on posts via the admin panael"""
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'email', 'body']