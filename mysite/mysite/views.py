from django.http import HttpResponse
from django.shortcuts import render
from bookslab.models import Book
def index(request):
    html = "<h1>Default View</h1>"
    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello")
def add(request):
	a=0
	b=0
	if request.GET:
		a=int(request.GET["a"])
		b=int(request.GET["b"])
	sum=a + b
	data={"a":a,"b":b,"sum":sum}
	return render(request,"getform.html",{"data":data})
	
def loop(request):
	l=[1,2,3,4,5]
	data={"l":l}
	return render(request,"loops.html",{"data":data})
	
def sum(request):
	a=0
	b=0
	if request.POST:
		a=int(request.POST["a"])
		b=int(request.POST["b"])
	sum=a + b
	data={"a":a,"b":b,"sum":sum}
	return render(request,"postform.html",{"data":data})
