"""PDFIngestor class for extracting data from .pdf files"""

from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """
    Class PDFIngestor
    
    Extracts quotes and authors from .pdf files and returns
    a QuoteModel object.
    """
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quote and author data from .pdf files.
        
        Parameters:
            path: a string indicating path to the .pdf file
        Return:
            List[QuoteModel]: returns list of quotes and authors
        
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp_{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0],
                                       parsed[1]
                                       )
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
