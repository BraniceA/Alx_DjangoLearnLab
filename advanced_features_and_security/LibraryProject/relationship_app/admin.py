# from django.contrib import admin

# # Register your models here.
# from .models import Author, Book, Library, Librarian

# # Register your models here.(Boook)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name')  # Adjust fields as per your Author model
#     search_fields = ('name',)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'library')  # Adjust fields as per your Book model
#     search_fields = ('title', 'author__name', 'library__name')
#     list_filter = ('library', 'author')

# @admin.register(Library)
# class LibraryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'librarian')  # Adjust fields as per your Library model
#     search_fields = ('name', 'books__title', 'librarian__name')
#     list_filter = ('librarian',)

# @admin.register(Librarian)
# class LibrarianAdmin(admin.ModelAdmin):
#     list_display = ('name', 'library')  # Adjust fields as per your Librarian model
#     search_fields = ('name', 'library__name')
#     list_filter = ('library',)
