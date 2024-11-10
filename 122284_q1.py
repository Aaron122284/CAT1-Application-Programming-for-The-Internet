class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"Borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"Returned {book.title}")
        else:
            print(f"{book.title} was not borrowed.")


book1 = Book("1984", "George Orwell")
member = LibraryMember("Yannick", "LM122284")

member.borrow_book(book1)
member.return_book(book1)
