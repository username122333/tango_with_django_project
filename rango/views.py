<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from datetime import datetime
=======
=======
from rango.forms import CategoryForm, PageForm
from django.urls import reverse
=======
from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages': page_list}

	visitor_cookie_handler(request)
	context_dict['visits'] = request.session['visits']
	response = render(request, 'rango/index.html', context_dict)

	return response



def about(request):
	return render(request, 'rango/about.html', {"visits": request.session['visits']})



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
<<<<<<< HEAD

@login_required
def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if category:
				page = form.save(commit=False)
				page.category = category
				page.views = 0
				page.save()
			return HttpResponseRedirect(reverse('rango:show_category', kwargs = {"category_name_slug": category_name_slug}))
		else:
			print(form.errors)

	context_dict = {'form':form, 'category': category}

	return render(request, 'rango/add_page.html', context_dict)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b


def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
<<<<<<< HEAD
				return HttpResponseRedirect(reverse('rango:index'))
=======
				return HttpResponseRedirect(reverse('index'))
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			return render(request, 'rango/login.html', {"wronguser": True})
	else:
		return render(request, 'rango/login.html')


@login_required
def restricted(request):
	return render(request, 'rango/restricted.html')

<<<<<<< HEAD

=======
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('rango:index'))
<<<<<<< HEAD


def visitor_cookie_handler(request):
	visits = int(request.COOKIES.get('visits', '1'))
	last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

	if (datetime.now() - last_visit_time).days > 0:
		visits += 1
		request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = last_visit_cookie

	request.session['visits'] = visits


def get_server_side_cookie(request, cookie, default_val = None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val






=======
=======
=======
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
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b
