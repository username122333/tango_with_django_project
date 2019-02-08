from django.contrib import admin
<<<<<<< HEAD
from rango.models import Category, Page, UserProfile
=======
<<<<<<< HEAD
from rango.models import Category, Page, UserProfile
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
from rango.models import Category, Page
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b

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
admin.site.register(UserProfile)
=======
<<<<<<< HEAD
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
=======
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
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
>>>>>>> 23b13ac84ac2803559a2fcb97ee688a7d443278b
