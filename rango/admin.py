from django.contrib import admin
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
<<<<<<< HEAD
admin.site.register(Page, PageAdmin)
=======
admin.site.register(Page, PageAdmin)
=======
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
=======
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731


>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
