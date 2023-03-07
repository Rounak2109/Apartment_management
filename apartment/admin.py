from django.contrib import admin
from .models import Apartment, FlatTypes
# Register your models here.

admin.site.register([Apartment, FlatTypes])