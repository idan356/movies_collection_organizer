from movies.tracks.track import Track
from typing import Tuple, List


class VideoTrack(Track):

    def __init__(self, track_info: dict):
        super().__init__(track_info)

    def get_resolution(self) -> Tuple[int, int]:
        pixel_dimensions: str = self._get_property("pixel_dimensions").lower()
        if "x" in pixel_dimensions:
            dimensions: List[str] = pixel_dimensions.split("x")
            return int(dimensions[0]), int(dimensions[1])
        return -1, -1
