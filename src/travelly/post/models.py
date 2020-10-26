from django.db import models

from django.conf import settings

# Create your models here.


class Post(models.Model):

	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	text 			= 	models.CharField(max_length = 4000, blank = True)
	photo 			=	models.FileField(blank = True)
	video 			= 	models.FileField(blank = True)
	location 		= 	models.CharField(max_length = 4000, blank = True)
	likes 			=	models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True , related_name = 'Likes')
	created_at 		=  	models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):

		return str(self.user.full_name) + '-' +'Post' 






class Comment(models.Model):
	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			= 	models.ForeignKey(Post, on_delete = models.CASCADE)
	text 			= 	models.CharField(max_length = 4000, blank = True)
	photo 			= 	models.FileField(blank = True)
	created_at 		=  	models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):

		return str(self.user.full_name) + '-' +'Post' 