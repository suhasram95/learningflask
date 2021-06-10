from enum import Enum
class BookTypes(Enum):
    HARDCOVER = "hardcover"
    PAPERBACK = "paperback"
class Book:
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, BookTypes.HARDCOVER.value, page_weight)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, BookTypes.PAPERBACK.value, page_weight)

book = Book.hardcover("Harry Potter", "50g")
print (book)

