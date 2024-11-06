# Initialize the variables: i to count the iterations, s to sum even numbers
i = 0
s = 0

# Infinite loop to keep asking for input until the condition is met
while True:
    # If 10 numbers have been processed, exit the loop
    if i == 10:
        break
    
    # Increment the iteration count
    i += 1
    
    # Take an integer input from the user
    n = int(input("n = "))
    
    # Skip odd numbers and continue to the next iteration
    if n % 2 != 0:
        continue
    
    # Add the even number to the sum
    s = s + n

# Print the sum of the even numbers entered after 10 iterations
print("Sum of even numbers:", s)
