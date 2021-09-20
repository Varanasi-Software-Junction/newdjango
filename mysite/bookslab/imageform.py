# forms.py
from django import forms
from bookslab.models import *

class ImageForm(forms.ModelForm):

	class Meta:
		model = BookImage
		fields = ['bookname', 'book_img']
