# Project Plan: Personal Library Manager (v2.1)

## Section 1: Project Overview
**Project Title:** Personal Library Manager
**Development Methodology:** AI-Assisted Iterative Prototyping

**Summary:**
The Personal Library Manager is a Python-based CLI (Command Line Interface) application designed to help readers organize their book collections. While the initial concept focused on manual entry, this evolved version leverages open APIs to automate data entry and ensures data persistence between sessions. The application serves as a centralized tool for tracking inventory and reading progress, designed for users who want a lightweight, distraction-free management tool with modern conveniences. Following an incremental approach, a minimal Flask web interface was initially introduced to explore browser-based access, with the CLI remaining the primary interface. In the latest iteration, this web interface has matured into a fully functional add-book form that reuses the same persistent JSON data store as the CLI, demonstrating how the project’s planning and architecture support continuous improvement over time.

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

* **Web-based Add Book Form (New – Assignment 7):**
    A Flask-powered `/add` route now presents an HTML form that collects all user-facing fields of the `Book` model (ISBN, Title, Author, Genre, Pages, Read status, and Rating). When submitted, the form issues a POST request to the same route, where the server validates and structures the data into a `Book` dictionary, assigns a new sequential `id`, appends it to the in-memory library, and persists the updated collection back to `data.json`. After a successful save, the user is redirected to a page that lists all books, creating a cohesive web-based flow that mirrors and extends the original CLI-driven experience.

* **Bringing Your Data to the Web (Assignment 9):**
    The Flask app exposes main routes (`/`, `/books`, and `/items`) that handle GET requests. Each list route calls `load_library()` (from `app.py`) to read and parse all data from the persistent `data.json` file, then passes the resulting collection to `render_template()`. The Jinja2 template (`templates/books.html`) receives this data collection, uses a `{% for book in books %}` loop to iterate through it, and generates HTML (a table) to display the details of each item—id, title, author, genre, pages, read status, rating, and ISBN—in a readable format. This single template plus server-side data replaces the need for many static HTML pages; one dynamic page is driven by the current contents of the JSON "database."

### Interface Evolution (v2.1)
*The introduction of a Flask web app (`web_app.py`) represents an incremental pivot toward browser-based access.*

**Current State:**
- **CLI (`app.py`):** Primary interface; full menu-driven functionality.
- **Web (`web_app.py`):** Flask app that exposes a main route (`/`), list routes (`/books`, `/items`) that read/parse `data.json` and pass the collection to Jinja2, and an `/add` route that serves and processes an HTML form for creating new `Book` records. The templates folder contains `index.html`, `books.html` (list view with for-loop over items), and `add.html`.

**Planned Next Step (Incremental):**
Continue expanding the web interface so that more CLI features are available in the browser. Near-term iterations (v2.2 and beyond) will focus on adding read-only and mutating operations that parallel the CLI menu, such as viewing analytics, searching by author, and toggling the read status directly from the web UI. Over time, the plan is to refactor shared logic (e.g., persistence and business rules) into reusable modules so that both the CLI and Flask layers can evolve without duplication, preserving a clear trajectory of improvement from simple scripts to a multi-interface application.

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

**Current Implementation (CLI):** The application stores each book as a Python dictionary with all 8 keys. When adding a book, the user provides only `title`, `author`, and `pages`. The remaining fields are auto-populated: `id` (sequential integer), `isbn` and `genre` (empty strings), `is_read` (`False`), and `rating` (`0.0`).

## Section 4: Development Strategy & Tools
This project utilizes modern AI-assisted workflows to accelerate development and ensure code quality despite the timeline constraints.

**Primary IDE:** Cursor (VS Code fork with integrated LLM capabilities).

**Implementation Strategy:**
1.  **Code Generation:** Cursor will be utilized to generate boilerplate code for file I/O (handling the JSON save/load cycle) and to construct the specific HTTP requests required for the Open Library API.
2.  **Refactoring & Optimization:** AI tools will be used to review code blocks for efficiency (e.g., converting standard loops to list comprehensions for the search features) and ensuring PEP 8 style compliance.
3.  **Debugging:** Runtime errors will be diagnosed using AI context awareness to rapidly identify logic gaps or data type mismatches, particularly when parsing the JSON response from the API.
4.  **Dual-Interface Development:** New features will be designed so they can serve both CLI and web clients (e.g., shared logic in services/modules). The Flask app will gradually adopt routes that mirror CLI actions, starting with read-only operations (e.g., viewing the library) and then expanding to full create/update/delete flows, such as the new web-based add-book form.
5.  **Iterative Planning & Continuous Improvement:** Each assignment iteration intentionally pushes the design forward—from a basic CLI, to persistent storage and API integration, to a shared web interface that reuses the same `load_library()` / `save_library()` persistence logic. This incremental planning approach ensures that changes are small, testable, and traceable in the project documentation, making the evolution of the system explicit rather than accidental.

## Assignment 9 Deliverables (Bringing Your Data to the Web)
- **Updated Flask application:** `web_app.py` — main route (`/`) and list routes (`/books`, `/items`) handle GET, read/parse `data.json` via `load_library()`, and pass the data collection to `render_template()`.
- **Templates folder:** Contains `books.html` (and `index.html`, `add.html`). `books.html` receives the collection, uses a Jinja2 `{% for book in books %}` loop, and generates HTML to display the details of each item in a readable table.
- **Updated project plan:** This document (`project_plan.md`) includes the above feature description and deliverables.