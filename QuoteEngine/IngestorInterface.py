"""Abstract class for parsing and extracting data"""

from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel 

class IngestorInterface(ABC):
    """IngestorInterface class
    Methods:
        can_ingest
        parse
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Classmethod 'can_ingest' ensures files can be parsed.
        
        Parameters:
            cls: IngestorInterface class
            path: string indicating path to file
        Returns:
            boolean: whether file can be parsed or not
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str)-> List[QuoteModel]:
        """
        Classmethod 'parse' extracts quotes and authors from files.
        
        Parameters:
            cls: IngestorInterface class
            path: string indicating path to file
        Returns:
            List[QuoteModel]: list of quotes and authors
        """
        
        pass