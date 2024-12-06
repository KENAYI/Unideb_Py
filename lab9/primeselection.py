import sys
import math

# Function to check if a number is prime
def is_prime(n: int) -> bool:
    # Numbers 0 and 1 are not prime
    if n == 0 or n == 1:
        return False
    
    # Check divisibility from 2 up to the square root of n
    d = 2
    while d <= math.sqrt(n):
        if n % d == 0:  # If n is divisible by d, it's not prime
            return False
        d += 1
    
    # If no divisors were found, n is prime
    return True

# Main function to process the input file and print primes
def main():
    # Open the file provided as a command-line argument
    with open(sys.argv[1]) as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into numbers and strip any extra spaces
            numbers = line.strip().split(' ')
            
            primes = []  # List to store unique prime numbers
            
            # Check each number to see if it's prime
            for number in numbers:
                if is_prime(int(number)) and int(number) not in primes:
                    primes.append(int(number))
            
            # Sort the primes in ascending order
            primes.sort()
            
            # Print the primes as a comma-separated list, or "NOTHING" if no primes
            if primes:
                print(', '.join(str(p) for p in primes))
            else:
                print("NOTHING")

# Ensures the main function runs only when the script is executed directly
if __name__ == '__main__':
    main()
