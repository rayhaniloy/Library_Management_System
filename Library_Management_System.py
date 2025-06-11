class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f'Book "{self.__title}" has been borrowed succesfully.')
        else:
            print(f'Book "{self.__title}" is already borrowed.')

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f'Book "{self.__title}" has been returned succesfully.')
        else:
            print(f'Book "{self.__title}" was not borrowed.')

    def view_book_info(self):
        status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {status}")

    @classmethod
    def find_book_by_id(cls, book_id):
        for book in Library.book_list:
            if book.__book_id == book_id:
                return book
        return None


Book("B001", "abc", "ABC")
Book("B002", "bcd", "BCD")
Book("B003", "def", "DEF")
Book("B004", "efg", "EFG")
Book("B005", "fgh", "FGH")
Book("B006", "ghi", "GHI")
Book("B007", "hij", "HIJ")
Book("B008", "ijk", "IJK")


while True:
    print("\n===== Library Menu =====")
    print("Press 1 to View All Books")
    print("Press 2 to Borrow a Book")
    print("Press 3 to Return a Book")
    print("Press 4 to Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\n--- Book List ---")
        for book in Library.book_list:
            book.view_book_info()
            print("-" * 30)
    
    elif choice == "2":
        book_id = input("Enter the Book ID to borrow: ")
        book = Book.find_book_by_id(book_id)
        if book:
            book.borrow_book()
        else:
            print("Invalid Book ID. Please enter a valid book ID.")
    
    elif choice == "3":
        book_id = input("Enter the Book ID to return: ")
        book = Book.find_book_by_id(book_id)
        if book:
            book.return_book()
        else:
            print("Invalid Book ID. Please enter a valid book ID.")
    
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")