# Project Plan: Personal Library Manager

## Section 1: Project Overview
**Project Title:** Personal Library Manager

**Summary:**
The Personal Library Manager is a Python-based application designed to help readers organize their physical and/or digital book collections. The application's purpose is to replace disorganized notes or spreadsheets with a centralized tool for tracking book inventory and reading progress. The intended user is an individual who needs a simple, text-based interface to quickly log books they own, filter them by reading status, and manage their personal reading goals without requiring complex software or an internet connection.

## Section 2: Core Features
* **Add a New Book:** The user can input essential details (Title, Author, Genre) to append a new book record to their library.
* **View Library Inventory:** The user can display a full list of their saved books, with options to filter the view by "Read" or "Unread" status.
* **Search by Author:** The user can input an author's name to retrieve and display all books in the library associated with that specific author.
* **Update Reading Status:** The user can select a specific book from their collection and toggle its status from "Unread" to "Read."
* **Remove a Book:** The user can permanently delete a book record from the library if it is lost, donated, or no longer needed.

## Section 3: Data Model
**Record Entity:** `Book`

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | A unique identifier for the book (e.g., 101). |
| `title` | String | The full title of the book. |
| `author` | String | The name of the author. |
| `genre` | String | The category of the book (e.g., "Non-Fiction", "Sci-Fi"). |
| `pages` | Integer | The total number of pages in the book. |
| `is_read` | Boolean | A True/False flag indicating if the book has been completed. |
| `rating` | Float | A 0.0 to 5.0 star rating (optional, defaults to 0.0 if unread). |
