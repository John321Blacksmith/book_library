from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.

class BooksListView(ListView):
	"""
	This view renders all the books
	available on the site.
	"""
	model = Book
	template_name = 'books/books_list.html'