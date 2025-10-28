# demo.py - Demonstration script for the Mini Library Management System
from operations import add_book, add_member, search_books, borrow_book, return_book, update_book, delete_member, books, members

def run_demo():
    # Add sample books
    add_book("123", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 3)
    add_book("456", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2)
    add_book("789", "Dune", "Frank Herbert", "Sci-Fi", 4)

    # Add sample members
    add_member(1, "Alice", "alice@example.com")
    add_member(2, "Bob", "bob@example.com")

    # Search
    print("Search results for 'Time':", search_books("Time"))

    # Borrow and return
    borrow_book(1, "456")
    print("After borrowing, available copies of 456:", books["456"]["available_copies"])
    borrow_book(1, "123")
    print("Alice borrowed books:", next(m for m in members if m["member_id"]==1)["borrowed_books"])

    return_book(1, "123")
    print("After return, available copies of 123:", books["123"]["available_copies"])

    # Update book copies
    update_book("456", total_copies=4)
    print("Updated total copies for 456:", books["456"]["total_copies"])

    # Attempt to delete member (Bob) who has no borrowed books
    delete_member(2)
    print("Members after deleting Bob:", [m['member_id'] for m in members])

if __name__ == "__main__":
    run_demo()