from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
	path('', views.BooksListView.as_view(), name='home'),
]