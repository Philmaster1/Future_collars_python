class Books:
        def __init__(self, title, author, available=True):
            self.title = title


        self.author = author
        self.available = available
        def from_file_format(line):
            title, author, available = line.strip().split('│')
            return book(title, author, available == 'True')

        def load_books_from(filename):
            books = []


        try:
            with open(filename, 'r') as file:
                for line in file:
                    books.append(from_file_format(line))
        except FileNotFoundError:
            print("File with books not exists, creating new file")

    def display_books(books):
        if not books:
            print("No books in library")
        else:
            for i, book in enumerate(bools, 1):
                print(f"{i} . {book.describe}")

            def main():
                filename= "books.txt"
                books= load_books_from_file(filename)

                while True:
                    print("\n--- Menu ---")
                    print("1.Display all books")
                    print("2.Add book")
                    print("3.Borrow a book")
                    print("4.Return a previously borrowed book")
                    print("5.Exit")

choice = input("choose option")
if choice == '1':
    display_books(books)
elif choice == '2':
    print("2")
elif choice == '3':
    print("3")

elif choice == ('4'):
    print("4")

elif choice == ('5'):
    print("5")





