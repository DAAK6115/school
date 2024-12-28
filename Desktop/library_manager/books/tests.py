import unittest
from books.models import Book
from books.services import BookService

class TestBookService(unittest.TestCase):
    def test_add_book(self):
        book_service = BookService()
        book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
        book_service.add_book(book)
        self.assertIn(book, book_service.get_books())
