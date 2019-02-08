from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import slugify

=======

<<<<<<< HEAD
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)
<<<<<<< HEAD
	slug = models.SlugField(unique = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
=======
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731

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
		return self.title
<<<<<<< HEAD
=======
=======
>>>>>>> e46c979f77ed0b63845697c217b74efa8cb41d58
>>>>>>> 9f3c297ec1bdf5b3f9157c8cdc599651ab02d731
