from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def index(request):
    # SELECT  FROM movies_movie
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    return HttpResponse(int(movie_id))