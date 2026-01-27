# AI Calculator

A simple command-line calculator application built with Python. The program sequentially prompts the user for a first number, an arithmetic operation, and a second number, then displays the result.

## Requirements

This project uses only Python standard library modules. No external dependencies are required.

The calculator sequentially prompts the user for:
1. First number
2. Arithmetic operation (+, -, *, /)
3. Second number

It then calculates and displays the result, with proper error handling for invalid inputs and division by zero.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

**Entry Point:** Run `python calculator.py` to start the calculator program.

## AI Collaboration Log

### Prompt: Fix calculator errors and rewrite calculator.py

**My Prompt:** My calculator is broken. Please fix it.

**AI's Response:** The AI identified several issues in the original calculator code, such as incorrect method implementations and widget management problems. The AI completely rewrote the calculator using a cleaner architecture with proper indentation, including:
- Separate functions for getting user input (`get_number()` and `get_operation()`)
- A `calculate()` function that handles all four operations (+, -, *, /)
- Proper error handling with specific, friendly error messages
- A clear `main()` function that orchestrates the sequential prompts
- Input validation loops that reprompt until valid input is received

**How It Helped:** The AI's response solved the core functionality issues by restructuring the entire calculator implementation. The new code eliminated the errors I was experiencing and created a working calculator that properly handles user input, performs calculations, and handles errors gracefully. The sequential prompting system works exactly as required by the assignment rubric, and the error handling provides specific, user-friendly messages for both error cases (non-numeric input and division by zero). This rewrite made the calculator fully functional and ready for use. Given my lack of experience with Python, this was crucial.

Using AI to rebuild the GUI flow showed me how to structure tkinter apps cleanly while still meeting the assignment’s launch-from-CLI requirement.