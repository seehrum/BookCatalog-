import json
import os
import platform
import signal

class BookCatalog:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn, category, sector):
        """Add a book to the catalog."""
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
        """Save books to a JSON file."""
        with open('books.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    def load_books(self):
        """Load books from a JSON file."""
        try:
            with open('books.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []

def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def signal_handler(sig, frame):
    """Handle interrupt signal."""
    print("\nExiting program.")
    exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)  # Handle CTRL+C gracefully
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
            if results:
                for book in results:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Category: {book['category']}, Sector: {book['sector']}")
            else:
                print("No books found.")
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("\nCatalog:")
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
