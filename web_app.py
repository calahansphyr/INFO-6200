"""
Personal Library Manager - Flask Web Interface

To run:
  1. pip install -r requirements.txt
  2. python web_app.py
Then open http://127.0.0.1:5000/
"""
from __future__ import annotations

import json
import os
from functools import wraps
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for, session, jsonify, flash, abort

from extensions import db
from models import Book, User

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URI", f"sqlite:///{BASE_DIR / 'project.db'}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# --- Authentication Helpers ---

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# --- Database Setup & Seeding ---

def _all_books_ordered() -> list[Book]:
    user_id = session.get("user_id")
    if not user_id:
        return []
    return db.session.query(Book).filter_by(user_id=user_id).order_by(Book.id).all()


def seed_from_json_if_empty() -> None:
    """If the books table is empty and data.json exists, import rows once."""
    if db.session.query(Book).first() is not None:
        return
        
    # We must have a user to own the seed data
    admin = db.session.query(User).filter_by(username="admin").first()
    if not admin:
        admin = User(username="admin")
        admin.set_password("admin")
        db.session.add(admin)
        db.session.commit()

    data_file = BASE_DIR / "data.json"
    if not data_file.is_file():
        return
    try:
        raw: list[dict] = json.loads(data_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return
    for row in raw:
        book = Book(
            user_id=admin.id,
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
    with app.app_context():
        db.create_all()
        seed_from_json_if_empty()

init_database()


# --- Context Processors ---

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    user = db.session.get(User, user_id) if user_id else None
    return dict(current_user=user)


# --- Authentication Routes ---

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for("register"))

        if db.session.query(User).filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = db.session.query(User).filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


# --- Web Application Routes ---

@app.route("/")
def index() -> str:
    if "user_id" not in session:
        return redirect(url_for("login"))
    books = _all_books_ordered()
    preview_books = books[:5]
    return render_template("index.html", books=books, preview_books=preview_books)


@app.route("/books")
@app.route("/items")
@login_required
def list_books() -> str:
    books = _all_books_ordered()
    return render_template("books.html", books=books)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add() -> str:
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
            user_id=session["user_id"],
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


@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
@login_required
def edit_book(item_id: int):
    book = db.session.query(Book).filter_by(id=item_id, user_id=session["user_id"]).first()
    if not book:
        return redirect(url_for("list_books"))
        
    if request.method == "POST":
        book.isbn = request.form.get("isbn", "").strip()
        book.title = request.form.get("title", "").strip()
        book.author = request.form.get("author", "").strip()
        book.genre = request.form.get("genre", "").strip()
        
        pages_raw = request.form.get("pages", "").strip()
        rating_raw = request.form.get("rating", "").strip()
        book.is_read = request.form.get("is_read") is not None

        try:
            book.pages = int(pages_raw) if pages_raw else 0
        except ValueError:
            book.pages = 0

        try:
            book.rating = float(rating_raw) if rating_raw else 0.0
        except ValueError:
            book.rating = 0.0

        db.session.commit()
        return redirect(url_for("list_books"))

    return render_template("edit.html", book=book)


@app.route("/delete/<int:item_id>", methods=["POST"])
@login_required
def delete_book(item_id: int):
    book = db.session.query(Book).filter_by(id=item_id, user_id=session["user_id"]).first()
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for("list_books"))


# --- RESTful API Routes ---

@app.route("/api/v1/items", methods=["GET"])
@login_required
def api_get_items():
    books = _all_books_ordered()
    data = []
    for book in books:
        data.append({
            "id": book.id,
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "pages": book.pages,
            "is_read": book.is_read,
            "rating": book.rating
        })
    return jsonify(data)


@app.route("/api/v1/items/<int:item_id>", methods=["GET"])
@login_required
def api_get_item(item_id: int):
    book = db.session.query(Book).filter_by(id=item_id, user_id=session["user_id"]).first()
    if not book:
        abort(404, description="Item not found or you don't have access")
        
    return jsonify({
        "id": book.id,
        "isbn": book.isbn,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "pages": book.pages,
        "is_read": book.is_read,
        "rating": book.rating
    })


if __name__ == "__main__":
    app.run(debug=True)
