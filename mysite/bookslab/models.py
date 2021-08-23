from django.db import models

# Create your models here.
class Book(models.Model):
	bookname=models.CharField(max_length=50)
	price=models.IntegerField()
	subject=models.CharField(max_length=20)

	class Meta:
		db_table="book"

