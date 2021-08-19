"""Base class for extracting data from csv, docx, pdf, txt files """

from typing import List
import docx
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """
    Ingestor class for parsing data
    
    """

    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract data from defined doctypes.
        
        Parameters:
            cls: IngestorInterface class
            path: string indicating path to file
            
        Return:
            List[QuoteModel]: list of quotes and authors
        """
        
        for ingestor in cls.Ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)