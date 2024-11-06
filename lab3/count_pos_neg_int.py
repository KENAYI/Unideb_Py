# Initialize counters for positive and negative numbers
pos = 0
neg = 0

# Infinite loop to keep asking for input
while True:
    # Take an integer input from the user
    n = int(input("n="))

    # If the input is 0, break out of the loop
    if n == 0:
        break

    # If the number is positive, increment the positive number counter
    if n > 0:
        pos += 1
    
    # If the number is negative, increment the negative number counter
    if n < 0:
        neg += 1

# Print the total count of positive and negative numbers
print("Positive numbers =", pos)
print("Negative numbers =", neg)
