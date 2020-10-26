from django.db import models

from django.conf import settings





class Guide(models.Model):

	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	location		= 	models.CharField(max_length = 4000) 
	price 			=	models.IntegerField()
	time_available	= 	models.DateTimeField()
	created_at		=	models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):

		return str(self.user.full_name) + '-' + self.location


class Booking(models.Model):

	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			=	models.ForeignKey(Guide, on_delete = models.CASCADE)

	def __str__(self):

		return str(self.user.full_name) + '-' + 'Bookings'



class Review(models.Model):
	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			= 	models.ForeignKey(Guide, on_delete = models.CASCADE)
	text 			= 	models.CharField(max_length = 4000, blank = True)
	rating 			= 	models.BooleanField(blank = True, default = False)

	def __str__(self):

		return str(self.user.full_name) + '-' + 'review'

