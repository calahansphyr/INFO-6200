"""SQLAlchemy models for the Personal Library Manager."""

from __future__ import annotations

from extensions import db


class Book(db.Model):
    """A single book record matching the project plan data model."""

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(20), nullable=False, default="")
    title = db.Column(db.String(255), nullable=False, default="")
    author = db.Column(db.String(255), nullable=False, default="")
    genre = db.Column(db.String(128), nullable=False, default="")
    pages = db.Column(db.Integer, nullable=False, default=0)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)
