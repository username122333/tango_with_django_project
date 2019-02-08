from django.conf.urls import url
from rango import views

<<<<<<< HEAD
app_name = 'rango'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category')
]
=======
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about')

]
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
