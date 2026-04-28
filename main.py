# ============================================================
#  main.py  — Entry Point of the Library Management System
# ============================================================
# HOW TO RUN:
#   Open a terminal in this folder and type:
#       python main.py
#
# PROJECT STRUCTURE:
#   main.py                        ← You are here (run this)
#   library_management/
#       __init__.py                ← Makes it a package
#       books.py                   ← Book records & functions
#       students.py                ← Student records & functions
#       transactions.py            ← Issue, return, fine logic
#       display.py                 ← Menus and input helpers
# ============================================================

# Import all modules from the library_management package
from library_management import books       as books_mod
from library_management import students    as students_mod
from library_management import transactions as trans_mod
from library_management import display


# ─────────────────────────────────────────────
#  BOOK MANAGEMENT
# ─────────────────────────────────────────────

def book_management():
    """Sub-menu for all book-related operations."""
    while True:
        display.print_book_menu()
        choice = display.get_input("Enter your choice")

        if choice == "1":
            # Show all books
            books_mod.display_all_books()
            display.pause()

        elif choice == "2":
            # Search by title or author
            keyword = display.get_input("Enter title or author to search")
            results = books_mod.search_book(keyword)
            if results:
                print(f"\n  Found {len(results)} result(s):\n")
                print(f"  {'ID':<8} {'Title':<25} {'Author':<20} {'Copies'}")
                print("  " + "-" * 60)
                for bid, info in results.items():
                    copies = f"{info['available_copies']} / {info['total_copies']}"
                    print(f"  {bid:<8} {info['title']:<25} {info['author']:<20} {copies}")
            else:
                print(f"\n  [!] No books found matching '{keyword}'.")
            display.pause()

        elif choice == "3":
            # Add a new book
            print("\n  --- Add New Book ---")
            book_id = display.get_input("Book ID (e.g. B006)")
            title   = display.get_input("Book Title")
            author  = display.get_input("Author Name")
            try:
                copies = int(display.get_input("Number of Copies"))
                if copies <= 0:
                    print("\n  [!] Copies must be at least 1.")
                else:
                    books_mod.add_book(book_id, title, author, copies)
            except ValueError:
                print("\n  [!] Please enter a valid number for copies.")
            display.pause()

        elif choice == "0":
            break  # Go back to main menu

        else:
            print("\n  [!] Invalid choice. Please try again.")


# ─────────────────────────────────────────────
#  STUDENT MANAGEMENT
# ─────────────────────────────────────────────

def student_management():
    """Sub-menu for all student-related operations."""
    while True:
        display.print_student_menu()
        choice = display.get_input("Enter your choice")

        if choice == "1":
            # Show all students
            students_mod.display_all_students()
            display.pause()

        elif choice == "2":
            # Register a new student
            print("\n  --- Register New Student ---")
            student_id = display.get_input("Student ID (e.g. S004)")
            name       = display.get_input("Full Name")
            email      = display.get_input("Email Address")
            students_mod.register_student(student_id, name, email)
            display.pause()

        elif choice == "0":
            break

        else:
            print("\n  [!] Invalid choice. Please try again.")


# ─────────────────────────────────────────────
#  ISSUE / RETURN BOOK
# ─────────────────────────────────────────────

def issue_return_management():
    """Sub-menu for issuing and returning books."""
    while True:
        display.print_issue_menu()
        choice = display.get_input("Enter your choice")

        if choice == "1":
            # Issue a book
            print("\n  --- Issue a Book ---")
            print("  Tip: Use option 1 from Book/Student menus to find IDs.\n")

            # Show books and students for reference
            books_mod.display_all_books()
            students_mod.display_all_students()

            student_id = display.get_input("Enter Student ID")
            book_id    = display.get_input("Enter Book ID")
            try:
                duration = int(display.get_input("Loan Duration (in weeks)"))
                if duration <= 0:
                    print("\n  [!] Duration must be at least 1 week.")
                else:
                    trans_mod.issue_book(student_id, book_id, duration)
            except ValueError:
                print("\n  [!] Please enter a valid number for duration.")
            display.pause()

        elif choice == "2":
            # Return a book
            print("\n  --- Return a Book ---")
            trans_mod.display_issued_books()

            if trans_mod.issued_records:  # Only ask if there are active records
                tid = display.get_input("Enter Transaction ID to return")
                trans_mod.return_book(tid)
            display.pause()

        elif choice == "0":
            break

        else:
            print("\n  [!] Invalid choice. Please try again.")


# ─────────────────────────────────────────────
#  FINE PREVIEW
# ─────────────────────────────────────────────

def fine_preview():
    """Show the current fine for an active transaction."""
    trans_mod.display_issued_books()
    if trans_mod.issued_records:
        tid = display.get_input("Enter Transaction ID to check fine")
        trans_mod.check_fine_preview(tid)
    display.pause()


# ─────────────────────────────────────────────
#  MAIN PROGRAM LOOP
# ─────────────────────────────────────────────

def main():
    """
    Main function — runs the application loop.
    Keeps showing the menu until the user chooses to exit.
    """
    display.print_header()

    while True:
        display.print_main_menu()
        choice = display.get_input("Enter your choice")

        if choice == "1":
            book_management()

        elif choice == "2":
            student_management()

        elif choice == "3":
            issue_return_management()

        elif choice == "4":
            trans_mod.display_issued_books()
            display.pause()

        elif choice == "5":
            fine_preview()

        elif choice == "0":
            print("\n  Goodbye! Happy Reading!\n")
            break

        else:
            print("\n  [!] Invalid choice. Please enter a number from the menu.")


# ─────────────────────────────────────────────
#  Run the program
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
