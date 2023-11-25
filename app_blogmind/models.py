from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profile_images/', default='profile-1.jpg')

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_images/')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.created.year, self.created.month, self.created.day, self.slug])

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

