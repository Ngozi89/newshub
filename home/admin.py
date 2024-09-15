from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register post models and post admin class.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
