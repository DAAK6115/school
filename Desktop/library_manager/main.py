from books.models import Book
from books.services import BookService
from users.models import User
from users.services import UserService

if __name__ == "__main__":
    # Gestion des livres
    book_service = BookService()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book_service.add_book(book1)
    print(f"Books in library: {book_service.get_books()}")

    # Gestion des utilisateurs
    user_service = UserService()
    user1 = User("johndoe", "john@example.com")
    user_service.add_user(user1)
    print(f"Users in system: {user_service.get_users()}")
