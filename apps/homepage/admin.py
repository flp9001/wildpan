from django.contrib import admin

from .models import Comment
from .models import Like
from .models import Post
from .models import PostImage


class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 4


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
