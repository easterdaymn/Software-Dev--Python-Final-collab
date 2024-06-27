class Book:
    def __init__(self, title, author, isbn):
        self.details = (title, author, isbn)  # Using a tuple to store book details
        self.issued_to = None
    
    @property
    def title(self):
        return self.details[0]

    @property
    def author(self):
        return self.details[1]
    
    @property
    def isbn(self):
        return self.details[2]

    def issue(self, member):
        self.issued_to = member
    
    def return_book(self):
        self.issued_to = None
