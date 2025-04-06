from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.title
    

from .models import Post  # Import the Post model from the same app

class Comment(models.Model):  # Define a Comment model
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to a Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a User
    content = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

