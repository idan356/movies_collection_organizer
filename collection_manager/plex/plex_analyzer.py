from collection_manager.plex.plex_analyzed_movie import PlexAnalyzedMovie
from collection_manager.plex.plex_enums import ExtrasFolderNames
from movies_dbs.movies_db_parser import MoviesDBParser
from collection_manager.analyzer import Analyzer
from movies.movies_factory import MoviesFactory
from movies.movies_enums import MovieExtensions
from movies_dbs.movie_db import MovieDB
from movies.movie import Movie
from pathlib import Path
from typing import List
import os


class PlexAnalyzer(Analyzer):

    def __init__(self, db_parser: MoviesDBParser):
        super().__init__()
        self.db_parser: MoviesDBParser = db_parser

    def analyze(self, movies_collection: Path) -> None:
        """Analyze a movies collection path according to PLEX conventions"""
        for root, dirs, files in os.walk(movies_collection):
            self._analyze_folder(root)

    def _analyze_folder(self, root: str) -> None:
        """Analyze a single folder with video files according to PLEX conventions"""
        if self._should_analyze_folder(root):
            video_files: List[Path] = self._get_video_files(Path(root))
            for video_file in video_files:
                self._analyze_single_video_file(video_file)

    def _should_analyze_folder(self, root: str) -> bool:
        """False if the given folder name equals to one of PLEX known folders (e.g "trailers"), true otherwise"""
        for extra_folder_name in ExtrasFolderNames:
            if root.title() == extra_folder_name.value:
                return False
        return True

    def _get_video_files(self, folder: Path) -> List[Path]:
        """Get all video files to analyze"""
        all_video_files: List[Path] = []
        for ext in MovieExtensions:
            for video in folder.glob(f"*.{ext.value}"):
                if "trailer" not in video.name.lower():
                    all_video_files.append(video)
        return all_video_files

    def _analyze_single_video_file(self, video_file: Path) -> None:
        """Analyze single video file"""
        movie: Movie = MoviesFactory.get_movie(video_file)
        movie_db: MovieDB = self.db_parser.get_movie_db(movie)
        analyzed_movie: PlexAnalyzedMovie = PlexAnalyzedMovie(movie, movie_db)
        self.analyzed_movies.append(analyzed_movie)
