# Project Plan: Personal Library Manager (v2.2)

## Section 1: Project Overview
**Project Title:** Personal Library Manager
**Development Methodology:** AI-Assisted Iterative Prototyping

**Summary:**
The Personal Library Manager is a Python-based CLI (Command Line Interface) application designed to help readers organize their book collections. While the initial concept focused on manual entry, this evolved version leverages open APIs to automate data entry and ensures data persistence between sessions. The application serves as a centralized tool for tracking inventory and reading progress, designed for users who want a lightweight, distraction-free management tool with modern conveniences. Following an incremental approach, a minimal Flask web interface was initially introduced to explore browser-based access, with the CLI remaining the primary interface. The web layer now persists books in a **SQLite** database (`project.db`) using the **SQLAlchemy** ORM via Flask-SQLAlchemy, while the CLI continues to use the shared JSON file (`data.json`) for backward compatibility. This demonstrates how the project’s planning and architecture support continuous improvement over time—from flat files to relational storage for the web tier.

## Section 2: Core Features (Evolution & Maturity)
The feature set has been expanded from simple list management to include automation and persistence, transforming the tool from a temporary script into a usable application.

**Currently Implemented:**
* **Add a Book:** Manual entry of title, author, and page count. Each book is stored as a dictionary using the full 8-field data model (see Section 3); fields not collected from the user are populated with sensible defaults.
* **List all Books:** Iterates through the master list of book dictionaries and displays each entry in a human-readable format.
* **Exit:** Graceful exit from the application.

* **Smart Add via ISBN (New):**
    The user can input a book's ISBN (e.g., 9780140328721). The application will query the Open Library API to automatically retrieve and populate the Title, Author, and Page Count. The user can confirm or edit these details before saving. *Fallback: Manual entry is available if offline.*
* **Data Persistence (New - Assignment 6 Implemented):**
    The application automatically loads the library inventory from a local JSON file (e.g., `data.json`) on startup. If the file does not exist, it starts with an empty library without crashing. Whenever the data is modified (e.g., a book is added), the updated data set is **immediately** written back to the file in a structured, human-readable JSON format. This ensures the user's library persists between sessions and avoids data loss.
* **Analytics Dashboard (New):**
    A new menu option that calculates and displays key metrics, such as "Total Books Owned," "Total Pages Read," and "Completion Rate %."
* **Search by Author:**
    The user can input an author's name to retrieve and display all books in the library associated with that specific author.
* **Update Reading Status:**
    The user can select a specific book from their collection and toggle its status from "Unread" to "Read."
* **Remove a Book:**
    The user can permanently delete a book record from the library.

* **Web-based Add Book Form (Assignment 7; storage updated in Assignment 10):**
    A Flask-powered `/add` route presents an HTML form that collects all user-facing fields of the `Book` model (ISBN, Title, Author, Genre, Pages, Read status, and Rating). When submitted, the server validates the input, builds a SQLAlchemy `Book` instance, adds it to the database session, commits to SQLite, and redirects to the list view. (Earlier iterations used dictionaries and `data.json`; the web tier now uses the ORM.)

* **Web-based CRUD (Assignment 11):**
    The app implements full CRUD logic via dynamic routes: `/edit/<int:item_id>` retrieves a single book and renders a pre-populated form allowing details to be modified and committed to SQLite, while `/delete/<int:item_id>` removes the record from the database. UI controls on the main table seamlessly trigger these update and delete actions.

* **Bringing Your Data to the Web (Assignment 9; queries updated in Assignment 10):**
    The Flask app exposes main routes (`/`, `/books`, and `/items`) that handle GET requests. List routes query all `Book` rows from SQLite via SQLAlchemy (e.g., `select(Book).order_by(Book.id)`) and pass the resulting objects to `render_template()`. The Jinja2 template (`templates/books.html`) uses a `{% for book in books %}` loop to render id, title, author, genre, pages, read status, rating, and ISBN in a table.

* **SQLite & SQLAlchemy Web Persistence (Assignment 10):**
    The Flask app is configured with a SQLite database URI pointing at `project.db`. A declarative `Book` model (in `models.py`) maps the eight project fields to a `books` table. On startup (when running `python web_app.py`), the app creates tables if needed and, if the table is empty, can optionally import existing rows from `data.json` so legacy sample data appears in the database without manual SQL.

### Interface Evolution (v2.2)
*The introduction of a Flask web app (`web_app.py`) represents an incremental pivot toward browser-based access.*

**Current State:**
- **CLI (`app.py`):** Primary interface; full menu-driven functionality; persists to `data.json`.
- **Web (`web_app.py`):** Flask app with Flask-SQLAlchemy; main route (`/`), list routes (`/books`, `/items`) that query SQLite for all `Book` rows, and `/add` that creates and commits ORM instances. Shared templates: `index.html`, `books.html`, `add.html`. Supporting modules: `extensions.py` (database handle), `models.py` (`Book` model).

