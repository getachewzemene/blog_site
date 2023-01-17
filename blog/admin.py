from django.contrib import admin

# Register your models here.

from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', "created_at")
    display_filster = ('title', 'created_at', "author")


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
