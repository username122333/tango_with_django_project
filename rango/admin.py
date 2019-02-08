from django.contrib import admin
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

<<<<<<< HEAD
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
=======
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
=======
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731


