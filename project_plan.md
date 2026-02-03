# Project Plan: Personal Library Manager (v2.0)

## Section 1: Project Overview
**Project Title:** Personal Library Manager
**Development Methodology:** AI-Assisted Iterative Prototyping

**Summary:**
The Personal Library Manager is a Python-based CLI (Command Line Interface) application designed to help readers organize their book collections. While the initial concept focused on manual entry, this evolved version leverages open APIs to automate data entry and ensures data persistence between sessions. The application serves as a centralized tool for tracking inventory and reading progress, designed for users who want a lightweight, distraction-free management tool with modern conveniences.

## Section 2: Core Features (Evolution & Maturity)
The feature set has been expanded from simple list management to include automation and persistence, transforming the tool from a temporary script into a usable application.

* **Smart Add via ISBN (New):**
    The user can input a book's ISBN (e.g., 9780140328721). The application will query the Open Library API to automatically retrieve and populate the Title, Author, and Page Count. The user can confirm or edit these details before saving. *Fallback: Manual entry is available if offline.*
* **Data Persistence (New):**
    The application will automatically load the library inventory from a local JSON file upon startup and save any changes to the file upon exit. This ensures the user's library is not lost when the program closes.
* **Analytics Dashboard (New):**
    A new menu option that calculates and displays key metrics, such as "Total Books Owned," "Total Pages Read," and "Completion Rate %."
* **Search by Author:**
    The user can input an author's name to retrieve and display all books in the library associated with that specific author.
* **Update Reading Status:**
    The user can select a specific book from their collection and toggle its status from "Unread" to "Read."
* **Remove a Book:**
    The user can permanently delete a book record from the library.

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

## Section 4: Development Strategy & Tools
This project utilizes modern AI-assisted workflows to accelerate development and ensure code quality despite the timeline constraints.

**Primary IDE:** Cursor (VS Code fork with integrated LLM capabilities).

**Implementation Strategy:**
1.  **Code Generation:** Cursor will be utilized to generate boilerplate code for file I/O (handling the JSON save/load cycle) and to construct the specific HTTP requests required for the Open Library API.
2.  **Refactoring & Optimization:** AI tools will be used to review code blocks for efficiency (e.g., converting standard loops to list comprehensions for the search features) and ensuring PEP 8 style compliance.
3.  **Debugging:** Runtime errors will be diagnosed using AI context awareness to rapidly identify logic gaps or data type mismatches, particularly when parsing the JSON response from the API.