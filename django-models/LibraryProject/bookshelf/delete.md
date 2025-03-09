from bookshelf.models import Book
<!-- TO RETRIEVE THE BOOK -->
book = Book.objects.get(title="Nineteen Eighty-Four")

<!-- TO DELETE THE BOOK -->
book.delete()

<!-- TO CONFIRM IF BOOK WAS DELETED -->
print(Book.objects.all())

<!-- OUTPUT -->
<QuerySet []>
