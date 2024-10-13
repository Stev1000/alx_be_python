# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book):
        # Add the book to the collection
        self.books.append(book)

    def list_books(self):
        # Iterate through the books and print their details
        for book in self.books:
            print(book.get_details())
