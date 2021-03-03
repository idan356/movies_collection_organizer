from enum import Enum


class ExtrasFolderNames(Enum):
    """
    List of extras folders names supported by Plex
    https://support.plex.tv/articles/local-files-for-trailers-and-extras/
    """
    BEHIND_THE_SCENE = "Behind The Scenes"
    DELETED_SCENES = "Deleted Scenes"
    FEATURETTES = "Featurettes"
    INTERVIEWS = "Interviews"
    SCENES = "Scenes"
    SHORTS = "Shorts"
    TRAILERS = "Trailers"
    OTHER = "Other"


class SupportedDBs(Enum):
    """Supported PLEX Movies DBs"""
    TMDB = "tmdb"
    IMDB = "imdb"
