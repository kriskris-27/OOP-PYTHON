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

print("\n=== EBook ===")

ebook1=Ebook("Advanced Python", "Jane Doe", "789-012", 5.2, "PDF")
ebook1.checkout()
ebook1.display_info()
ebook1.download()