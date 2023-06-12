from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
	"""
	This serializer performs translation
	the data of the current model fields 
	to the JSON format.
	"""
	class Meta:
		model = Book
		fields = ('title', 'subtitle', 'author', 'isbn')