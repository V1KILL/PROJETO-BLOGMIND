from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentado por {self.user}'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profile_images/', default='profile-default.jpg')
    background = models.ImageField(upload_to='background_images/', default='background-default.jpg')

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='profile_images/')
    description = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def formatted_date(self):
        return self.created.strftime("%d, %B, %Y")
    
    def formatted_modified(self):
        return self.modified.strftime("%d, %B, %Y")
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.created.year, self.created.month, self.created.day, self.slug])
    
    def get_absolute_url_comment(self):
        return reverse('comentar', args=[self.created.year, self.created.month, self.created.day, self.slug])
    
    def removepost(self):
        return reverse('removepost', args=[self.created.year, self.created.month, self.created.day, self.slug])

    def bio(self):
        return 

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

