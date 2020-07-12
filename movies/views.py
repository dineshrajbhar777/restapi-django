from django.db.models import Q
from rest_framework import viewsets

from .models import Genre, Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    allowed_methods = ['GET']
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        
        q = self.request.GET.get("q", None)
        if q is not None:
            queryset = queryset.filter(
                Q(name__icontains= q) | Q(director__icontains= q) | Q(genre__name__icontains= q)
            )
        else:
            name = self.request.GET.get("name", None)
            if name is not None:
                queryset = queryset.filter(name__icontains= name)
                
            director = self.request.query_params.get('director', None)
            if director is not None:
                queryset = queryset.filter(director__icontains= director)
				
            genre = self.request.query_params.get('genre', None)
            if genre is not None:
                queryset = queryset.filter(genre__name__icontains= genre)        
        return queryset
    