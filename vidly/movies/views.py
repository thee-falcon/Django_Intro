from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def index(request):
    # SELECT  FROM movies_movie
    movies = Movies.objects.all()
    output = ', '.join([movie.title for movie in movies])
    return HttpResponse(output)