class Student:
    def __init__(self, name):
        self.name = name
        self.issued_books = {}

    def issue_book(self, book, issue_date, duration):
        self.issued_books[book.book_id] = {
            "book": book,
            "issue_date": issue_date,
            "duration": duration
        }
        book.is_issued = True

    def return_book(self, book_id, return_date):
        if book_id in self.issued_books:
            record = self.issued_books.pop(book_id)
            book = record["book"]
            book.is_issued = False
            return record, return_date
        return None, None
