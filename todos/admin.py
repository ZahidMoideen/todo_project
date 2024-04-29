# admin.py
from django.contrib import admin
from .models import Todo,Project


admin.site.register(Project)
admin.site.register(Todo)

