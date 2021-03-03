from movies.tracks.track import Track


class SubtitleTrack(Track):

    def __init__(self, track_info: dict):
        super().__init__(track_info)

    def get_language(self) -> str:
        return self._get_property('language')

    def is_default(self) -> str:
        return self._get_property('default_track')

    def is_enabled(self) -> str:
        return self._get_property('enabled_track')

    def is_forced(self) -> str:
        return self._get_property('forced_track')
