from django.contrib import admin

from .models import (

	Guide,
	Review

	)


admin.site.register(Guide)
admin.site.register(Review)