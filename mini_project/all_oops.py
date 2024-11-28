from abc import ABC, abstractmethod

# Abstract Class: Person (Abstraction)
class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def role(self):
        pass

# Inheritance: Member and Librarian inherit Person
class Member(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if library.lend_book(book, self):
            self.borrowed_books.append(book)

    def return_book(self, book, library):
        if book in self.borrowed_books:
            library.receive_book(book, self)
            self.borrowed_books.remove(book)

    def role(self):
        return "Member"

class Librarian(Person):
    def role(self):
        return "Librarian"

    def approve_transaction(self):
        return "Transaction approved."

# Class and Encapsulation: Book and Library
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.__books = []  # Encapsulation: Private collection
        self.__transactions = []  # Encapsulation: Private history

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        return [f"{book.title} by {book.author}" for book in self.__books]

    def lend_book(self, book, member):
        if book in self.__books:
            self.__books.remove(book)
            self.__transactions.append(f"{member.name} borrowed {book.title}")
            return True
        print(f"Book '{book.title}' is not available.")
        return False

    def receive_book(self, book, member):
        self.__books.append(book)
        self.__transactions.append(f"{member.name} returned {book.title}")

    def show_transactions(self):
        return self.__transactions

# Polymorphism in action
def show_role(person):
    print(f"{person.name} is a {person.role()}.")

# Demonstration
if __name__ == "__main__":
    # Create library, books, and people
    library = Library()
    book1 = Book("1984", "George Orwell", "12345")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")
    library.add_book(book1)
    library.add_book(book2)

    member = Member("Rahul", "M001")
    librarian = Librarian("Anita", "L001")

    # Polymorphism: Dynamic behavior
    show_role(member)  # Output: Rahul is a Member.
    show_role(librarian)  # Output: Anita is a Librarian.

    # Member borrowing a book
    print("\nAvailable books:", library.show_books())
    member.borrow_book(book1, library)
    print("After borrowing:", library.show_books())

    # Member returning a book
    member.return_book(book1, library)
    print("After returning:", library.show_books())

    # Transactions
    print("\nTransaction History:")
    print("\n".join(library.show_transactions()))
