# Function to calculate the sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function to calculate the average
def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function to find the maximum value
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# Function to find the minimum value
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# Main program
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Number of values must be greater than 0.")
else:
    numbers = []

    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    print("\nResults:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))