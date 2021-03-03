from movies_dbs.movie_db import MovieDB
from typing import Union
from tmdb3 import Movie


class TMDBMovie(MovieDB):

    def __init__(self, movie: Movie, fallback_movie: Movie = None):
        super().__init__()
        self.movie: Movie = movie
        self.fallback_movie: Union[Movie, None] = fallback_movie
        self._trailer: Union[str, None] = None

    def get_title(self) -> str:
        """Get movie title"""
        return self.movie.title

    def get_year(self) -> str:
        """Get movie release year"""
        return str(self.movie.releasedate.year)

    def get_movie_id(self) -> str:
        """Get movie's database unique ID"""
        return self.movie.id

    def get_youtube_trailer_url(self) -> str:
        """Get movie's trailer URL from the DB"""
        if self._trailer is None:
            self._find_trailer_url()
        return self._trailer

    def _find_trailer_url(self) -> None:
        """Find the movie's trailer URL"""
        if self.movie.youtube_trailers:
            self._trailer = self.movie.youtube_trailers[0].geturl()
        elif self.fallback_movie is not None and len(self.fallback_movie.youtube_trailers) > 0:
            self._trailer = self.fallback_movie.youtube_trailers[0].geturl()
        else:
            self._trailer = ""
