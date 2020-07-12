import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Movie, Genre

class Command(BaseCommand):
    #  dump movies data to db
    def handle(self, *args, **options):
        filepath= settings.BASE_DIR + "/imdb.json"
        with open(filepath, "r") as f:
            rdata= f.read()
            data= json.loads(rdata)
            
            m= {}
            c= 0
            for d in data:
                #  get movie details
                m["name"]=         d.get("name")
                m["director"]=     d.get("director")
                m["popularity"]=   d.get("99popularity")
                m["imdb_score"]=   d.get("imdb_score")
                movie, created=    Movie.objects.get_or_create(**m)
                
                #  get genre
                genre_list= d.get("genre")
                for g in genre_list:
                    g= g.strip()
                    genre, created= Genre.objects.get_or_create(name= g)
                    movie.genre.add(genre)
                movie.save()
                c+= 1
                print("[%4s] %s" % (c, movie))

                
