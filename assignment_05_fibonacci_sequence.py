# Part A: Print the first N Fibonacci terms
def print_fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


# Part B: Check if a number is a Fibonacci number
def is_fibonacci(number):
    if number < 0:
        return False

    a = 0
    b = 1

    while a < number:
        c = a + b
        a = b
        b = c

    return a == number


# Main program
n = int(input("How many terms? "))

if n <= 0:
    print("Error: Number of terms must be greater than 0.")
else:
    print_fibonacci(n)

number = int(input("Enter a number to check: "))

if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is NOT a Fibonacci number.")