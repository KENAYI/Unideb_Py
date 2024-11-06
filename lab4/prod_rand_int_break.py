# Import the random module to generate random numbers
import random

# Initialize a counter variable 'c' to track the number of steps
c = 0

# Start an infinite loop to generate random numbers
while True:
    # Generate a random integer between 1 and 10 (inclusive)
    x = random.randint(1, 10)
    
    # If the random number is 5, stop the loop
    if x == 5:
        break
    
    # Print the random number, ensuring they stay on the same line
    print(x, end=' ')
    
    # Increment the counter by 1 for each number generated
    c += 1

# After the loop ends (when x == 5), print how many steps were taken
print("\nStopped after {} steps!".format(c))
