from django.contrib import admin
from .models import Book, Magazine, DVD, CD

# Register your models here.


admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(DVD)
admin.site.register(CD)