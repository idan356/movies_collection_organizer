from tmdb3 import set_key, searchMovie, set_cache, Movie as TMBDMovie
from movies_dbs.movies_db_parser import MoviesDBParser
from movies_dbs.tmdb.tmdb_movie import TMDBMovie
from tmdb3.locales import Locale
from movies.movie import Movie
from typing import Union


class TMDBParser(MoviesDBParser):

    def __init__(self, api_key: str, locale: Locale, fallback_locale: Locale = None):
        super().__init__()
        self.api_key: str = api_key
        self.locale: Locale = locale
        self.fallback_locale: Locale = fallback_locale
        set_key(api_key)
        set_cache('null')

    def get_movie_db(self, movie: Movie) -> Union[TMDBMovie, None]:
        """Get the movie's DB object"""
        year: str = movie.get_year()
        title: str = movie.get_title()
        main_locale_movie = self._get_first_movie_result(title, year, self.locale)
        fallback_locale_movie = None
        if self.fallback_locale and (not main_locale_movie or not main_locale_movie.youtube_trailers):
            fallback_locale_movie = self._get_first_movie_result(title, year, self.fallback_locale)
        return TMDBMovie(main_locale_movie, fallback_locale_movie)

    def _get_first_movie_result(self, title: str, year: str, locale: Locale) -> Union[TMBDMovie, None]:
        """Search the given movie in the DB and use the first result if exists"""
        results = searchMovie(title, year=year, locale=locale)
        return results[0] if results else None
