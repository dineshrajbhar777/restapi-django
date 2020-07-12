from django.contrib import admin

from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display=  ["name", "director", "popularity", "imdb_score"]
    list_filter=   ["genre"]
    search_fields= ["name", "director"]
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
