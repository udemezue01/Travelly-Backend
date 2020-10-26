from django.db import models
from django.conf import settings



class Profile(models.Model):

	user 			= 	models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	avatar 			= 	models.FileField(blank = True)
	cover_photo 	= 	models.FileField(blank = True)

	username 		= 	models.CharField(max_length = 3000)
	bio 			= 	models.CharField(max_length = 4000, blank = True)
	location		= 	models.CharField(max_length = 4000, blank = True)

	def __str__(self):

		return str(self.user.email) + '-' + 'Profile'

		