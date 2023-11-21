from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='img/', blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        related_query_name="customuser",
        blank=True,
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        related_query_name="customuser",
        blank=True,
        verbose_name="user permissions",
    )

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

