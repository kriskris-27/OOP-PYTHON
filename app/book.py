class Book:
    def __init__(self,title,author,isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_checked_out = False
        

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if len(value) < 3:
            raise ValueError("The title must be atleast three")
        self._title = value

    @property
    
    def is_checked_out(self):
        return self._is_checked_out
        
    def checkout(self):
        self._is_checked_out = True
        print(f"'{self.title}' has been checked out")

    def return_book(self):
        self._is_checked_out = False
        print(f"'{self.title}' has been returned")

    def display_info(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self._author}")
        print(f"ISBN: {self._isbn}")
        print(f"Status: {status}")