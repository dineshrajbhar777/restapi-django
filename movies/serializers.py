from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('genre',)

class MovieSerializer(serializers.ModelSerializer):
    genre= GenreSerializer(read_only= True, many= True)
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = (
            'name',
            'director',
            'popularity',
            'imdb_score',
            'genre',
        )
