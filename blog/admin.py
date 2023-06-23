from django.contrib import admin

from .models import Post, Comment
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Post, MarkdownxModelAdmin)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'image', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
