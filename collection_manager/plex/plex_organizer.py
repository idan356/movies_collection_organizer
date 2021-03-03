from collection_manager.analyzed_movie import AnalyzedMovie
from collection_manager.organizer import Organizer
from youtube_utils import YoutubeUtils
from system_utils import SystemUtils
from pathlib import Path
from typing import List
import logging


class PlexOrganizer(Organizer):

    def __init__(self, db_name: str):
        super().__init__()
        self.db_name: str = db_name
        self._logger = logging.getLogger()

    def organize(self, movies: List[AnalyzedMovie]) -> None:
        """Organize a given list of analyzed movies based on PLEX conventions"""
        for analyzed_movie in movies:
            self._organize_movie(analyzed_movie)

    def _organize_movie(self, analyzed_movie: AnalyzedMovie) -> None:
        """Organize a single movie according to PLEX conventions"""
        self._logger.info(f'\nOrganizing {analyzed_movie.movie.get_file_name()}')
        self._update_folder_name(analyzed_movie)
        self._update_movie_file_name(analyzed_movie)
        self._handle_trailer(analyzed_movie)

    def _update_folder_name(self, analyzed_movie: AnalyzedMovie) -> None:
        """Update folder name with necessary information"""
        movie_path: Path = analyzed_movie.movie.get_file_path()
        new_folder_name: str = self._generate_new_folder_name(analyzed_movie)
        new_movie_path: Path = movie_path.parent / new_folder_name / movie_path.name
        self._update_movie_path(analyzed_movie, movie_path, new_movie_path)

    def _generate_new_folder_name(self, analyzed_movie: AnalyzedMovie) -> str:
        """Generate the folder name according to PLEX conventions"""
        title: str = analyzed_movie.movie_db.get_title()
        self._logger.info(f"Locale movie title: {title}")
        year: str = analyzed_movie.movie_db.get_year()
        self._logger.info(f"Release year: {year}")
        folder_name: str = self._append_movie_id_to_name(f'{title} ({year})', analyzed_movie)
        self._logger.info(f"Folder name: {folder_name}")
        return folder_name

    def _update_movie_file_name(self, analyzed_movie: AnalyzedMovie) -> None:
        """Update movie file name with the necessary information according to PLEX conventions"""
        movie_path: Path = analyzed_movie.movie.get_file_path()
        new_movie_name: str = self._append_movie_id_to_name(movie_path.stem, analyzed_movie)
        new_movie_path: Path = movie_path.parent / f'{new_movie_name}{movie_path.suffix}'
        self._update_movie_path(analyzed_movie, movie_path, new_movie_path)

    def _update_movie_path(self, analyzed_movie: AnalyzedMovie, movie_path: Path, new_movie_path: Path) -> None:
        """Update a single analyzed movie file path"""
        new_sanitized_movie_path: Path = SystemUtils.sanitize_filepath(new_movie_path)
        new_sanitized_movie_path.parent.mkdir(parents=True, exist_ok=True)
        movie_path.rename(new_sanitized_movie_path)
        analyzed_movie.movie.path = new_sanitized_movie_path

    def _append_movie_id_to_name(self, name: str, analyzed_movie: AnalyzedMovie) -> str:
        """Append the movie ID to it current name"""
        movie_id: str = analyzed_movie.movie_db.get_movie_id()
        if movie_id:
            name = f'{name} {{{self.db_name}-{movie_id}}}'
        return name

    def _handle_trailer(self, analyzed_movie: AnalyzedMovie) -> None:
        """Download movie trailer if not exists already"""
        if analyzed_movie.should_download_trailer():
            self._download_trailer(analyzed_movie)

    def _download_trailer(self, analyzed_movie: AnalyzedMovie) -> None:
        """Download the highest resolution trailer from Youtube"""
        trailer_url: str = analyzed_movie.get_youtube_trailer_url()
        if trailer_url:
            self._logger.info(f"Downloading trailer: {trailer_url}")
            trailer_dest: Path = analyzed_movie.get_trailer_folder_path()
            trailer_name: str = analyzed_movie.get_trailer_file_name()
            YoutubeUtils.download_highest_resolution(trailer_url, trailer_dest, trailer_name)
            self._logger.info("Trailer downloaded successfully")
