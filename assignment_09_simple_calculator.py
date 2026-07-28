# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


# Function for modulus
def modulus(a, b):
    if b == 0:
        return None
    return a % b


# Function for exponentiation
def exponent(a, b):
    return a ** b


# Function to display the menu
def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# Main Program
while True:
    display_menu()

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: Invalid choice.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")

    elif choice == "2":
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

    elif choice == "3":
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

    elif choice == "4":
        result = divide(num1, num2)
        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {num1} / {num2} = {result}")

    elif choice == "5":
        result = modulus(num1, num2)
        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {num1} % {num2} = {result}")

    elif choice == "6":
        print(f"Result: {num1} ** {num2} = {exponent(num1, num2)}")