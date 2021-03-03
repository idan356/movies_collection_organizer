from collection_manager.plex.plex_enums import ExtrasFolderNames
from collection_manager.analyzed_movie import AnalyzedMovie
from movies_dbs.movie_db import MovieDB
from movies.movie import Movie
from typing import List
from pathlib import Path


class PlexAnalyzedMovie(AnalyzedMovie):

    def __init__(self, movie: Movie, movie_db: MovieDB):
        super().__init__(movie, movie_db)

    def is_the_only_movie_in_folder(self) -> bool:
        """True if current movie is the only video file in the folder, false otherwise"""
        pass

    def get_existing_trailers(self) -> List[Path]:
        """Get all movie's trailer files if exists"""
        if self.is_the_only_movie_in_folder():
            if self.get_trailer_folder_path().exists():
                return list(self.get_trailer_folder_path().iterdir())
        return list(self.movie.get_folder().glob(f'*{self.get_trailer_file_name()}*'))

    def get_trailer_folder_path(self) -> Path:
        """Return the trailer folder path according to PLEX conventions"""
        return self.movie.get_folder() / ExtrasFolderNames.TRAILERS.value

    def get_trailer_file_name(self) -> str:
        """Return trailer file name according to PLEX conventions"""
        return "trailer"
