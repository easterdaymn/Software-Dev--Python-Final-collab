import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book
from member import Member

class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Library Management System")
        
        # Add book section
        self.add_book_frame = tk.Frame(root)
        self.add_book_frame.pack()
        
        self.book_title_label = tk.Label(self.add_book_frame, text="Book Title")
        self.book_title_label.grid(row=0, column=0)
        self.book_title_entry = tk.Entry(self.add_book_frame)
        self.book_title_entry.grid(row=0, column=1)
        
        self.book_author_label = tk.Label(self.add_book_frame, text="Book Author")
        self.book_author_label.grid(row=1, column=0)
        self.book_author_entry = tk.Entry(self.add_book_frame)
        self.book_author_entry.grid(row=1, column=1)
        
        self.book_isbn_label = tk.Label(self.add_book_frame, text="Book ISBN")
        self.book_isbn_label.grid(row=2, column=0)
        self.book_isbn_entry = tk.Entry(self.add_book_frame)
        self.book_isbn_entry.grid(row=2, column=1)
        
        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=3, columnspan=2)
        
        # Add member section
        self.add_member_frame = tk.Frame(root)
        self.add_member_frame.pack()
        
        self.member_id_label = tk.Label(self.add_member_frame, text="Member ID")
        self.member_id_label.grid(row=0, column=0)
        self.member_id_entry = tk.Entry(self.add_member_frame)
        self.member_id_entry.grid(row=0, column=1)
        
        self.member_name_label = tk.Label(self.add_member_frame, text="Member Name")
        self.member_name_label.grid(row=1, column=0)
        self.member_name_entry = tk.Entry(self.add_member_frame)
        self.member_name_entry.grid(row=1, column=1)
        
        self.add_member_button = tk.Button(self.add_member_frame, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=2, columnspan=2)
        
        # Issue book section
        self.issue_book_frame = tk.Frame(root)
        self.issue_book_frame.pack()
        
        self.issue_isbn_label = tk.Label(self.issue_book_frame, text="Book ISBN")
        self.issue_isbn_label.grid(row=0, column=0)
        self.issue_isbn_entry = tk.Entry(self.issue_book_frame)
        self.issue_isbn_entry.grid(row=0, column=1)
        
        self.issue_member_id_label = tk.Label(self.issue_book_frame, text="Member ID")
        self.issue_member_id_label.grid(row=1, column=0)
        self.issue_member_id_entry = tk.Entry(self.issue_book_frame)
        self.issue_member_id_entry.grid(row=1, column=1)
        
        self.issue_book_button = tk.Button(self.issue_book_frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=2, columnspan=2)
        
        # Return book section
        self.return_book_frame = tk.Frame(root)
        self.return_book_frame.pack()
        
        self.return_isbn_label = tk.Label(self.return_book_frame, text="Book ISBN")
        self.return_isbn_label.grid(row=0, column=0)
        self.return_isbn_entry = tk.Entry(self.return_book_frame)
        self.return_isbn_entry.grid(row=0, column=1)
        
        self.return_member_id_label = tk.Label(self.return_book_frame, text="Member ID")
        self.return_member_id_label.grid(row=1, column=0)
        self.return_member_id_entry = tk.Entry(self.return_book_frame)
        self.return_member_id_entry.grid(row=1, column=1)
        
        self.return_book_button = tk.Button(self.return_book_frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=2, columnspan=2)
        
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        isbn = self.book_isbn_entry.get()
        book = Book(title, author, isbn)
        self.library.add_book(book)
        messagebox.showinfo("Success", "Book added successfully!")
        
    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.member_name_entry.get()
        member = Member(member_id, name)
        self.library.add_member(member)
        messagebox.showinfo("Success", "Member added successfully!")
    
    def issue_book(self):
        isbn = self.issue_isbn_entry.get()
        member_id = self.issue_member_id_entry.get()
        self.library.issue_book(isbn, member_id)
    
    def return_book(self):
        isbn = self.return_isbn_entry.get()
        member_id = self.return_member_id_entry.get()
        self.library.return_book(isbn, member_id)

if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    gui = LibraryGUI(root, library)
    root.mainloop()