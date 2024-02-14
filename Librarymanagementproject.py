print("Welcome to Pylib!")

class Library:
    def __init__(self, name):
        self.name = name

    def list_books(self):
        try:
            with open("books.txt", "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    book_info = line.split(",")
                    book_title = book_info[0]
                    book_author = book_info[1]
                    print(f"Title: {book_title}, Author: {book_author}")
        except FileNotFoundError:
            print("No books found in the library.")

    def add_book(self):
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        release_year = input("Enter the first release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
        with open("books.txt", "a") as file:
            file.write(book_info)
        print(f"{book_title} by {book_author} has been added to the library.")

    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ")
        try:
            with open("books.txt", "r") as file:
                lines = file.readlines()
            with open("books.txt", "w") as file:
                for line in lines:
                    if book_title not in line:
                        file.write(line)
            print(f"{book_title} has been removed from the library.")
        except FileNotFoundError:
            print("No books found in the library.")


library = Library("Pylib")

while True:
    print("\nMenu:")
    print("1. List all books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library.list_books()
    elif choice == "2":
        library.add_book()
    elif choice == "3":
        library.remove_book()
    elif choice == "4":
        print("Thank you for using Pylib. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



