<!-- TO ACCESS THE BOOK MODEL IN BOOKSHELF APP -->
from myapp.models import Book

<!-- Create a Book instance -->
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- Confirm creation -->
print(book)

<!-- OUTPUT -->
1984 by George Orwell (1949)