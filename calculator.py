
# calculator.py
# This script provides a simple command-line calculator that can perform addition, subtraction,
# multiplication, and division.

def add():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")


def subtract():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        result = num1 - num2
        print(f"The result of subtracting {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def multiply():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def divide():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")



def home():
    while True:
        print("\n")
        print("#######################")
        print("Welcome to the Calculator!")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("#######################")
        print("\n")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    home()

