import logging


class Track(object):

    def __init__(self, track_info: dict):
        self.track_info: dict = track_info
        self.properties: dict = self.track_info["properties"]
        self.logger = logging.getLogger()

    def _get_property(self, property_name: str) -> str:
        if property_name not in self.properties:
            raise ValueError(f'{property_name} does not exists')
        return self.properties[property_name]

    def _get_info(self, info_name: str) -> str:
        if info_name not in self.track_info:
            raise ValueError(f'{info_name} does not exists')
        return self.track_info[info_name]

    def get_codec(self):
        return self._get_info("codec")

    def get_id(self):
        return self._get_info("id")

    def get_type(self):
        return self._get_info("type")
