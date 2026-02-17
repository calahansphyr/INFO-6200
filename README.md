# Personal Library Manager

A Python project including a command-line Personal Library Manager and a minimal Flask web application. The library manager stores books in a JSON file and provides a menu-driven interface to add and list books.

## Project Structure

- **app.py** — Personal Library Manager (command-line). Stores books in `data.json` and provides options to add books, list all books, and exit.
- **web_app.py** — Minimal Flask web server. Displays "Hello, Web!" at the root URL.

## Requirements

- **app.py** uses only Python standard library modules (no external dependencies).
- **web_app.py** requires Flask. See `requirements.txt`.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Applications

### Personal Library Manager (command-line)

```bash
python app.py
```

Menu options:
1. Add a Book (title, author, page count)
2. List all Books
3. Exit

Data is persisted in `data.json` in the project directory.

### Flask Web App

```bash
python web_app.py
```

Then open http://127.0.0.1:5000/ in your browser.
