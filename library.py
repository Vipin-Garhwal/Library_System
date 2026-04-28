from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def display_books(self):
        for book in self.books.values():
            print(book)

    def calculate_fine(self, issue_date, duration, return_date):
        due_date = issue_date + timedelta(days=duration)
        if return_date > due_date:
            late_days = (return_date - due_date).days
            weeks_late = late_days // 7 + (1 if late_days % 7 else 0)
            fine = weeks_late * 50  # Progressive fine: 50 per week late
            return fine
        return 0
