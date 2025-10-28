# tests.py - simple assert-based tests for operations.py
from operations import (
    books, members,
    add_book, add_member, search_books,
    borrow_book, return_book, delete_book, delete_member
)

# Clear any existing data (in case tests run multiple times)
books.clear()
members.clear()

# Test 1: Add a book successfully
add_book("T1", "Test Book 1", "Author A", "Fiction", 1)
assert "T1" in books
assert books["T1"]["available_copies"] == 1

# Test 2: Prevent adding duplicate ISBN
try:
    add_book("T1", "Test Book 1 Duplicate", "Author A", "Fiction", 1)
    assert False, "Duplicate ISBN should raise ValueError"
except ValueError:
    pass

# Test 3: Borrow a book when available
add_member(10, "Tester", "test@example.com")
borrow_book(10, "T1")
assert books["T1"]["available_copies"] == 0
assert "T1" in next(m for m in members if m["member_id"]==10)["borrowed_books"]

# Test 4: Prevent borrowing when no copies left
try:
    borrow_book(10, "T1")
    assert False, "Should not be able to borrow when no copies left"
except ValueError:
    pass

# Test 5: Return a book increases available copies
return_book(10, "T1")
assert books["T1"]["available_copies"] == 1
assert "T1" not in next(m for m in members if m["member_id"]==10)["borrowed_books"]

# Test 6: Delete member with no borrowed books succeeds
add_member(11, "Removable", "remove@example.com")
delete_member(11)
assert all(m["member_id"] != 11 for m in members)

print("All tests passed.")