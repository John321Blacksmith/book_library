from django.db import models

# Create your models here.


class LibraryItem(models.Model):
	"""
	This abstract model describes
	the common properties each
	item in the library has.
	"""

	upc = models.IntegerField()
	title = models.CharField(max_length=200)
	subject = models.CharField(max_length=40)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


# class Contributor(models.Model):
# 	"""
# 	This model represents an
# 	every person who's contributed
# 	to the library item creation.
# 	"""
# 	name = models.CharField(max_length=200)


class Book(LibraryItem):
	"""
	This child model inherits
	from the main LibraryItem.
	"""
	isbn = models.CharField(max_length=13)
	dds = models.CharField(max_length=10)


class Magazine(LibraryItem):
	"""
	This child model inherits
	from the main LibraryItem.
	"""
	issue_num = models.CharField(max_length=10)
	volume_num = models.CharField(max_length=10)


class DVD(LibraryItem):
	"""
	This child model inherits
	from the main LibraryItem.
	"""
	genre = models.CharField(max_length=20)
	

class CD(LibraryItem):
	"""
	This child model inherits
	from the main LibraryItem.
	"""