# Collatz
# This program asks users to input any positive integer and outputs the successive values of the calculation
# author: Michael Lawal

# Function to perform the calculation and print the sequence
def collatz_sequence(n):
    # Ensure the input is a positive integer
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Print the starting number
    print(f"Starting with: {n}")
    
    # Continue until the sequence reaches 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If even, divide by 2
        else:
            n = 3 * n + 1  # If odd, multiply by 3 and add 1
        print(n)

# Ask the user for a positive integer
try:
    user_input = int(input("Enter a positive integer: "))
    collatz_sequence(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
