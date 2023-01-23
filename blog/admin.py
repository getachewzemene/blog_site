from django.contrib import admin

# Register your models here.

from .models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', "created_at")
    list_display = ('title', 'created_at', "author")
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
