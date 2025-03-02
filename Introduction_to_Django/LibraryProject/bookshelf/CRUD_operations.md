<!-- CREATE A BOOK -->

from myapp.models import Book
<!-- Create a Book instance -->
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<!-- Confirm creation -->
print(book)
<!-- OUTPUT -->
1984 by George Orwell (1949)



<!-- RETRIEVE A BOOK -->

<!--  Retrieve -->
retrieved_book = Book.objects.get(title="1984")
<!-- DISPLAY BOOK DETAILS -->
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")
<!-- OUTPUT -->
Title: 1984, Author: George Orwell, Year: 1949



<!-- UPDATE A BOOK -->

<!-- TO RETRIEVE THE BOOK -->
book = Book.objects.get(title="1984")
<!-- TO UPDATE THE TITLE OF THE BOOK -->
book.title = "Nineteen Eighty-Four"
<!-- TO SAVE CHANGES MADE -->
book.save()
<!-- TO PRINT AND SEE IF CHANGES HAVE BEEN MADE -->
print(f"Updated Title: {book.title}")
<!-- OUTPUT -->
Updated Title: Nineteen Eighty-Four



<!-- DELETE A BOOK -->

<!-- TO RETRIEVE THE BOOK -->
book = Book.objects.get(title="Nineteen Eighty-Four")
<!-- TO DELETE THE BOOK -->
book.delete()
<!-- TO CONFIRM IF BOOK WAS DELETED -->
print(Book.objects.all())
<!-- OUTPUT -->
<QuerySet []>