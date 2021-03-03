from collection_manager.analyzed_movie import AnalyzedMovie
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List


class Analyzer(ABC):

    def __init__(self):
        self.analyzed_movies: List[AnalyzedMovie] = []

    @abstractmethod
    def analyze(self, movies_collection_path: Path) -> None:
        """Analyze a movies collection path"""
        pass

    def get_analyzed_movies(self) -> List[AnalyzedMovie]:
        """Get all analyzed movies"""
        return self.analyzed_movies
