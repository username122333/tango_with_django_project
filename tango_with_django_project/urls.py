from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> 5713a1011b5570c6fd8750eec798d7ed32f38915
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
<<<<<<< HEAD
    url(r'^rango/', include('rango.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
<<<<<<< HEAD
    url(r'^rango/', include('rango.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
<<<<<<< HEAD
    url(r'^rango/', include('rango.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
    url(r'^rango/', include('rango.urls'))
]

>>>>>>> 5713a1011b5570c6fd8750eec798d7ed32f38915
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
