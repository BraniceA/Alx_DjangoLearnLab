from django.db import models

# Create your models here.
class Author(models.Model):     # Author model with a name field.
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Book(models.Model):       # Book model with title, publication_year, and author fields.
    title = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='books')

    def __str__(self):
        return self.title