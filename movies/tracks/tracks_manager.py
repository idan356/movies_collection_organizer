from movies.tracks.subtitle_track import SubtitleTrack
from movies.tracks.audio_track import AudioTrack
from movies.tracks.video_track import VideoTrack
from movies.tracks.track import Track
from movies.movies_enums import TrackTypes
from system_utils import SystemUtils
from typing import List, Union
from pathlib import Path
import json


class TracksManager(object):

    GET_MOVIE_INFO_COMMAND: str = "mkvmerge -F json --identify"

    def __init__(self, movie_path: Path):
        self.movie_path: Path = movie_path
        self.tracks_info: List[dict] = []
        self.info: Union[None, dict] = None
        self.video_tracks: List[VideoTrack] = []
        self.audio_tracks: List[AudioTrack] = []
        self.subtitle_tracks: List[SubtitleTrack] = []

    def analyze(self) -> None:
        self._get_tracks_info()
        for track in self.tracks_info:
            track_type: str = track['type']
            if track_type == TrackTypes.VIDEO.value:
                self.video_tracks.append(VideoTrack(track))
            elif track_type == TrackTypes.AUDIO.value:
                self.audio_tracks.append(AudioTrack(track))
            elif track_type == TrackTypes.SUBTITLES.value:
                self.subtitle_tracks.append(SubtitleTrack(track))

    def _get_tracks_info(self):
        command: str = f'{self.GET_MOVIE_INFO_COMMAND} \"{self.movie_path}\"'
        info: str = SystemUtils.run_command(command)
        self.info = json.loads(info)
        self.tracks_info = self.info["tracks"]

    def get_all_tracks(self) -> List[Track]:
        output: List[Track] = []
        output.extend(self.video_tracks)
        output.extend(self.audio_tracks)
        output.extend(self.subtitle_tracks)
        return output
