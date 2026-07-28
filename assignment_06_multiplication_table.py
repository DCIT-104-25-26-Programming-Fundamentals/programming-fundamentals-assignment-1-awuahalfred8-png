# Part A: Print a single multiplication table
def print_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# Part B: Print multiplication tables from 1 to N
def print_tables_up_to(n):
    for number in range(1, n + 1):
        print_table(number)
        print("---------------------------")


# Main program

# Part A
number = int(input("Enter a number: "))

if number <= 0:
    print("Error: Number must be a positive integer.")
else:
    print_table(number)

    # Part B
    n = int(input("\nEnter a number N: "))

    if n <= 0:
        print("Error: Number must be a positive integer.")
    else:
        print_tables_up_to(n)