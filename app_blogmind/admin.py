from django.contrib import admin
from .models import Post, UserProfile, Comment

admin.site.register(UserProfile)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description', 'created', 'modified')


