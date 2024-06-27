from array import array
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.book_ids = array('i')  # Using an array to store book IDs
    
    def add_book(self, book):
        self.books[book.isbn] = book
        self.book_ids.append(int(book.isbn))  # Adding the book's ISBN to the array
    
    def add_member(self, member):
        self.members[member.member_id] = member
    
    def issue_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            book = self.books[isbn]
            member = self.members[member_id]
            if book.issued_to is None:
                book.issue(member)
                member.borrow_book(book)
                print(f"Book {book.title} issued to {member.name}.")
            else:
                print("Book is already issued.")
        else:
            print("Book or Member not found.")
    
    def return_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            book = self.books[isbn]
            member = self.members[member_id]
            if book.issued_to == member:
                book.return_book()
                member.return_book(book)
                print(f"Book {book.title} returned by {member.name}.")
            else:
                print("Book was not issued to this member.")
        else:
            print("Book or Member not found.")
