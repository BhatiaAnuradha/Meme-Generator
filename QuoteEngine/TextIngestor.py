"""TextIngestor class for extracting data from .txt files"""

import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """
    Class TextIngestor
    
    Extracts quotes and authors from .txt files and returns
    a QuoteModel object.
    """
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quote and author data from .txt files.
        
        Parameters:
            path: a string indicating path to the .txt file
        Return:
            List[QuoteModel]: returns list of quotes and authors
        
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        file = open(path, "r")
        quotes = []

        for line in file.readlines():
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(' - ')
                new_quote = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(new_quote)

        file.close()
        return quotes