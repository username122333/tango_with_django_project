from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages': page_list}

	# Render the response and send it back
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	try:
		category = Category.objects.get(slug = category_name_slug)
		pages = Page.objects.filter(category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category

	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context_dict)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
from django.shortcuts import render

def index(request):
	
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	return render(request, 'rango/about.html')
<<<<<<< HEAD
=======
=======

def index(request):
	return HttpResponse("Rango says hey there partner! <br> <a href = '/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Rango says here is the about page. <br> <a href = '/rango/'>Index</a>")
>>>>>>> 5713a1011b5570c6fd8750eec798d7ed32f38915
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
