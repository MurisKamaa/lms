from abc import ABC, abstractmethod
from models.book import Book

class User(ABC):
    name: str
    borrowed_books: list[Book]

    @abstractmethod
    def get_user_info(self) -> str:
        pass

    @abstractmethod
    def borrow_books(self, book: Book) -> None:
        pass

    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass

class Member(User):
    def __init__(self, name) -> None:
        self.name = name
        self.borrowed_books = []

    def get_user_info(self) -> str:
        return f"Member: {self.name}"

    def borrow_book(self, book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book) -> None:
        self.borrowed_books.remove(book)

class Librarian(User):
    def __init__(self, name) -> None:
        self.name = name

    def get_user_info(self) -> str:
        return f"Librarian: {self.name}"
    
    def borrow_books(self, book: Book) -> None:
        pass

    def return_book(self, book: Book) -> None:
        pass