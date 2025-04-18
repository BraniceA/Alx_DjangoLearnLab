from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link to user
    title = models.CharField(max_length=255)  # post title
    content = models.TextField()  # post content
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp at creation
    updated_at = models.DateTimeField(auto_now=True)  # timestamp at update

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # link to post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # comment author
    content = models.TextField()  # comment text
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp at creation
    updated_at = models.DateTimeField(auto_now=True)  # timestamp at update

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevents duplicate likes
