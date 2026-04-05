"""SQLAlchemy models for the Personal Library Manager."""

from __future__ import annotations
import os

from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


def get_cipher() -> Fernet | None:
    """Retrieve the Fernet cipher using the environment key."""
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        return None
    return Fernet(key.encode("utf-8"))


class User(db.Model):
    """User model for authentication and data ownership."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    books = db.relationship("Book", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Book(db.Model):
    """A single book record matching the project plan data model."""

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Ownership
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="books")

    # Encrypted fields (stored as relatively long strings since Fernet expands size)
    _isbn = db.Column("isbn", db.String(255), nullable=False, default="")
    _title = db.Column("title", db.String(512), nullable=False, default="")
    _author = db.Column("author", db.String(512), nullable=False, default="")
    _genre = db.Column("genre", db.String(255), nullable=False, default="")
    
    # Numerical / Boolean fields (not encrypted)
    pages = db.Column(db.Integer, nullable=False, default=0)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)

    # --- Properties for Encryption/Decryption ---

    @property
    def isbn(self) -> str:
        cipher = get_cipher()
        if not cipher or not self._isbn:
            return self._isbn
        try:
            return cipher.decrypt(self._isbn.encode("utf-8")).decode("utf-8")
        except Exception:
            return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        cipher = get_cipher()
        if cipher and value:
            self._isbn = cipher.encrypt(value.encode("utf-8")).decode("utf-8")
        else:
            self._isbn = value

    @property
    def title(self) -> str:
        cipher = get_cipher()
        if not cipher or not self._title:
            return self._title
        try:
            return cipher.decrypt(self._title.encode("utf-8")).decode("utf-8")
        except Exception:
            return self._title

    @title.setter
    def title(self, value: str) -> None:
        cipher = get_cipher()
        if cipher and value:
            self._title = cipher.encrypt(value.encode("utf-8")).decode("utf-8")
        else:
            self._title = value

    @property
    def author(self) -> str:
        cipher = get_cipher()
        if not cipher or not self._author:
            return self._author
        try:
            return cipher.decrypt(self._author.encode("utf-8")).decode("utf-8")
        except Exception:
            return self._author

    @author.setter
    def author(self, value: str) -> None:
        cipher = get_cipher()
        if cipher and value:
            self._author = cipher.encrypt(value.encode("utf-8")).decode("utf-8")
        else:
            self._author = value

    @property
    def genre(self) -> str:
        cipher = get_cipher()
        if not cipher or not self._genre:
            return self._genre
        try:
            return cipher.decrypt(self._genre.encode("utf-8")).decode("utf-8")
        except Exception:
            return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        cipher = get_cipher()
        if cipher and value:
            self._genre = cipher.encrypt(value.encode("utf-8")).decode("utf-8")
        else:
            self._genre = value
