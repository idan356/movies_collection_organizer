from movies.movie import Movie
from pathlib import Path


class MKVMovie(Movie):

    def __init__(self, movie_path: Path):
        super().__init__(movie_path)
