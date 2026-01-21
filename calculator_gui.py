import tkinter as tk
from tkinter import messagebox, simpledialog

def get_number_gui(root, prompt):
    """Prompt user for a number using GUI dialog and validate input."""
    while True:
        try:
            user_input = simpledialog.askstring("Calculator", prompt)
            if user_input is None:  # User clicked Cancel
                return None
            number = float(user_input)
            return number
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

def get_operation_gui(root):
    """Prompt user for an operation using GUI dialog and validate input."""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = simpledialog.askstring("Calculator", "Enter operation (+, -, *, /):")
        if operation is None:  # User clicked Cancel
            return None
        operation = operation.strip()
        if operation in valid_operations:
            return operation
        else:
            messagebox.showerror("Error", "Please enter a valid operation (+, -, *, /).")

def calculate(first_number, operation, second_number):
    """Perform the calculation based on the operation."""
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_number / second_number

def main():
    """Main calculator function with GUI."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Get first number
    first_number = get_number_gui(root, "Enter first number:")
    if first_number is None:
        return
    
    # Get operation
    operation = get_operation_gui(root)
    if operation is None:
        return
    
    # Get second number
    second_number = get_number_gui(root, "Enter second number:")
    if second_number is None:
        return
    
    # Perform calculation with error handling
    try:
        result = calculate(first_number, operation, second_number)
        messagebox.showinfo("Result", f"Result: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    
    root.destroy()

if __name__ == '__main__':
    main()
