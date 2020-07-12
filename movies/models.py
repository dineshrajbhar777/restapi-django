from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name= models.CharField(max_length= 200)

    class Meta:
        verbose_name= "Genre"
        verbose_name_plural= "Genres"
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    name=       models.CharField(max_length= 500)
    director=   models.CharField(max_length= 200)
    popularity= models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    imdb_score= models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    genre=      models.ManyToManyField(Genre)

    class Meta:
        verbose_name= "Movie"
        verbose_name_plural= "Movies"
    
    def __str__(self):
        return self.name
    
    @property
    def owner(self):
        return self.user
    