from rest_framework import serializers
from api.models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer): # serializes all fields of the Book model.
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):     #ensures the publication_year is not in the future.
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nesting BookSerializer serializes related books dynamically
    class Meta:
        model = Author
        fields = 'name'                             # Only the name field is serialized.