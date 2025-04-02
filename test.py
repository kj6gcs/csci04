def operatorValidation(num1, num2, operator):
    """Performs the math operation and returns the equation as a formatted string."""
    if operator == '+':  # Addition
        return f"{num1} + {num2} = {num1 + num2}"
    elif operator == '-':  # Subtraction
        return f"{num1} - {num2} = {num1 - num2}"
    elif operator == '*':  # Multiplication
        return f"{num1} * {num2} = {num1 * num2}"
    elif operator == '/':  # Division
        if num2 == 0:
            return "Are you trying to implode the universe? You can't divide by zero!"  # Fun Easter egg
        return f"{num1} / {num2} = {num1 / num2}"
    else:
        return "You can only enter the following operators: +, -, *, /"


def calculations():
    """Loops through user input and performs calculations until the user quits."""
    while True:
        num1 = input("Enter the first number or 'q' to quit: ")
        if num1.lower() == 'q':
            print("Exiting Program")
            break

        num2 = input("Enter the second number or 'q' to quit: ")
        if num2.lower() == 'q':
            print("Exiting Program")
            break

        operator = input("Enter a valid operator (+, -, *, /) or 'q' to quit: ")
        if operator.lower() == 'q':
            print("Exiting Program")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
            result = operatorValidation(num1, num2, operator)
            print(result)  # Prints the full equation
        except ValueError:
            print("Error: Please enter valid numbers.")

# Welcome message
print("\n>>> Simple Calculator <<<\n")
print(">>> You will enter your first number, second number, and then the operator to use <<<\n")
print(">>> Enter 'q' at any point to quit the program <<<\n")
print(">>> Only +, -, *, and / are valid operators <<<\n")

# Start calculator
calculations()

