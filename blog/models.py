from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
	class Meta:
		verbose_name_plural = 'Categories'

	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=150, unique=True)
	excerpt = models.CharField(max_length=200)
	image = CloudinaryField('image')
	slug = models.SlugField(unique=True)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='post', null=True)
	likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

	def number_of_likes(self):
		return self.likes.count()


class Comment(models.Model):
	text = models.TextField(max_length=400)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)


