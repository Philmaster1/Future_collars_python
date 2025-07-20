class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

def __str__(self):
    status = "Available" if self.available else "Borrowed"
    return f"{self.title} - {self.author} ({status})"


    #def describe(self):
      #  status = "Available" if self.available else "Borrowed"
      #  return f"{self.title} - {self.author} ({status})"

def to_file_format(self):
    return f"{self.title} - {self.author}|{self.available}"


def from_file_format(line):  # Map text line to object
    title, author, available = line.strip().split('|')
    return Book(title, author, available == 'True')


def load_books_from_file(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                books.append(from_file_format(line))
    except FileNotFoundError:
        print("File with books nos exists, creating new file")
    return books


def display_books(books):
    if not books:
        print("No books in library")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.describe()}")


def add_book(books, title, author):
    books.append(Book(title, author))
    print(f"New book added: {title}")

def borrow_book(books, book_number):
    if 0 < book_number <= len(books):
        book = books[book_number -1]
        if book.available:
            book.available = False
            print(f"you borrowed book: {book.title}")
        else:
            print("book already taken")

def return_book(books, book_number):
    if 0 < book_number <= len(books):
        book = books[book_number - 1]
        if book.available:
            book.available = True
            print(f"you return book: {book.title}")
        else:
            print("book already returned")

def save_books_to_file(filename, books):
    with open(filename, 'w') as file:
        for book in books:
            file.write(book.to_file_format() + "\n")

def main():
    filename = "books.txt"
    books = load_books_from_file(filename)

    while True:
        print("\n--- MENU ---")
        print("1. Display all books")
        print("2. Add new books")
        print("3. Borrow a book")
        print("4. Return a previously borrowed book")
        print("5. Exit")

        choice = input("Choose option")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            title = input("Enter the title")
            author = input("Enter the author")
            add_book(books, title, author)
        elif choice == '3':
            display_books(books)
            book_number = int(input("Enter id of the book to borrow"))
            borrow_book(books, book_number)
        elif choice == '4':
            display_books(books)
            book_number = int(input("Enter id of the book to return"))
            return_book(books, book_number)
        elif choice == '5':
            break
        else:
            print("Wrong option")


main()



