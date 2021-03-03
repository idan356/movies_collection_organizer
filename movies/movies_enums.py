from enum import Enum


class TrackTypes(str, Enum):
    """Possible tracks of video files"""
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLES = "subtitles"


class VideoResolutions(Enum):
    """Common video resolutions"""
    UNKNOWN = -1
    HD = 1280
    FULL_HD = 1920
    QUAD_HD_2K = 2560
    ULTRA_HD_4K = 3840
    ULTRA_HD_8K = 7680


class SubtitleExtensions(Enum):
    """Common subtitles files extensions"""
    SRT = "srt"
    SUB = "sub"


class MovieExtensions(Enum):
    """Common movies files extensions"""
    MKV = "mkv"
    MP4 = "mp4"
