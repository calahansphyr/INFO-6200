"""
Personal Library Manager - Flask Web Interface

To run:
  1. pip install -r requirements.txt
  2. python web_app.py
Then open http://127.0.0.1:5000/
"""
from __future__ import annotations

from typing import List, Dict, Any

from flask import Flask, redirect, render_template, request, url_for

from app import load_library, save_library, library as cli_library

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Main route: home page. Reads and parses all data from JSON, passes collection to template."""
    books = load_library()
    return render_template("index.html", books=books)


@app.route("/books")
@app.route("/items")
def list_books() -> str:
    """Display all items from persistent JSON. GET: read/parse data.json, pass collection to Jinja2 for rendering."""
    books = load_library()
    return render_template("books.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add() -> str:
    """Display and process the add-book form."""
    if request.method == "POST":
        books: List[Dict[str, Any]] = load_library()

        # Keep CLI library in sync so save_library() writes the correct data
        cli_library.clear()
        cli_library.extend(books)

        isbn = request.form.get("isbn", "").strip()
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        genre = request.form.get("genre", "").strip()
        pages_raw = request.form.get("pages", "").strip()
        rating_raw = request.form.get("rating", "").strip()
        is_read = request.form.get("is_read") is not None

        try:
            pages = int(pages_raw) if pages_raw else 0
        except ValueError:
            pages = 0

        try:
            rating = float(rating_raw) if rating_raw else 0.0
        except ValueError:
            rating = 0.0

        next_id = max((b.get("id", 0) for b in cli_library), default=0) + 1
        book: Dict[str, Any] = {
            "id": next_id,
            "isbn": isbn,
            "title": title,
            "author": author,
            "genre": genre,
            "pages": pages,
            "is_read": is_read,
            "rating": rating,
        }

        cli_library.append(book)
        save_library()

        return redirect(url_for("list_books"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
