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