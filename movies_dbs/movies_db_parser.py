from movies_dbs.movie_db import MovieDB
from abc import ABC, abstractmethod
from movies.movie import Movie


class MoviesDBParser(ABC):

    @abstractmethod
    def get_movie_db(self, movie: Movie) -> MovieDB:
        """Get the movie's DB object"""
        pass
