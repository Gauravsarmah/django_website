from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
	return render(request,'myapp/index.html')


def about(request):
	return render(request,'myapp/about.html')


def contact(request):
	return render(request,'myapp/contact.html')


def services(request):
	return render(request,'myapp/services.html')
