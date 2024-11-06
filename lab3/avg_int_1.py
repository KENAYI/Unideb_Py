# Initialize a variable to store the sum of numbers
sum = 0

# Take the number of inputs (n) from the user
n = int(input())

# Loop through the range of n to get n inputs
for i in range(n):
    # Take a number as input from the user
    num = int(input())
    
    # Add the input number to the sum
    sum += num

# Calculate the average by dividing the sum by the number of inputs and print it with 2 decimal places
print("{0:.2f}".format(sum / n))
