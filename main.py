from collection_manager.collection_manager import CollectionManager
from collection_manager.plex.plex_organizer import PlexOrganizer
from collection_manager.plex.plex_analyzer import PlexAnalyzer
from collection_manager.plex.plex_enums import SupportedDBs
from movies_dbs.tmdb.tmdb_parser import TMDBParser
from tmdb3.locales import Locale, get_locale
from configurations import Configurations
from pathlib import Path
import logging


def main():
    """Organize a given directory of cinema movies based on PLEX conventions"""
    movies: Path = Path(Configurations.MOVIES_PATH)
    tmdb_parser: TMDBParser = _get_tmdb_parser()
    plex_analyzer: PlexAnalyzer = PlexAnalyzer(db_parser=tmdb_parser)
    plex_organizer: PlexOrganizer = PlexOrganizer(db_name=SupportedDBs.TMDB.value)
    collection_manager: CollectionManager = CollectionManager(movies, plex_analyzer, plex_organizer)
    collection_manager.analyze()
    collection_manager.organize()


def _get_tmdb_parser() -> TMDBParser:
    """Create a new TMDB object"""
    api_key: str = Configurations.TMDB_API_KEY
    heb_locale: Locale = get_locale("he", "IL")
    eng_locale: Locale = get_locale("en", "US")
    tmdb_parser: TMDBParser = TMDBParser(api_key=api_key, locale=heb_locale, fallback_locale=eng_locale)
    return tmdb_parser


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
