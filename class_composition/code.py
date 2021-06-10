from typing import List
class BookShelf:
    def __init__(self, *books):
        self.books = books
    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

shelf = BookShelf(300)
print(shelf)

class Book:
    def __init__(self, name):
        self.name = name
    
book = Book("Harry Potter")
book2 = Book("Rains of fire")
print (book)
print (book2)