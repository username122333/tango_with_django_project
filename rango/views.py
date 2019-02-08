from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render

def index(request):
	
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	return render(request, 'rango/about.html')
=======

def index(request):
	return HttpResponse("Rango says hey there partner! <br> <a href = '/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Rango says here is the about page. <br> <a href = '/rango/'>Index</a>")
>>>>>>> 5713a1011b5570c6fd8750eec798d7ed32f38915
