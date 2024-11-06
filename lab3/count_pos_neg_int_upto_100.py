# Initialize variables for the sum, and counters for even and odd numbers
s = 0
even = 0
odd = 0

# Infinite loop to keep asking for input
while True:
    # Take an integer input from the user
    n = int(input("n="))
    
    # Add the input number to the sum
    s += n
    
    # If the sum exceeds 100, break out of the loop
    if s > 100:
        break
    
    # Check if the number is even
    if n % 2 == 0:
        even += 1
    else:
        # If it's not even, it's odd
        odd += 1

# After the loop ends, print the counts of even and odd numbers
print("Number of evens =", even)
print("Number of odds =", odd)
