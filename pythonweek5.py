class Book:
    def __init__(self, title, author, year_published, genre):
        self.title = title              # Title of the book
        self.author = author            # Author name
        self.year_published = year_published  # Year when the book was published
        self.genre = genre              # Book genre (e.g., fiction, non-fiction)
        self.is_checked_out = False     # Book availability status
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned. Thank you!")
        else:
            print(f"'{self.title}' was not checked out.")
    
    def get_description(self):
        """Return a formatted string describing the book."""
        return f"'{self.title}' by {self.author} ({self.year_published}) - Genre: {self.genre}"

# Example usage
my_book = Book("1984", "George Orwell", 1949, "Dystopian")
print(my_book.get_description())  # Output book details
my_book.check_out()                # Check out the book
my_book.check_out()                # Try to check out again to test logic
my_book.return_book()              # Return the book