from django.http import HttpResponse
from django.shortcuts import render
from bookslab.models import Book
	
def insert(request):
	bookname="The Recursion Sutras"# request.GET["bookname"]
	price=399#request.GET["price"]
	subject="Recursion"#request.GET["subject"]
	print(bookname,price,subject)
	book=Book(
	bookname=bookname,price=price,subject=subject
	)
	book.save()
	return HttpResponse("Inserted")
	
def find(request):
	book=Book.objects.filter(price=399)
	if len(book)==0:
		return HttpResponse("None")
	else:
		return HttpResponse("Book Name = " + str(book[0].bookname))
def all(request):
	books=Book.objects.all()
	n=len(books)
	return HttpResponse("No of books " + str(n))
