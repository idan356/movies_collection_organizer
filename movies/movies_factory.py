from movies.mkv_movie.mkv_movie import MKVMovie
from movies.mp4_movie.mp4_movie import MP4Movie
from movies.movies_enums import MovieExtensions
from movies.movie import Movie
from pathlib import Path


class MoviesFactory(object):

    @staticmethod
    def get_movie(movie_path: Path) -> Movie:
        """Create a new video object based on it type"""
        movie_suffix: str = movie_path.suffix[1:].lower()
        if movie_suffix == MovieExtensions.MKV.value:
            return MKVMovie(movie_path)
        elif movie_suffix == MovieExtensions.MP4.value:
            return MP4Movie(movie_path)
