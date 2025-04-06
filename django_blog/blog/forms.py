# This form inherits from UserCreationForm, which provides fields for username and password.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from taggit.forms import TagWidget  # Import the TagWidget from taggit

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field to the registration form

    class Meta:
        model = User  # Specify the user model to use
        fields = ['username', 'email', 'password1', 'password2']  # Fields to include in the form


from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


from .models import Comment  # Import Comment model

class CommentForm(forms.ModelForm):  # Create a form for Comment
    class Meta:
        model = Comment
        fields = ['content']  # Only show the content field in the form


# from taggit.forms import TagField
# from taggit.models import Tag

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=widgets.Textarea(attrs={'rows': 5, 'cols': 40}))  # Use Textarea widget for content
    tags = forms.CharField(widget=TagWidget())  # Use TagWidget for tags field
widgets
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
