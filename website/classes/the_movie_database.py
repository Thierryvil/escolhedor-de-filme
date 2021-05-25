""" The Movie Database class file """
import json
from random import randrange
import requests

class TheMovieDataBase:
    """ TheMovieDataBase Class """

    BASE_URL = 'https://api.themoviedb.org/3'
    GENRE_ENDPOINT = '/genre/movie/list?'
    DISCOVER_ENDPOINT = '/discover/movie?'

    _api_key = None
    _language = 'pt-BR'

    def __init__(self, api_key, language='pt-BR'):
        self._api_key = api_key
        self._language = language

    @staticmethod
    def response_200_or_error(target_url):
        """ Get responde from request """
        if target_url.status_code == 200:
            return target_url.text
        raise Exception(f'Invalid Requests: {target_url.status_code}:{target_url.text}')

    def get_genre_list(self):
        """" Get genre list from api """
        target = f'{self.BASE_URL}{self.GENRE_ENDPOINT}api_key={self._api_key}&language={self._language}'
        target_data = self.response_200_or_error(requests.get(target))

        return json.loads(target_data)['genres']

    def get_movie(self, genre):
        """ Get random movie from api """
        discover_endpoint = f'{self.BASE_URL}{self.DISCOVER_ENDPOINT}api_key={self._api_key}&language={self._language}&vote_count.gte=1000&include_adult=false&with_genres={genre}'
        target_data = self.response_200_or_error(requests.get(discover_endpoint))
        movie_data = json.loads(target_data)
        page = randrange(1, movie_data['total_pages'])

        discover_endpoint = discover_endpoint + f'&page={page}'
        target_data = self.response_200_or_error(requests.get(discover_endpoint))
        movie_data = json.loads(target_data)
        return movie_data['results'][randrange(1, len(movie_data['results']))]
