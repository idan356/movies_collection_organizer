from movies.tracks.track import Track


class AudioTrack(Track):

    def __init__(self, track_info: dict):
        super().__init__(track_info)

    def get_language(self) -> str:
        return self._get_property("language")
