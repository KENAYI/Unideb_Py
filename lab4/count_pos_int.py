# Take an integer input for the number of values to check
n = int(input())

# Initialize a counter for the even positive numbers
c = 0

# Loop through 'n' number of inputs
for i in range(n):
    # Take an integer input from the user
    num = int(input())

    # Check if the number is positive and even
    if num > 0 and num % 2 == 0:
        # Increment the counter if the number is positive and even
        c += 1

# After the loop ends, print the count of positive even numbers
print(c)
