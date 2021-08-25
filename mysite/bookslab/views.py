from django.http import HttpResponse
from django.shortcuts import render
from bookslab.models import Book


def many(request):
	command=""
	bookname=""
	price=""
	subject=""
	result=""
	if request.GET:
		command=request.GET["command"]
	if command=="Insert":
		bookname=request.GET["bookname"]
		price=request.GET["bookprice"]
		subject=request.GET["booksubject"]
		book=Book(bookname=bookname,price=price,subject=subject)
		book.save()
		result="Inserted Successfully"
	data={"result":result,"name":bookname,"price":price,"subject":subject}
	return render(request,"insert.html",{"data":data})
	
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
def update(request):
	book=Book.objects.filter(price=200)
	if len(book)==0:
		return HttpResponse("None")
	else:
		book[0].bookname="New Name"
		book[0].save()
		return HttpResponse("Book Name = " + str(book[0].bookname))
def delete(request):
	book=Book.objects.filter(price=399)
	if len(book)==0:
		return HttpResponse("None")
	else:
		book[0].delete()
		return HttpResponse("Book Name = " + str(book[0].bookname))
	
def find(request):
	book=Book.objects.filter(price=399) & Book.objects.filter(bookname="Basic Java")
	if len(book)==0:
		return HttpResponse("None")
	else:
		return HttpResponse("Book Name = " + str(book[0].bookname))
def all(request):
	books=Book.objects.all().order_by('bookname')
	n=len(books)
	data={"books":books}
	return render(request,"booksshow.html",{"data":data})
