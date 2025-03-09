from django.contrib import admin
from .models import Letter, Package

admin.site.register(Letter)
admin.site.register(Package)