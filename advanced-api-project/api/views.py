from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework

# Create your views here.
# ListView: Anyone can read books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()       # ListView - Retrieve all books
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year']

# DetailView: Anyone can view a book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()       # DetailView - Retrieve a single book by ID
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible

# CreateView: Only authenticated users can create books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create books

    def perform_create(self, serializer):
        # Check if a book with the same title exists
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise ValidationError({"title": "A book with this title already exists."})
        serializer.save()  # Save the book

# UpdateView: Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Users can update, but non-users can only read

    def perform_update(self, serializer):
        # Prevent changing the book title to an already existing one
        title = serializer.validated_data.get('title')
        if Book.objects.exclude(pk=self.get_object().pk).filter(title=title).exists():
            raise ValidationError({"title": "A book with this title already exists."})
        serializer.save()

# DeleteView: Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires login

# Filtering books based on query parameters
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']  # Allows searching by book title or author name
    ordering_fields = ['publication_year']  # Allows ordering by publication year







