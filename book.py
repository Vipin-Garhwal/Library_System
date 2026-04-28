class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} - {'Issued' if self.is_issued else 'Available'}"
