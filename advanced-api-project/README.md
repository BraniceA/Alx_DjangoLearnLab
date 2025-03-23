Book Management API

This API allows users to manage books and authors using Django and Django REST Framework.

Features:
- View all books
- View a single book
- Add a new book (authenticated users only)
- Update a book (authenticated users only)
- Delete a book (authenticated users only)

Installation:
1. Clone the repository:
   git clone https://github.com/your-repo/book-api.git
   cd book-api
2. Install dependencies:
   pip install -r requirements.txt
3. Apply migrations:
   python manage.py migrate
4. Create a superuser (optional):
   python manage.py createsuperuser
5. Run the server:
   python manage.py runserver

API Endpoints:
- GET /books/ - List all books
- GET /books/<id>/ - Retrieve a book by ID
- POST /books/create/ - Add a new book (authenticated users only)
- PUT/PATCH /books/update/<id>/ - Update a book (authenticated users only)
- DELETE /books/delete/<id>/ - Delete a book (authenticated users only)

Authentication & Permissions:
- Public users can view books.
- Only authenticated users can add, update, or delete books.

Usage Example:
Retrieve all books:
curl -X GET http://127.0.0.1:8000/books/

Create a new book:
curl -X POST http://127.0.0.1:8000/books/create/ \
     -H "Authorization: Token YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"title": "New Book", "publication_year": 2024, "author": 1}'

License:
This project is licensed under the MIT License.

