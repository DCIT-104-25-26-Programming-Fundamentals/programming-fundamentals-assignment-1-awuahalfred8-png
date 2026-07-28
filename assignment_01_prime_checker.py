# Function to check whether a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for factors from 2 up to number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    # If no factors were found, the number is prime
    return True


# Main program
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is NOT a prime number.")