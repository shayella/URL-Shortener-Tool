from django.contrib import admin

# Register your models here.
from .models import ShortenURL

admin.site.register(ShortenURL)
