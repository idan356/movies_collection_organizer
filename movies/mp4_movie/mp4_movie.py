from movies.movies_enums import SubtitleExtensions
from movies.movie import Movie
from pathlib import Path
from typing import Union


class MP4Movie(Movie):

    def __init__(self, movie_path: Path):
        super().__init__(movie_path)
        self.subtitles: Union[None, Path] = None

    def analyze(self) -> None:
        """Analyze current movie"""
        super().analyze()
        self._analyze_subtitles()

    def _analyze_subtitles(self) -> None:
        """Find subtitles in the same folder"""
        for subtitle_extension in SubtitleExtensions:
            subtitle_path: Path = self.path.with_suffix(f'.{subtitle_extension.value}')
            if subtitle_path.exists():
                self.subtitles = subtitle_path
                break

    def has_subtitles(self, language: str) -> bool:
        """Return true if current movie has specific subtitles"""
        return self.subtitles is not None and language in self.subtitles.name
