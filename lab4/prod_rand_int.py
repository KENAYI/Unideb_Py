# Import the random module to generate random numbers
import random

# Take input from the user for the number of random numbers to generate
n = int(input("n = "))

# Initialize a variable 'p' to store the product of the numbers
p = 1

# Loop through a range of numbers from 1 to n (inclusive)
for i in range(1, n + 1):
    # Generate a random integer between 1 and 10 (inclusive)
    x = random.randint(1, 10)
    
    # Print the random number with a space between them
    print(x, end=' ')
    
    # Multiply the product 'p' by the random number 'x'
    p = p * x

# After the loop, print the final product of all the numbers
print("\nProduct = ", p)
