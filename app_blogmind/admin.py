from django.contrib import admin
from .models import Post, CustomUser
from django.contrib.auth.admin import UserAdmin
"""@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['user.id']
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','profile_image']"""

admin.site.register(CustomUser, UserAdmin)

# Registrando o modelo Post
admin.site.register(Post)


