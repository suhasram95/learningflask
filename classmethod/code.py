from enum import Enum
class Types(Enum):
    HARDCOVER = "hardcover"
    PAPERBACK = "paperback"
class Book:
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}"

book = Book("Harry Potter", Types.HARDCOVER.value, "50g")
print (book)