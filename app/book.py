class Book:
    def __init__(self,title,author,isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_checked_out = False
        

    @property
    def title(self):
        

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