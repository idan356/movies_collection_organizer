from collection_manager.analyzed_movie import AnalyzedMovie
from collection_manager.organizer import Organizer
from collection_manager.analyzer import Analyzer
from movies.movies_enums import VideoResolutions
from movies.movie import Movie
from typing import List, Tuple
from pathlib import Path


class CollectionManager(object):

    def __init__(self, movies_collection: Path, analyzer: Analyzer, organizer: Organizer):
        self.movies_collection: Path = movies_collection
        self.analyzer: Analyzer = analyzer
        self.organizer: Organizer = organizer

    def analyze(self) -> None:
        """Analyze collection"""
        self.analyzer.analyze(self.movies_collection)

    def organize(self) -> None:
        "Organize collection"
        self.organizer.organize(self.get_analyzed_movies())

    def get_analyzed_movies(self) -> List[AnalyzedMovie]:
        """Get analyzed movies"""
        return self.analyzer.get_analyzed_movies()

    def get_trailers(self) -> List[Tuple[str, str]]:
        """Get all Youtube trailers URLs"""
        output: List[Tuple[str, str]] = []
        all_movies: List[AnalyzedMovie] = self.get_analyzed_movies()
        for analyzed_movie in all_movies:
            trailer_url: str = analyzed_movie.movie_db.get_youtube_trailer_url()
            output.append((analyzed_movie.movie_db.get_title(), trailer_url))
        return output

    def get_movies_without_specific_subtitles(self, languages: List[str]) -> List[AnalyzedMovie]:
        """Find all videos that missing specific subtitles"""
        output: List[AnalyzedMovie] = []
        all_movies: List[AnalyzedMovie] = self.analyzer.get_analyzed_movies()
        for analyzed_movie in all_movies:
            if not self._has_all_subtitles_languages(analyzed_movie.movie, languages):
                output.append(analyzed_movie)
        return output

    def _has_all_subtitles_languages(self, movie: Movie, languages: List[str]) -> bool:
        """Returns true if the given movie has a specific subset of subtitles, false otherwise"""
        for language in languages:
            if not movie.has_subtitles(language):
                return False
        return True

    def get_low_resolution_movies(self, min_resolution: VideoResolutions) -> List[AnalyzedMovie]:
        """Get all movies with lower resolution that the given minimum resolution"""
        output: List[AnalyzedMovie] = []
        all_movies: List[AnalyzedMovie] = self.analyzer.get_analyzed_movies()
        for analyzed_movie in all_movies:
            max_resolution: Tuple[int, int] = analyzed_movie.movie.get_max_resolution()
            if max_resolution[0] < min_resolution.value:
                output.append(analyzed_movie)
        return output
