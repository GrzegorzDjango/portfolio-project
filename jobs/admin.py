from django.contrib import admin
from .models import Job


#we want to show jobs in admin page
admin.site.register(Job)
