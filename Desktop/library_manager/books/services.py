from books.models import Book

class BookService:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self):
        return self.books
