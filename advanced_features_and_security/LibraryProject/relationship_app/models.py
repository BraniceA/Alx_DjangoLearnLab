from django.db import models

# Create your models here.
# Define Complex Models in relationship_app/models.py:

#     Author Model:
#         name: CharField.
#     Book Model:
#         title: CharField.
#         author: ForeignKey to Author.
#     Library Model:
#         name: CharField.
#         books: ManyToManyField to Book.
#     Librarian Model:
#         name: CharField.
#         library: OneToOneField to Library.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
