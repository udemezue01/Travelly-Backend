from django.db import models

from django.conf import settings



TOUR_TYPE = (

	('IND', 'Individual'),

	('GRP', 'Group')

	)


SERVICE_TYPE = (

	('D', 'Driving'),

	('F', 'Flying'),

	('W', 'Walking'),

	('C', 'Cycling'),

	('R', 'Running'),

	('B', 'Boating'),

	('O', 'Other'),

	)





class Tour(models.Model):

	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	name 			= 	models.CharField(max_length = 5000, blank = True, null = True)

	description 	=  	models.CharField(max_length = 5000, blank = True, null = True)
	location		= 	models.CharField(max_length = 4000) 

	service_type 	= 	models.CharField(max_length = 3000, choices = SERVICE_TYPE, blank = True, null = True)
	tour_type 		= 	models.CharField(max_length = 3000, choices = TOUR_TYPE, blank = True, null = True)

	language 		=  	models.CharField(max_length = 400, blank = True, null = True)
	price 			=	models.IntegerField()
	time_available	= 	models.DateTimeField()

	featured_image	= 	models.FileField(blank = True, null = True)
	gallery_images 	= 	models.FileField(blank = True, null = True)
	video			=  	models.FileField(blank =True, null = True)

	created_at		=	models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):

		return str(self.user.full_name) + '-' + self.location


class Book(models.Model):

	user 			=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			=  models.ForeignKey(Tour, on_delete = models.CASCADE, blank=True, null = True)


	def __str__(self):

		return str(self.user.full_name) + '-' + 'Bookings'






class Review(models.Model):
	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			= 	models.ForeignKey(Tour, on_delete = models.CASCADE)
	text 			= 	models.CharField(max_length = 4000, blank = True)
	rating 			= 	models.BooleanField(blank = True, default = False)

	def __str__(self):

		return str(self.user.full_name) + '-' + 'review'

