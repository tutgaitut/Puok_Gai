import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' by {author} ({year}) added to the library.")

    def view_books(self):
        print("\nLibrary Collection:")
        for i, book in enumerate(self.books):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i + 1}. {book.title} by {book.author} ({book.year}) - {status}")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
                self.save_books()
                return
        print(f"Sorry, the book '{title}' is either not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
                self.save_books()
                return
        print(f"Sorry, the book '{title}' was not borrowed from this library.")

    def load_books(self):
        try:
            with open("library_books.json", "r") as file:
                books_data = json.load(file)
                for book in books_data:
                    loaded_book = Book(book["title"], book["author"], book["year"])
                    loaded_book.is_borrowed = book["is_borrowed"]
                    self.books.append(loaded_book)
        except FileNotFoundError:
            print("No existing library data found. Initializing new library.")

    def save_books(self):
        books_data = [
            {"title": book.title, "author": book.author, "year": book.year, "is_borrowed": book.is_borrowed}
            for book in self.books
        ]
        with open("library_books.json", "w") as file:
            json.dump(books_data, file)

# Initializing the library
library = Library()

# library
initial_books = [
    {"title": "Tomb of Sand", "author": "Geetanjali Shree", "year": 2022},
    {"title": "Adam", "author": "S. Hareesh", "year": 2022},
    {"title": "To Hell and Back: Humans of COVID", "author": "Barkha Dutt", "year": 2022},
    {"title": "Asoca: A Sutra", "author": "Irwin Allan Sealy", "year": 2021},
    {"title": "Whereabouts", "author": "Jhumpa Lahiri", "year": 2018},
    {"title": "The Bench", "author": "Meghan Markle, Duchess of Sussex", "year": 2021},
    {"title": "Elephant in the Womb", "author": "Kalki Koechlin", "year": 2021},
    {"title": "Landscapes of Loss: The Story of an Indian Drought", "author": "Kavitha Iyer", "year": 2021},
    {"title": "Economy and Society", "author": "Max Weber", "year": 1922},
    {"title": "Platform Scale: For a Post-Pandemic World", "author": "Sangeet Paul Choudhary", "year": 2021},
    {"title": "A House for Mr. Biswas", "author": "V.S. Naipaul", "year": 1961},
]

if not library.books:
    for book in initial_books:
        library.add_book(book["title"], book["author"], book["year"])

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a new book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.view_books()
    elif choice == "2":
        book_to_borrow = input("Enter the title of the book to borrow: ")
        library.borrow_book(book_to_borrow)
    elif choice == "3":
        book_to_return = input("Enter the title of the book to return: ")
        library.return_book(book_to_return)
    elif choice == "4":
        new_title = input("Enter the book title: ")
        new_author = input("Enter the book author: ")
        new_year = input("Enter the year of publication: ")
        library.add_book(new_title, new_author, int(new_year))
        library.save_books()
    elif choice == "5":
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
