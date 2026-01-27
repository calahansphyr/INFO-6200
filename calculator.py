def get_number(prompt):
    """Prompt user for a number and validate input."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def get_operation():
    """Prompt user for an operation and validate input."""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in valid_operations:
            return operation
        else:
            print("Error: Please enter a valid operation (+, -, *, /).")


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
    
    # Get first number
    first_number = get_number("Enter first number: ")
    
    # Get operation
    operation = get_operation()
    
    # Get second number
    second_number = get_number("Enter second number: ")
    
    # Perform calculation with error handling
    try:
        result = calculate(first_number, operation, second_number)
        print("-" * 40)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == '__main__':
    main()
