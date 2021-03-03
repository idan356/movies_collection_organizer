from abc import ABC, abstractmethod


class MovieDB(ABC):

    @abstractmethod
    def get_title(self) -> str:
        """Get movie title"""
        pass

    @abstractmethod
    def get_year(self) -> str:
        """Get movie release year"""
        pass

    @abstractmethod
    def get_movie_id(self) -> str:
        """Get movie's database unique ID"""
        pass

    @abstractmethod
    def get_youtube_trailer_url(self):
        """Get movie's trailer URL from the DB"""
        pass