**Planned Next Step (Incremental):**
Continue expanding the web interface so that more CLI features are available in the browser. Near-term iterations will focus on read-only and mutating operations that parallel the CLI menu (e.g., analytics, search by author, toggling read status in the UI). Optionally unify CLI persistence with the same SQLite database so both interfaces share one source of truth.

## Section 3: Data Model
**Record Entity:** `Book`
The data model has been updated to support API integration and persistent storage.


| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | A unique identifier for the book (e.g., 101). |
| `isbn` | String | The 10 or 13 digit ISBN used for API lookup (New). |
| `title` | String | The full title of the book. |
| `author` | String | The name of the author. |
| `genre` | String | The category of the book. |
| `pages` | Integer | The total number of pages in the book. |
| `is_read` | Boolean | A True/False flag indicating if the book has been completed. |
| `rating` | Float | A 0.0 to 5.0 star rating (optional, defaults to 0.0). |

**Current Implementation (CLI):** The application stores each book as a Python dictionary with all 8 keys in `data.json`. When adding a book, the user provides only `title`, `author`, and `pages`. The remaining fields are auto-populated: `id` (sequential integer), `isbn` and `genre` (empty strings), `is_read` (`False`), and `rating` (`0.0`).

**Web Implementation (Flask):** Each book is represented by the SQLAlchemy `Book` model mapped to the `books` table in `project.db`. The primary key `id` is auto-generated by SQLite. List and add routes use the ORM session (`db.session`) for queries and commits.

## Section 4: Development Strategy & Tools
This project utilizes modern AI-assisted workflows to accelerate development and ensure code quality despite the timeline constraints.

**Primary IDE:** Cursor (VS Code fork with integrated LLM capabilities).

**Implementation Strategy:**
1.  **Code Generation:** Cursor will be utilized to generate boilerplate code for file I/O (handling the JSON save/load cycle) and to construct the specific HTTP requests required for the Open Library API.
2.  **Refactoring & Optimization:** AI tools will be used to review code blocks for efficiency (e.g., converting standard loops to list comprehensions for the search features) and ensuring PEP 8 style compliance.
3.  **Debugging:** Runtime errors will be diagnosed using AI context awareness to rapidly identify logic gaps or data type mismatches, particularly when parsing the JSON response from the API.
4.  **Dual-Interface Development:** New features will be designed so they can serve both CLI and web clients (e.g., shared logic in services/modules). The Flask app will gradually adopt routes that mirror CLI actions, starting with read-only operations (e.g., viewing the library) and then expanding to full create/update/delete flows, such as the new web-based add-book form.
5.  **Iterative Planning & Continuous Improvement:** Each assignment iteration intentionally pushes the design forward—from a basic CLI, to persistent JSON storage, to a web interface that initially reused `load_library()` / `save_library()`, and now to a **SQLite-backed web data layer** with SQLAlchemy. This incremental planning approach keeps changes small, testable, and traceable in the project documentation.

## Assignment 9 Deliverables (Bringing Your Data to the Web)
- **Updated Flask application:** `web_app.py` — list routes and templates as described in Section 2 (superseded for data access by Assignment 10 below).
- **Templates folder:** Contains `books.html` (and `index.html`, `add.html`). `books.html` receives the collection, uses a Jinja2 `{% for book in books %}` loop, and generates HTML to display the details of each item in a readable table.
- **Updated project plan:** This document (`project_plan.md`) includes the above feature description and deliverables.

## Assignment 10 Deliverables (The Great Database Migration)
- **Updated Flask application:** `web_app.py` — SQLite URI configuration, `db.init_app(app)`, `db.create_all()` on startup, list routes that query all `Book` records via SQLAlchemy, and `/add` that constructs a `Book`, `db.session.add(...)`, and `db.session.commit()`.
- **New Python modules:** `extensions.py` (Flask-SQLAlchemy `db` instance), `models.py` (SQLAlchemy `Book` model for the eight fields in Section 3).
- **Dependencies:** `requirements.txt` includes `flask-sqlalchemy`.
- **SQLite database file:** `project.db` — created when the app runs; may contain seeded rows migrated from `data.json` if the table was initially empty.
- **Updated project plan:** This document (`project_plan.md`) describes the SQLite/SQLAlchemy web persistence and these deliverables.

## Assignment 11 Deliverables (Implementing CRUD)
- **Update and Delete Logic:** Added dynamic routes `/edit/<int:item_id>` and `/delete/<int:item_id>` within `web_app.py` extending the app's capability to fully mutate database rows natively through the browser.
- **Updated templates folder:** The `books.html` table features inline edit/delete controls linking to the respective ID-based routes, and the new `edit.html` provides a pre-populated HTML form allowing selective modifications of persistent attributes.
- **Updated project plan:** This document captures the final culmination of the CRUD migration, enabling the web tier to effectively replace the CLI mutators for book records.