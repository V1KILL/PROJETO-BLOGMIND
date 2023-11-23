from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profile_images/', default='profile-1.jpg')

    def __str__(self):
        return f'Profile of {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

