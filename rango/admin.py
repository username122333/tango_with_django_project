from django.contrib import admin
<<<<<<< HEAD
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
=======
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58


