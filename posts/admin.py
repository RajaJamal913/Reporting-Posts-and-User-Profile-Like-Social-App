from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_text', 'created_at')
    search_fields = ('user__username', 'content_text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Post, PostAdmin)
