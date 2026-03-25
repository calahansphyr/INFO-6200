"""
Personal Library Manager - Flask Web Interface

To run:
  1. pip install -r requirements.txt
  2. python web_app.py
Then open http://127.0.0.1:5000/
"""
from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

from extensions import db
from models import Book

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "project.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def _all_books_ordered() -> list[Book]:
    return db.session.query(Book).order_by(Book.id).all()


def seed_from_json_if_empty() -> None:
    """If the books table is empty and data.json exists, import rows once."""
    if db.session.query(Book).first() is not None:
        return
    data_file = BASE_DIR / "data.json"
    if not data_file.is_file():
        return
    try:
        raw: list[dict] = json.loads(data_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return
    for row in raw:
        book = Book(
            isbn=str(row.get("isbn", "") or ""),
            title=str(row.get("title", "") or ""),
            author=str(row.get("author", "") or ""),
            genre=str(row.get("genre", "") or ""),
            pages=int(row.get("pages", 0) or 0),
            is_read=bool(row.get("is_read", False)),
            rating=float(row.get("rating", 0.0) or 0.0),
        )
        db.session.add(book)
    db.session.commit()


def init_database() -> None:
    """Create tables and optional seed whenever the app module loads (any launcher)."""
    with app.app_context():
        db.create_all()
        seed_from_json_if_empty()


init_database()


@app.route("/")
def index() -> str:
    """Main route: home page. Query all books from SQLite, pass to template."""
    books = _all_books_ordered()
    preview_books = books[:5]
    return render_template("index.html", books=books, preview_books=preview_books)


@app.route("/books")
@app.route("/items")
def list_books() -> str:
    """List all books from the database via SQLAlchemy."""
    books = _all_books_ordered()
    return render_template("books.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add() -> str:
    """Display and process the add-book form."""
    if request.method == "POST":
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

        book = Book(
            isbn=isbn,
            title=title,
            author=author,
            genre=genre,
            pages=pages,
            is_read=is_read,
            rating=rating,
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("list_books"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
