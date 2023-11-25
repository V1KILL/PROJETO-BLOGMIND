from django.contrib import admin
from .models import Post, UserProfile
"""@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['user.id']
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','profile_image']"""

# Registrando o modelo Post
admin.site.register(UserProfile)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


