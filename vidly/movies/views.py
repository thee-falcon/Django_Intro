from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def index(request):
    # SELECT  FROM movies_movie
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
    # return HttpResponse(movie_id)

