from app.book import Book

book1 = Book("Python 1" , "John smith" , "123-456")

print(f"Book title: {book1.title}")

try:
    book1.title ="AB"
except ValueError as e:
    print(f"Error: {e}")

book1.title = "Python Programming"

print(f"New title: {book1.title}")