from django.db import models

class Genre(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    TYPES = [
        ('director', 'Director'),
        ('writer', 'Writer'),
        ('actor', 'Actor'),
    ]
    type = models.CharField(max_length = 10, choices = TYPES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()
    imdb_rating = models.FloatField()
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Person, related_name='directed_movies')
    writers = models.ManyToManyField(Person, related_name='written_movies')
    stars = models.ManyToManyField(Person, related_name='starred_movies')
    MPA_RATING = [
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    ]
    mpa_rating = models.CharField(max_length=5, choices = MPA_RATING)
    poster = models.ImageField(upload_to='posters/')
    bg_picture = models.ImageField(upload_to='bg_pictures/')

    def __str__(self):
        return self.title