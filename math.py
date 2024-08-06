import os
import operator
import time
import art

def clear_screen():
    """Clears the screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

def solve_math_problem(expression):
    """Solves a given math problem."""
    # Define operators
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # Split the expression into components
    tokens = expression.split()
    
    if len(tokens) != 3:
        return "Invalid expression format. Use 'number operator number'."

    num1, op, num2 = tokens
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid numbers. Please enter valid numbers."

    if op not in operators:
        return "Unsupported operator. Use +, -, *, or /."

    # Perform the calculation
    try:
        result = operators[op](num1, num2)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    return f"The result is: {result}"

def main():
    """Main function to run the calculator application."""
    text = "Calculator"
    ascii_art = art.text2art(text)  # Generate ASCII art once
    instructions = (
        "You can solve problems in the format 'number operator number'\n"
        "Supported operators: +, -, *, /"
    )
    
    clear_screen()  # Clear screen 
    print(ascii_art)  # Print ASCII art
    print(instructions)  # Print instructions
    
    while True:
        expression = input("Enter your math problem (or type 'exit' to quit): ")
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = solve_math_problem(expression)
        print(result)
        time.sleep(5)  # delays screen clear
        clear_screen()
        print(ascii_art)  # Print ASCII art again after clearing the screen
        print(instructions)  # Reprint instructions after clearing the screen

if __name__ == "__main__":
    main()
