from django.contrib import admin
from django.contrib.auth.models import User
from .models import Neighborhood, Profile, Business, Notice

#registering the models
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Notice)