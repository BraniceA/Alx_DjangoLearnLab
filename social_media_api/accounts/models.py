from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)  # User bio field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile image
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_followers', blank=True)  # Follow system
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following', blank=True)  # Users this user follows

    def __str__(self):
        return self.username


