class Book:
    total_books = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(Book.total_books)  
