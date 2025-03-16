<!-- WHILE IN DJANGO SHELL -->
<!--  Retrieve -->
retrieved_book = Book.objects.get(title="1984")

<!-- DISPLAY BOOK DETAILS -->
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")

<!-- OUTPUT -->
Title: 1984, Author: George Orwell, Year: 1949