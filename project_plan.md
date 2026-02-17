# Project Plan: Personal Library Manager (v2.1)

## Section 1: Project Overview
**Project Title:** Personal Library Manager
**Development Methodology:** AI-Assisted Iterative Prototyping

**Summary:**
The Personal Library Manager is a Python-based CLI (Command Line Interface) application designed to help readers organize their book collections. While the initial concept focused on manual entry, this evolved version leverages open APIs to automate data entry and ensures data persistence between sessions. The application serves as a centralized tool for tracking inventory and reading progress, designed for users who want a lightweight, distraction-free management tool with modern conveniences. Following an incremental approach, a minimal Flask web interface has been introduced to explore browser-based access, with the CLI remaining the primary interface for the current iteration.

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

### Interface Evolution (v2.1)
*The introduction of a Flask web app (`web_app.py`) represents an incremental pivot toward browser-based access.*

**Current State:**
- **CLI (`app.py`):** Primary interface; full menu-driven functionality.
- **Web (`web_app.py`):** Minimal Flask app serving a single route ("Hello, Web!") at http://127.0.0.1:5000/.

**Planned Next Step (Incremental):**
Share the existing `data.json` persistence with the web app. Add a `/library` route that loads and returns the library as JSON. This establishes the data bridge without duplicating persistence logic and sets the stage for future web-based list/add flows.

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
4.  **Dual-Interface Development:** New features will be designed so they can serve both CLI and web clients (e.g., shared logic in services/modules). The Flask app will gradually adopt routes that mirror CLI actions, starting with read-only operations (e.g., viewing the library).