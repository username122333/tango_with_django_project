from django.conf.urls import url
from rango import views

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
app_name = 'rango'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about'),
<<<<<<< HEAD
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
	url(r'^add_category/$', views.add_category, name = 'add_category'),
<<<<<<< HEAD
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$', views.user_login, name = 'login'),
	url(r'^restricted', views.restricted, name = 'restricted'),
	url(r'^logout/$', views.user_logout, name = 'logout')
]
=======
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page')
]
=======
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category')
]
=======
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about')

]
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
