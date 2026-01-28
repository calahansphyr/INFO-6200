import re


def parse_expression(expression):
    """Parse a calculation expression into first number, operation, and second number."""
    # Remove spaces and trailing = if present
    expression = expression.replace(" ", "").rstrip("=")
    
    # Pattern to match: number, operation, number
    pattern = r'([-+]?\d*\.?\d+)\s*([+\-*/])\s*([-+]?\d*\.?\d+)'
    match = re.match(pattern, expression)
    
    if not match:
        raise ValueError("Invalid expression format. Please use format: number operation number (e.g., 8+10)")
    
    first_number = float(match.group(1))
    operation = match.group(2)
    second_number = float(match.group(3))
    
    return first_number, operation, second_number


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
    """Main calculator function."""
    print("Welcome to the Calculator!")
    print("-" * 40)
    print("Enter your calculation (e.g., 8+10 or 8+10=)")
    print("Type 'quit' or 'exit' to close the calculator")
    print("-" * 40)
    
    while True:
        try:
            expression = input("\nEnter calculation: ").strip()
            
            if not expression:
                print("Error: Please enter a calculation.")
                continue
            
            # Check for exit commands
            if expression.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using the calculator!")
                break
            
            # Parse the expression
            first_number, operation, second_number = parse_expression(expression)
            
            # Perform calculation
            result = calculate(first_number, operation, second_number)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error: Please enter a valid calculation (e.g., 8+10, 5-3, 4*2, 10/2).")


if __name__ == '__main__':
    main()
