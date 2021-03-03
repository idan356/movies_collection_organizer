from collection_manager.analyzed_movie import AnalyzedMovie
from abc import ABC, abstractmethod
from typing import List


class Organizer(ABC):

    @abstractmethod
    def organize(self, movies: List[AnalyzedMovie]) -> None:
        """Organize a given list of analyzed movies"""
        pass
