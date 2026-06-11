from app.audiobook import Audiobook
from app.book import Book
from app.ebook import Ebook

# Test regular Book
print("=== Regular Book ===")
book1 = Book("Python 1", "John smith", "123-456")
book1.display_info()

# try:
#     book1.title ="AB"
# except ValueError as e:
#     print(f"Error: {e}")

# book1.title = "Python Programming"

# print(f"New title: {book1.title}")



# -------

# Test EBook (inherits from Book)

# print("\n=== EBook ===")

# ebook1=Ebook("Advanced Python", "Jane Doe", "789-012", 5.2, "PDF")
# ebook1.checkout()
# ebook1.display_info()
# ebook1.download()

books = [
    Book("Python Basics", "John Smith", "111-111"),
    Ebook("Advanced Python", "Jane Doe", "222-222", 5.2, "PDF"),
    Audiobook("Python Mastery", "Bob Johnson", "333-333", 8.5, "Alice Williams")
]
 
print("=== Polymorphism Demo ===")

for book in books:
    print(f"\nProcessing: {book.title}")
    book.checkout()
    book.display_info()


    if isinstance(book,Ebook):
        book.download()
    elif isinstance(book,Audiobook):
        book.play()
