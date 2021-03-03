from pathlib import Path
import pytube as pytube


class YoutubeUtils(object):

    @classmethod
    def download_highest_resolution(cls, url: str, output_folder: Path, file_name: str) -> None:
        """Download the highest resolution stream of a given Youtube video URL"""
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(str(output_folder), file_name)
