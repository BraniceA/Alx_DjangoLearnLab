from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '<script>' in title:
            raise forms.ValidationError("Invalid input detected!")
        return title

