from django.contrib.auth.models import Permission, User
from django.db import models

class Book(models.Model):
	book_name = models.CharField(max_length = 200)
	book_course = models.CharField(max_length = 4)
	book_sem = models.CharField(max_length = 1)
	book_sub = models.CharField(max_length = 100)
	book_price = models.CharField(max_length = 5)
	book_pno = models.CharField(max_length = 12)
	def __str__(self):
		return self.book_name
class Subject(models.Model):
	subject_name = models.CharField(max_length = 100)
	def __str__(self):
		return self.subject_name
		