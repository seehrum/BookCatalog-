import json
import os
import platform
import signal

class BookCatalog:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn, category, sector):
        """Add a book to the catalog with basic validation."""
        if not self.is_valid_isbn(isbn):
            print("Invalid ISBN. Book not added.")
            return

        book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'category': category,
            'sector': sector
        }
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def is_valid_isbn(self, isbn):
        """Check if the ISBN is valid."""
        # ISBN validation logic here
        return True

    def search_books(self, search_term):
        """Search for books by any field."""
        search_term = search_term.lower()
        results = [book for book in self.books if search_term in book['title'].lower() 
                   or search_term in book['author'].lower() 
                   or search_term in book['isbn'].lower() 
                   or search_term in book['category'].lower() 
                   or search_term in book['sector'].lower()]
        return results

    def display_books(self):
        """Display all books in the catalog."""
        print(f"\n\033[1mTotal number of books: {len(self.books)}\033[0m")  # Bold text
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Category: {book['category']}, Sector: {book['sector']}")

    def save_books(self):
        """Save books to a JSON file with exception handling."""
        try:
            with open('books.json', 'w') as file:
                json.dump(self.books, file, indent=4)
        except IOError as e:
            print(f"Error saving books: {e}")

    def load_books(self):
        """Load books from a JSON file with exception handling."""
        try:
            with open('books.json', 'r') as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading books: {e}")
            self.books = []

def clear_screen():
    """Clears the console screen in a more Pythonic way."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def signal_handler(sig, frame):
    """Handle interrupt signal gracefully."""
    print("\nExiting program.")
    raise SystemExit  # Raise a SystemExit exception to exit the program

def main():
    signal.signal(signal.SIGINT, signal_handler)
    catalog = BookCatalog()

    while True:
        clear_screen()
        print("\nBook Catalog System".center(50))
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Display All Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            category = input("Enter book category: ")
            sector = input("Enter book sector: ")
            catalog.add_book(title, author, isbn, category, sector)

        elif choice == '2':
            search_term = input("Enter a search term (title, author, ISBN, category, sector): ")
            results = catalog.search_books(search_term)
            print(f"\n\033[1mSearch Results - Total Found: {len(results)}\033[0m")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Category: {book['category']}, Sector: {book['sector']}")
            input("\nPress Enter to continue...")

        elif choice == '3':
            catalog.display_books()
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
