""" Tests File"""
import requests
from website import API_KEY

def test_api_key_is_not_null():
    """ Get API_KEY value and compare """
    assert API_KEY != None

def test_request_api_key():
    """ Test a request with api_key value """
    assert requests.get(f'https://api.themoviedb.org/3/movie/76341?api_key={API_KEY}').status_code == 200
