from movies.movies_exceptions import NoVideoTracksException
from movies.tracks.tracks_manager import TracksManager
from movies.tracks.video_track import VideoTrack
from movies.tracks.track import Track
from typing import List, Tuple
from pathlib import Path
import PTN


class Movie(object):

    def __init__(self, movie_path: Path):
        self.path: Path = movie_path
        self.name_parser: dict = {}
        self.tracks_manager: TracksManager = TracksManager(self.path)
        self.analyze()

    def analyze(self) -> None:
        """Analyze current movie"""
        self.name_parser: dict = PTN.parse(self.path.name)
        self.tracks_manager.analyze()

    def has_subtitles(self, language: str) -> bool:
        """Return true if current movie has specific subtitles"""
        for subtitle in self.tracks_manager.subtitle_tracks:
            if subtitle.get_language() == language:
                return True
        return False

    def get_title(self) -> str:
        """Get movie's title as mentioned in the movie file name"""
        return self._get_value_from_name("title")

    def get_year(self) -> str:
        """Get movie's release date as mentioned in the movie file name"""
        return self._get_value_from_name("year")

    def get_container(self) -> str:
        """Get movie's container type as mentioned in the movie file name"""
        return self._get_value_from_name("container")

    def get_codec(self) -> str:
        """Get movie's codec as mentioned in the movie file name"""
        return self._get_value_from_name("codec")

    def get_quality(self) -> str:
        """Get movie's quality as mentioned in the movie file name"""
        return self._get_value_from_name("quality")

    def _get_value_from_name(self, value_name: str) -> str:
        """Extract specific value from file's name"""
        if value_name not in self.name_parser:
            raise ValueError(f'{value_name} does not exists')
        return self.name_parser.get(value_name)

    def get_file_name(self) -> str:
        """Get video file name"""
        return self.path.name

    def get_file_path(self) -> Path:
        """Get video file path"""
        return self.path

    def get_folder(self) -> Path:
        """Get parent folder path"""
        return self.path.parent

    def get_all_resolutions(self) -> List[Tuple[int, int]]:
        """Get all resolutions streams of current movie"""
        video_tracks: List[VideoTrack] = self.tracks_manager.video_tracks
        resolutions: List[Tuple[int, int]] = []
        for video_track in video_tracks:
            resolutions.append(video_track.get_resolution())
        return resolutions

    def get_max_resolution(self) -> Tuple[int, int]:
        """Get max resolution stream"""
        all_resolutions: List[Tuple[int, int]] = self.get_all_resolutions()
        if all_resolutions:
            return sorted(all_resolutions)[0]
        raise NoVideoTracksException

    def get_tracks(self) -> List[Track]:
        """Get all tracks of current movie"""
        return self.tracks_manager.get_all_tracks()

    def __str__(self) -> str:
        return self._get_str()

    def __repr__(self) -> str:
        return self._get_str()

    def _get_str(self) -> str:
        title: str = self.get_title()
        year: str = self.get_year()
        if title and year:
            return f'{title} ({year})'
        return self.path.name
