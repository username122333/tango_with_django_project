from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

=======
<<<<<<< HEAD
from django.template.defaultfilters import slugify

=======

<<<<<<< HEAD
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
	slug = models.SlugField(unique = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
<<<<<<< HEAD
=======
=======
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	views = models.IntegerField(default = 0)

	def __str__(self):
<<<<<<< HEAD
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank = True)
	picture = models.ImageField(upload_to = 'profile_images', blank = True)

	def __str__(self):
		return self.user.username
=======
<<<<<<< HEAD
		return self.title
=======
		return self.title
<<<<<<< HEAD
=======
=======
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
>>>>>>> d6767caf436c41502a09cd44ab9c469910f77532
>>>>>>> 6cd5a7f59521d6297bc6f83b54f5cae1641ffb1b
