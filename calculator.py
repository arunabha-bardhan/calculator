def add_two_numbers(num1, num2):
    return num1 + num2

def subtract_two_numbers(num1, num2):
    return num1 - num2

def multiply_two_numbers(num1, num2):
    return num1 * num2

def calculator():
    print("Welcome to the calculator! You can calculate two numbers here")
    try:
        operation = input("Enter 'add' to add or 'subtract' to subtract or 'multiply' to multiply two numbers: ").strip().lower()
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 'add':
            result = add_two_numbers(num1, num2)
            print(f"The sum of {num1} and {num2} is {result}")
        elif operation == 'subtract':
            result = subtract_two_numbers(num1, num2)
            print(f"The difference between {num1} and {num2} is {result}")
        elif operation == 'multiply':
            result = multiply_two_numbers(num1, num2)
            print(f"The multiplication between {num1} and {num2} is {result}")
        else:
            print("Invalid operation. Please enter 'add' or 'subtract'.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


