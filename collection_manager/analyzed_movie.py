from movies_dbs.movie_db import MovieDB
from abc import ABC, abstractmethod
from movies.movie import Movie
from pathlib import Path
from typing import List


class AnalyzedMovie(ABC):

    def __init__(self, movie: Movie, movie_db: MovieDB):
        self.movie: Movie = movie
        self.movie_db: MovieDB = movie_db

    @abstractmethod
    def is_the_only_movie_in_folder(self) -> bool:
        """True if current movie is the only video file in the folder, false otherwise"""
        pass

    def should_download_trailer(self) -> bool:
        """True if no trailer exists, false otherwise"""
        return not self.already_have_trailer()

    def already_have_trailer(self) -> bool:
        """True if movie already have trailer, false otherwise"""
        return len(self.get_existing_trailers()) > 0

    @abstractmethod
    def get_existing_trailers(self) -> List[Path]:
        """Get all movie's trailer files if exists"""
        pass

    def get_youtube_trailer_url(self) -> str:
        """Return movie's trailer URL"""
        return self.movie_db.get_youtube_trailer_url()

    @abstractmethod
    def get_trailer_folder_path(self) -> Path:
        """Return the trailer folder path"""
        pass

    @abstractmethod
    def get_trailer_file_name(self) -> str:
        """Return trailer file name"""
        pass
