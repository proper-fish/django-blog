from django.contrib import admin
from .models import Post, Comment, Suggested


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('published_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Suggested)
