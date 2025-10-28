# operations.py
# Mini Library Management System Core Functions

books = {}  # Dictionary: ISBN -> details
members = []  # List of member dictionaries
genres = ("Fiction", "Non-Fiction", "Sci-Fi")  # Valid genres tuple

def add_book(isbn, title, author, genre, total_copies):
    """Add a book if ISBN is unique and genre is valid."""
    if isbn in books:
        raise ValueError("Book with this ISBN already exists.")
    if genre not in genres:
        raise ValueError(f"Invalid genre. Valid genres: {genres}")
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": int(total_copies),
        "available_copies": int(total_copies)
    }

def add_member(member_id, name, email):
    """Add a member if ID is unique."""
    if any(m["member_id"] == member_id for m in members):
        raise ValueError("Member ID already exists.")
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })

def search_books(keyword):
    """Return list of books matching title or author (case-insensitive)."""
    keyword = keyword.lower()
    return [
        {"isbn": isbn, **details}
        for isbn, details in books.items()
        if keyword in details["title"].lower() or keyword in details["author"].lower()
    ]

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """Update book details. Adjust available_copies if total_copies changes."""
    if isbn not in books:
        raise KeyError("Book not found.")
    if genre and genre not in genres:
        raise ValueError("Invalid genre.")
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        total_copies = int(total_copies)
        diff = total_copies - books[isbn]["total_copies"]
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] += diff
        if books[isbn]["available_copies"] < 0:
            # Prevent negative available copies; roll back and raise
            books[isbn]["available_copies"] -= diff
            books[isbn]["total_copies"] -= diff
            raise ValueError("Total copies cannot be less than borrowed copies.")

def update_member(member_id, name=None, email=None):
    """Update member details."""
    for m in members:
        if m["member_id"] == member_id:
            if name:
                m["name"] = name
            if email:
                m["email"] = email
            return
    raise KeyError("Member not found.")

def delete_book(isbn):
    """Delete a book only if no copies are currently borrowed."""
    if isbn not in books:
        raise KeyError("Book not found.")
    borrowed_count = books[isbn]["total_copies"] - books[isbn]["available_copies"]
    if borrowed_count > 0:
        raise ValueError("Cannot delete book: copies are currently borrowed.")
    del books[isbn]

def delete_member(member_id):
    """Delete a member only if they have no borrowed books."""
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                raise ValueError("Cannot delete member with borrowed books.")
            members.remove(m)
            return
    raise KeyError("Member not found.")

def borrow_book(member_id, isbn):
    """Allow a member to borrow up to 3 books if available."""
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        raise KeyError("Member not found.")
    if len(member["borrowed_books"]) >= 3:
        raise ValueError("Member has already borrowed 3 books.")
    if isbn not in books:
        raise KeyError("Book not found.")
    book = books[isbn]
    if book["available_copies"] <= 0:
        raise ValueError("No copies available to borrow.")
    book["available_copies"] -= 1
    member["borrowed_books"].append(isbn)

def return_book(member_id, isbn):
    """Return a borrowed book."""
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        raise KeyError("Member not found.")
    if isbn not in member["borrowed_books"]:
        raise ValueError("This book was not borrowed by the member.")
    member["borrowed_books"].remove(isbn)
    if isbn not in books:
        # If book record was deleted while borrowed (shouldn't happen), just ignore
        return
    books[isbn]["available_copies"] += 1