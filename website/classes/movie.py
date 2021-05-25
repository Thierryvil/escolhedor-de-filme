""" Movie Class File """

class Movie:
    """ Movie class """
    def __init__(self, movie_json):
        self.movie_json = movie_json

    def title(self):
        """ return movie title """
        return self.movie_json['title']

    def date(self):
        """ Return movie date yyyy-mm-day """
        return self.movie_json['release_date']

    def note(self):
        """ Return movie note 0.0 - 10 """
        return self.movie_json['vote_average']

    def poster(self):
        """ Return movie poster img PNG """
        return f'https://image.tmdb.org/t/p/w342{self.movie_json["poster_path"]}'

    def overview(self):
        """ Return movie overview """
        return self.movie_json['overview']

    def to_json(self):
        """ Return movie data"""
        return {
            'title': self.title(),
            'date': self.date(),
            'note': self.note(),
            'poster': self.poster(),
            'overview': self.overview()
        }