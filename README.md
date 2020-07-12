RESTful API for movies(something similar to IMDB)

Environment: Django Rest Framework, sqlite

1) Create virtual envitronment
    virtualenv env

2) Activate virtual envitronment
    source env/bin/activate

3) Install packages from reuqirements.txt
    pip install -r reuqirements.txt

4) cd to ~/restapi and run below commands
    python manage.py makemigrations
    python manage.py migrate

5) create superuser
    python manage.py createsuperuser
    (add username, email, password)

6) dump all movies datat to db from imdb.json file
    python manage.py dump_movies

7) start server 
    python manage.py runserver
  Output:
    Django version 3.0.8, using settings 'restapi.settings'                                       Starting development server at http://127.0.0.1:8000/                                         Quit the server with CTRL-BREAK. 

-----------------------
API request sample url
-----------------------

  BASE URL:
    http://127.0.0.1:8000/api/v1/movie/


  SEARCH BY (name OR director OR genre)
    http://127.0.0.1:8000/api/v1/movie/?q=superman

  SEARCH BY (name)
    http://127.0.0.1:8000/api/v1/movie/?name=god

  SEARCH BY (director)
    http://127.0.0.1:8000/api/v1/movie/?director=john

  SEARCH BY (genre)
    http://127.0.0.1:8000/api/v1/movie/?genre=sci

  SEARCH BY (name AND genre)
    http://127.0.0.1:8000/api/v1/movie/?name=Psycho&genre=horror


----------
ADMIN url
----------
  http://127.0.0.1:8000/admin
  (enter creted superuser username and password)

