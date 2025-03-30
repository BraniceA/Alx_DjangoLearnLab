from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author, Book
from django.test import TestCase

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data."""
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create an Author instance
        self.author1 = Author.objects.create(name="J.R.R. Tolkien")
        
        # Create some test books
        self.book1 = Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937)
        self.book2 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book3 = Book.objects.create(title="Brave New World", author="Aldous Huxley", publication_year=1932)

        # API endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    
    # CRUD TESTS
    

    def test_create_book(self):
        """Test creating a book (POST request)."""
        self.client.login(username='testuser', password='testpassword')  # Authenticate user
        data = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1965}
        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  # Ensure book was created
        self.assertEqual(Book.objects.last().title, "Dune")

    def test_get_book_list(self):
        """Test retrieving the book list (GET request)."""
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Ensure all books are returned

    def test_get_book_detail(self):
        """Test retrieving a single book (GET request)."""
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_update_book(self):
        """Test updating a book (PUT request)."""
        self.client.login(username='testuser', password='testpassword')
        data = {"title": "The Hobbit: Revised", "author": "J.R.R. Tolkien", "publication_year": 1937}
        response = self.client.put(self.detail_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()  # Reload the book from the database
        self.assertEqual(self.book1.title, "The Hobbit: Revised")

    def test_delete_book(self):
        """Test deleting a book (DELETE request)."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())  # Ensure book is deleted


    # FILTERING, SEARCHING, AND ORDERING TESTS


    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        response = self.client.get(f"{self.list_url}?author=George Orwell")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        """Test searching books by title."""
        response = self.client.get(f"{self.list_url}?search=Brave")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Brave New World")

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book_titles = [book["title"] for book in response.data]
        self.assertEqual(book_titles, ["Brave New World", "The Hobbit", "1984"])  # Sorted by year (ascending)

    def test_reverse_order_books_by_publication_year(self):
        """Test ordering books in descending order by publication year."""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book_titles = [book["title"] for book in response.data]
        self.assertEqual(book_titles, ["1984", "The Hobbit", "Brave New World"])  # Sorted by year (descending)

    
    # AUTHENTICATION & PERMISSIONS TESTS
    

    def test_create_book_unauthorized(self):
        """Ensure unauthorized users cannot create a book."""
        data = {"title": "Unauthorized Book", "author": "Unknown", "publication_year": 2022}
        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Unauthorized access

    def test_update_book_unauthorized(self):
        """Ensure unauthorized users cannot update a book."""
        data = {"title": "Hacked Book", "author": "Hacker", "publication_year": 2025}
        response = self.client.put(self.detail_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Unauthorized access

    def test_delete_book_unauthorized(self):
        """Ensure unauthorized users cannot delete a book."""
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Unauthorized access
