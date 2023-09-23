from django.contrib import admin
from .models import *

# Register your models here.

class studinfoDisplay(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','dob','mobile','address']

admin.site.register(studinfo,studinfoDisplay)