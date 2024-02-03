from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import  Genre, Movie
from .serializers import *
from .utils import paginate_queryset

def genre_list(request):
    genres = Genre.objects.all()
    return JsonResponse(serialize_genre_list(genres), safe=False)

def movie_list(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 2))
    genre = request.GET.get('genre')
    src = request.GET.get('src')
    movies = Movie.objects.all()
    if genre:
        movies = movies.filter(genres = genre)
        if not movies.exists():
            return JsonResponse({'error': ['genre__invalid']}, status=404)
    if src:
        movies = movies.filter(title__startswith = src)
        if not movies.exists() or len(src) < 2:
            return JsonResponse({'error': ['src__invalid']}, status=404)
    total_movies = movies.count()
    total_pages = (total_movies + page_size - 1) // page_size
    if page > total_pages or page < 1:
        return JsonResponse({'error': ['page__invalid']}, status=400)
    movies_paginated = paginate_queryset(movies, page, page_size)

    data = {
        'pages': total_pages,
        'total': total_movies,
        'results': serialize_movie_list(movies_paginated)
    }

    return JsonResponse(data)

def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return JsonResponse(serialize_movie(movie))
    except Movie.DoesNotExist:
        return JsonResponse({'error': ["movie__not_found"]}, status=404)