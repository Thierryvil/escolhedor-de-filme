""" View File, routes """
from flask import Blueprint, render_template, request
from website import API_KEY
from .utils import GENRE_ID
from .classes.movie import Movie
from .classes.the_movie_database import TheMovieDataBase

views = Blueprint('views', __name__)
movie = TheMovieDataBase(API_KEY)


@views.route('/')
def home():
    """ Render index template, initial page """
    genres = [genre['name'] for genre in movie.get_genre_list()]

    return render_template('index.html', genres=genres)


@views.route('/random_film', methods=['POST'])
def get_post_javascript_data():
    """ Get data from frontend and return random movie """
    genre_index = int(request.form['genre_index'])
    genre = GENRE_ID[genre_index]
    random_movie = Movie(movie.get_movie(genre))

    return random_movie.to_json()
