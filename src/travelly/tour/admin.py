from django.contrib import admin

from .models import (

	Tour,
	Book,
	Review,

	)



admin.site.register(Tour)
admin.site.register(Book)
admin.site.register(Review)