""" Base class for the QuoteModel."""

class QuoteModel():
    """ Class defines quote with author's name."""
    def __init__(self, body: str, author: str):
        """Instantiate variables for QuoteModel class. """
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of the QuoteModel class """
        return f'<{self.body},{self.author}>'
