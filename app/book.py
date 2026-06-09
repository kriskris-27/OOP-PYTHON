class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def checkout(self):
        self.is_checked_out = True
        print(f"'{self.title}' has been checked out")

    def return_book(self):
        self.is_checked_out = False
        print(f"'{self.title}' has been returned")

    def display_info(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")