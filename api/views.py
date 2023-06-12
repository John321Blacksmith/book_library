from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

# Create your views here.


class BookAPIView(generics.ListAPIView):
	"""
	This view fetches a queryset of books
	and invokes the JSON serializer
	to convert queryset data to JSON.
	"""
	queryset = Book.objects.all()
	serializer_class = BookSerializer