# AI Calculator

A simple calculator application built with Python and tkinter.

## Requirements

This project uses only Python standard library modules. No external dependencies are required.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

**Entry Point:** Run `python calculator.py` to start the calculator program.

## AI Collaboration Log

### Prompt: Fix calculator errors and rewrite ai_calculator.py

**My Prompt:** I asked the AI to fix errors in my calculator application and rewrite the `ai_calculator.py` file to make it functional.

**AI's Response:** The AI identified that the original calculator code had several issues including incorrect method implementations and widget management problems. The AI completely rewrote the calculator using a cleaner architecture with proper indentation including:
- A `Calculator` class that properly manages the GUI using tkinter and ttk
- A string-based expression system (`self.expression`) that accumulates button presses
- Proper use of `StringVar` for managing the display text
- A simplified button creation loop that handles the layout programmatically
- Error handling in the `calculate()` method using try/except blocks

**How It Helped:** The AI's response solved the core functionality issues by restructuring the entire calculator implementation. The new code eliminated the errors I was experiencing and created a working calculator that properly handles button presses, displays expressions, performs calculations, and handles errors gracefully. This rewrite made the calculator fully functional and ready for use.
