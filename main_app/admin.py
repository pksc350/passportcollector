from django.contrib import admin

from .models import Stamp, Weather, Attraction

# Register your models here.
admin.site.register(Stamp)

admin.site.register(Weather)

admin.site.register(Attraction)