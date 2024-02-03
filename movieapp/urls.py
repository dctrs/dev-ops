from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie-list'),
    path('genres/', views.genre_list, name='genre-list'),
    path('movies/<int:movie_id>/', views.get_movie, name='get-movie'),
]
