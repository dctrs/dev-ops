def serialize_genre_list(genres):
    return [{'id': genre.id, 'title': genre.title} for genre in genres]

def serialize_movie(movie):
    return {
        'id': movie.id,
        'title': movie.title,
        'description': movie.description,
        'poster': movie.poster.url if movie.poster else None,
        'bg_picture': movie.bg_picture.url if movie.bg_picture else None,
        'release_year': movie.release_year,
        'mpa_rating': movie.mpa_rating,
        'imdb_rating': movie.imdb_rating,
        'duration': movie.duration,
        'genres': [{'id': genre.id, 'title': genre.title} for genre in movie.genres.all()],
        'directors': [{'id': director.id, 'name': director.first_name + ' ' + director.last_name} for director in movie.directors.all()],
        'writers': [{'id': writer.id, 'name': writer.first_name + ' ' + writer.last_name} for writer in movie.writers.all()],
        'stars': [{'id': star.id, 'name': star.first_name + ' ' + star.last_name} for star in movie.stars.all()],
    }

def serialize_movie_list(movies):
    return [serialize_movie(movie) for movie in movies]