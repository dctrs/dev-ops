from django.contrib import admin
from .models import Genre, Person, Movie

admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Movie)