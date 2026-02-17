"""
Personal Library Manager - Graduate School Assignment
Stores books in a global list and provides menu-driven add/list/exit.
Loads data from data.json on startup and saves immediately on modification.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

library: list[dict] = []


def load_library() -> list[dict]:
    """Load library from data.json. Returns empty list if file missing or invalid."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_library() -> None:
    """Write the current library to data.json in human-readable JSON format."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)


def add_book() -> None:
    """Prompt for Title, Author, and Page Count; append as a dictionary to library."""
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    page_count_input = input("Enter page count: ").strip()
    try:
        pages = int(page_count_input)
    except ValueError:
        pages = 0
    next_id = max((b["id"] for b in library), default=0) + 1
    book = {
        "id": next_id,
        "isbn": "",
        "title": title,
        "author": author,
        "genre": "",
        "pages": pages,
        "is_read": False,
        "rating": 0.0,
    }
    library.append(book)
    save_library()
    print("Book added successfully.\n")


def list_books() -> None:
    """Iterate through library and print every book in a readable format."""
    if not library:
        print("Your library is empty. Add some books to get started!\n")
        return
    print("\n--- Your Books ---")
    for i, book in enumerate(library, start=1):
        print(
            f"{i}. {book['title']} by {book['author']} "
            f"({book['pages']} pages)"
        )
    print()


def main() -> None:
    """Run the main menu loop."""
    global library
    library = load_library()

    while True:
        print("Personal Library Manager")
        print("-----------------------")
        print("1. Add a Book")
        print("2. List all Books")
        print("3. Exit")
        print()

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            print("Goodbye! Thanks for using Personal Library Manager.")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
