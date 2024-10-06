# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize the Book instance with title and author."""
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book, making it unavailable."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out

    def return_book(self):
        """Return the book, making it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Was not checked out

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the Library instance with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'You have checked out "{title}".'
                return f'"{title}" is already checked out.'
        return f'Book titled "{title}" not found in the library.'

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f'You have returned "{title}".'
                return f'"{title}" was not checked out.'
        return f'Book titled "{title}" not found in the library.'

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            return "\n".join(available_books)
        return "No available books."


