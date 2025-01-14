from django.contrib import admin
from .models import Movies, Genre

# Register your models here, and customize the tables.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate', 'date_created', 'id')

admin.site.register(Movies, MovieAdmin)
admin.site.register(Genre, GenreAdmin)