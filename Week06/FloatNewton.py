# Newton method for estimating squareroots
# This program takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Michael Lawal
# Reference: Newton-Raphson method for approximating square roots, iterative numerical methods.

def sqrt(x):
    # Initial guess (we can use x / 2 as a reasonable starting point)
    guess = x / 2.0

    # Tolerance level for stopping the iteration
    tolerance = 1e-10
    
    # Loop to improve the guess until the result is accurate enough
    while True:
        # Newton's method for square roots
        new_guess = 0.5 * (guess + x / guess)
        
        # Check if the difference between the old and new guess is within the tolerance
        if abs(guess - new_guess) < tolerance:
            return new_guess
        
        guess = new_guess

# Example usage:
num = float(input("Enter a positive floating-point number: "))
print(f"The approximate square root of {num} is {sqrt(num)}")
