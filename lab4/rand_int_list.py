# Import the random module to generate random numbers
import random

# Take input from the user for the number of even numbers to generate
n = int(input("n="))

# Initialize an empty list to store the even numbers
list = []

# Start an infinite loop to generate random numbers
while True:
    # If the length of the list is equal to 'n', stop the loop
    if len(list) == n:
        break
    
    # Generate a random integer between 1 and 10 (inclusive)
    x = random.randint(1, 10)
    
    # If the number is even, add it to the list
    if x % 2 == 0:
        list.append(x)

# After the loop ends, print the list of even numbers
print(list)
