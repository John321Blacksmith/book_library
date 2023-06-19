from django.test import TestCase
from .models import Contributor, Book, Magazine, DVD, CD
# Create your tests here.


class LibraryModelsDataTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# create several contributors
		cls.contributor1 = Contributor.objects.create('Frank F.')
		cls.contributor2 = Contributor.objects.create('John K.')
		cls.contributor3 = Contributor.objects.create('Paul V.')
		cls.contributor5 = Contributor.objects.create('Will M.')
		cls.contributor6 = Contributor.objects.create('Will M.')
		cls.contributor7 = Contributor.objects.create('Will M.')

		# create several library items
		cls.book = Book.objects.create(
					title='Test Book',
					upc='t111',
					subject='testing',
					isbn='111222333444',
					dds='55.66T',
					contributors=cls.contributor1,
			)
		cls.magazine = Magazine.objects.create(
					title='Test Magazine',
					upc='t222',
					subject='testing',
					issue_num='#555',
					volume_num='5',
					contributors=cls.contributor2,
			)
		cls.dvd = DVD.objects.create(
					title='Test dvd',
					upc='t333',
					subject='testing',
					genre='test',
					contributors=cls.contributor3,
			)
		cls.cd = CD.objects.create(
					title='Test cd',
					upc='t444',
					subject='testing',
					contributors=cls.contributor4,
			)


	def test_contributors_exist(self):
		self.assertIn(self.contributor1, Contributor.objects.all())
		self.assertIn(self.contributor2, Contributor.objects.all())
		self.assertIn(self.contributor3, Contributor.objects.all())
		self.assertIn(self.contributor5, Contributor.objects.all())
		self.assertIn(self.contributor6, Contributor.objects.all())
		self.assertIn(self.contributor7, Contributor.objects.all())


