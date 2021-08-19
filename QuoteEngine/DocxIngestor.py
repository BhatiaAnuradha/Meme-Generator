"""DocxIngestor class for extracting data from .docx files"""

from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """
    Class DocxIngestor
    
    Extracts quotes and authors from .docx files and returns
    a QuoteModel object.
    """
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quote and author data from .docx files.
        
        Parameters:
            path: a string indicating path to the .docx file
        Return:
            List[QuoteModel]: returns list of quotes and authors
        
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
        
        return quotes
